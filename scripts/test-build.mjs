#!/usr/bin/env node
/**
 * Dependency-free build validator for the Hugo portfolio.
 *
 * Walks the generated `public/` tree and asserts a set of SEO / accessibility /
 * correctness invariants on every HTML page. Run after `hugo` via `npm test`.
 *
 * Exit code 0 = all checks pass, 1 = one or more failures.
 */
import { readdirSync, readFileSync, statSync, existsSync } from "node:fs";
import { join, relative } from "node:path";

const ROOT = new URL("..", import.meta.url).pathname;
const PUBLIC = join(ROOT, "public");

if (!existsSync(PUBLIC)) {
  console.error("✗ public/ not found — run `hugo` (or `npm run build`) first.");
  process.exit(1);
}

/** Recursively collect every .html file under a directory. */
function htmlFiles(dir) {
  const out = [];
  for (const entry of readdirSync(dir)) {
    const full = join(dir, entry);
    if (statSync(full).isDirectory()) out.push(...htmlFiles(full));
    else if (entry.endsWith(".html")) out.push(full);
  }
  return out;
}

const failures = [];
const fail = (file, msg) => failures.push(`${relative(PUBLIC, file)}: ${msg}`);

/**
 * Non-indexed utility pages that intentionally lack full SEO/template markup:
 * - static/ form handlers & debug pages copied verbatim into public/
 * - auto-generated alias/redirect stubs without source markdown
 * These are excluded from content-page invariants.
 */
const SKIP = new Set([
  "contact-form.html",
  "contact-success.html",
  "debug-forms.html",
  "links.html",
  "subscribe-form.html",
  "subscribe-success.html",
  "subscribe.html",
  "test-form.html",
  "newsletter/2025-12-20-issue-1/index.html",
  "newsletter/2025-12-21-issue-1/index.html",
]);

const pages = htmlFiles(PUBLIC).filter((f) => !SKIP.has(relative(PUBLIC, f)));
if (pages.length === 0) {
  console.error("✗ No HTML pages found in public/.");
  process.exit(1);
}

for (const file of pages) {
  const html = readFileSync(file, "utf8");

  // 404 page is allowed to skip canonical/article checks.
  const is404 = file.endsWith("404.html");

  // SEO essentials.
  // Attribute values may be unquoted in Hugo's minified output, so quotes are optional.
  if (!/<title>[^<]+<\/title>/i.test(html)) fail(file, "missing or empty <title>");
  if (!/<meta\s+name=["']?description["']?\s+content=["'][^"']+["']/i.test(html))
    fail(file, "missing meta description");
  if (!is404 && !/<link\s+rel=["']?canonical["']?/i.test(html))
    fail(file, "missing canonical link");

  // Accessibility essentials.
  if (!/<html[^>]*\slang=/i.test(html)) fail(file, "<html> missing lang attribute");

  // Every <img> needs an alt attribute (may be empty for decorative images).
  const imgs = html.match(/<img\b[^>]*>/gi) || [];
  for (const img of imgs) {
    if (!/\salt=/i.test(img)) fail(file, `<img> without alt: ${img.slice(0, 80)}`);
  }

  // Any JSON-LD blocks must be valid JSON.
  const ldBlocks = html.match(/<script[^>]*type=["']application\/ld\+json["'][^>]*>([\s\S]*?)<\/script>/gi) || [];
  for (const block of ldBlocks) {
    const json = block.replace(/<script[^>]*>/i, "").replace(/<\/script>/i, "").trim();
    try {
      JSON.parse(json);
    } catch (e) {
      fail(file, `invalid JSON-LD: ${e.message}`);
    }
  }
}

console.log(`Checked ${pages.length} pages.`);
if (failures.length) {
  console.error(`\n✗ ${failures.length} check(s) failed:\n`);
  for (const f of failures) console.error("  - " + f);
  process.exit(1);
}
console.log("✓ All build validation checks passed.");
