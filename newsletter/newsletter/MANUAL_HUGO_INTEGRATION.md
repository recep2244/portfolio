
# 🚨 Manual Integration Required 🚨

You asked me to write to `/home/recep/Desktop/job_applications/hugo`, but I DO NOT have permission to edit files in that folder.

I can only edit files in:
`/home/recep/Desktop/Machine_Learning/projects/newsletter/newsletter`

## How to Add the Newsletter to Your Hugo Site (Copy-Paste)

1.  **Create the File**:
    Open a terminal and run this command yourself:
    ```bash
    nano /home/recep/Desktop/job_applications/hugo/layouts/shortcodes/newsletter.html
    ```

2.  **Paste This Code**:
    ```html
    <style>
    .newsletter-card {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(20px);
        padding: 2.5rem;
        border-radius: 16px;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
        border: 1px solid rgba(0,0,0,0.1);
        max-width: 480px;
        margin: 3rem auto;
        text-align: center;
        font-family: inherit;
    }
    .newsletter-card h3 { color: #0b6e4f; margin-top: 0; }
    .newsletter-card input {
        width: 100%; padding: 12px; margin-bottom: 10px;
        border: 1px solid #ddd; border-radius: 8px;
    }
    .newsletter-card button {
        width: 100%; padding: 12px; background: #0b6e4f; color: white;
        border: none; border-radius: 8px; font-weight: bold; cursor: pointer;
    }
    .newsletter-card button:hover { background: #095c42; }
    </style>

    <div class="newsletter-card">
        <h3>🧬 Genome Daily</h3>
        <p>Automated bioinformatics signals, delivered daily.</p>
        <form action="https://formspree.io/f/YOUR_FORMSPREE_ID" method="POST">
            <input type="text" name="name" placeholder="First Name" required>
            <input type="email" name="email" placeholder="Work Email" required>
            <button type="submit">Subscribe Free</button>
        </form>
    </div>
    ```

3.  **Use It**:
    Add `{{< newsletter >}}` to any page on your Hugo site.
