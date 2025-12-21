# How to Key the Newsletter into Your Hugo Site

Since I cannot access your Hugo project directly, here is the manual integration guide.

## Part 1: add the Subscription Form to Hugo

You want the premium subscription form to appear on your Hugo website.

### Step 1: Create a Shortcode
In your Hugo project, create a new file: `layouts/shortcodes/newsletter-form.html`

Paste this code inside it:

```html
<style>
.newsletter-card {
    background: rgba(255, 255, 255, 0.95);
    backdrop-filter: blur(20px);
    padding: 2rem;
    border-radius: 16px;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    border: 1px solid #e1e4e8;
    max-width: 450px;
    margin: 2rem auto;
    text-align: center;
    font-family: 'Inter', sans-serif;
}
.newsletter-card h3 { color: #0b6e4f; margin-top: 0; }
.newsletter-card input {
    width: 100%;
    padding: 12px;
    margin-bottom: 10px;
    border: 1px solid #ddd;
    border-radius: 8px;
    box-sizing: border-box;
}
.newsletter-card button {
    width: 100%;
    padding: 12px;
    background: #0b6e4f;
    color: white;
    border: none;
    border-radius: 8px;
    font-weight: bold;
    cursor: pointer;
}
.newsletter-card button:hover { background: #095c42; }
</style>

<div class="newsletter-card">
    <h3>🧬 Genome Daily</h3>
    <p>Get automated bioinformatics research signals every morning.</p>
    
    <!-- Replace with your Formspree Link -->
    <form action="https://formspree.io/f/YOUR_FORMSPREE_ID" method="POST">
        <input type="text" name="name" placeholder="First Name" required>
        <input type="email" name="email" placeholder="Work Email" required>
        <button type="submit">Subscribe Free</button>
    </form>
    <small style="color:#888; display:block; margin-top:10px;">Join 1,000+ Bioinformaticians</small>
</div>
```

### Step 2: Use it in Content
Now, in any markdown file (like `content/about.md` or a new `content/newsletter.md`), just write:

```markdown
{{< newsletter-form >}}
```

## Part 2: Hosting the Archives (Advanced)

If you want your *past issues* to appear on your website:

1.  **Configure Output**: We can modify `generate_issue.py` to output Markdown (`.md`) files instead of just HTML.
2.  **Sync**: You would set up a script to copy these `.md` files from the Newsletter folder to `hugo/content/posts/newsletter/`.

*If you want me to write the python script to convert issues to Hugo Markdown, let me know!*
