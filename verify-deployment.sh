#!/bin/bash

# Hugo Site Deployment Verification Script
# This script checks if your Hugo site is ready for deployment

echo "🔍 Verifying Hugo Site Configuration..."
echo ""

# Check 1: Verify baseURL
echo "✓ Checking baseURL..."
BASE_URL=$(grep "baseURL:" hugo.yaml | cut -d"'" -f2)
echo "  Current baseURL: $BASE_URL"
if [ "$BASE_URL" != "https://recep2244.github.io/portfolio/" ]; then
    echo "  ⚠️  WARNING: baseURL should be 'https://recep2244.github.io/portfolio/'"
else
    echo "  ✅ baseURL is correct"
fi
echo ""

# Check 2: Verify workflow files exist
echo "✓ Checking GitHub Actions workflows..."
if [ -f ".github/workflows/hugo.yml" ]; then
    echo "  ✅ hugo.yml exists"
elif [ -f ".github/workflows/deploy.yml" ]; then
    echo "  ⚠️  deploy.yml found (expected hugo.yml)"
else
    echo "  ❌ No Pages workflow found (.github/workflows/hugo.yml)"
fi
echo ""

# Check 3: Verify package files exist
echo "✓ Checking npm dependencies..."
if [ -f "package.json" ] && [ -f "package-lock.json" ]; then
    echo "  ✅ package.json and package-lock.json exist"
else
    echo "  ❌ package files missing"
fi
echo ""

# Check 4: Test build
echo "✓ Testing Hugo build..."
if command -v npx &> /dev/null; then
    npx hugo --minify &> /dev/null
    if [ $? -eq 0 ]; then
        echo "  ✅ Hugo build successful"
        PAGE_COUNT=$(find public -name "index.html" | wc -l)
        echo "  📄 Generated $PAGE_COUNT pages"
    else
        echo "  ❌ Hugo build failed"
        echo "  Run 'npx hugo --minify' to see errors"
    fi
else
    echo "  ⚠️  npx not found, skipping build test"
fi
echo ""

# Check 5: Verify public directory
echo "✓ Checking public directory..."
if [ -d "public" ]; then
    if [ -f "public/index.html" ]; then
        echo "  ✅ public/index.html exists"
    else
        echo "  ❌ public/index.html missing"
    fi
else
    echo "  ⚠️  public directory not found (run 'npx hugo --minify')"
fi
echo ""

# Check 6: Verify live site status
echo "✓ Checking live site..."
if command -v curl &> /dev/null; then
    HTTP_STATUS=$(curl -s -o /dev/null -w "%{http_code}" "$BASE_URL")
    if [ "$HTTP_STATUS" = "200" ]; then
        echo "  ✅ Site responds with HTTP 200"
    else
        echo "  ⚠️  Site responds with HTTP $HTTP_STATUS (not live yet)"
    fi
else
    echo "  ⚠️  curl not found, skipping live check"
fi
echo ""

# Summary
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📋 DEPLOYMENT CHECKLIST:"
echo ""
echo "LOCAL SETUP (Verified above):"
echo "  ✓ Configuration files"
echo "  ✓ Build process"
echo ""
echo "GITHUB PAGES SETUP (You must do these manually):"
echo "  1. Go to: https://github.com/recep2244/portfolio/settings/pages"
echo "  2. Under 'Source', select: GitHub Actions"
echo "  3. Click Save"
echo ""
echo "  4. Go to: https://github.com/recep2244/portfolio/actions"
echo "  5. Check if workflow 'Deploy Hugo site to Pages' ran"
echo "  6. If not, click 'Run workflow' button"
echo ""
echo "  7. Wait 2 minutes, then visit:"
echo "     https://recep2244.github.io/portfolio/"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
