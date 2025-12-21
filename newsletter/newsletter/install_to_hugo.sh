#!/bin/bash
set -e

# Define paths
NEWSLETTER_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
HUGO_DIR="/home/recep/Desktop/Machine_Learning/projects/hugo"

echo "🚀 Installing Newsletter components to Hugo site at: $HUGO_DIR"

if [ ! -d "$HUGO_DIR" ]; then
    echo "❌ Error: Hugo directory not found at $HUGO_DIR"
    exit 1
fi

# 1. Create the Shortcode (for embedding in posts)
# This allows usage of {{< newsletter >}} in markdown files
mkdir -p "$HUGO_DIR/layouts/shortcodes"
SHORTCODE_FILE="$HUGO_DIR/layouts/shortcodes/newsletter.html"

cat <<EOF > "$SHORTCODE_FILE"
<style>
.newsletter-card {
    background: rgba(255, 255, 255, 0.95);
    backdrop-filter: blur(20px);
    padding: 2.5rem;
    border-radius: 16px;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 10px 15px -3px rgba(0, 0, 0, 0.1);
    border: 1px solid rgba(0,0,0,0.05);
    max-width: 480px;
    margin: 3rem auto;
    text-align: center;
    font-family: inherit;
    color: #1c2b26;
}
.newsletter-card h3 { 
    color: #0b6e4f; 
    margin-top: 0; 
    margin-bottom: 0.5rem;
    font-size: 1.5rem;
    font-weight: 700;
}
.newsletter-tagline {
    color: #58655f;
    line-height: 1.6;
    margin-bottom: 1.5rem;
    font-size: 0.95rem;
}
.newsletter-card input {
    width: 100%;
    padding: 12px 16px;
    margin-bottom: 10px;
    border: 2px solid #e1e4e8;
    border-radius: 8px;
    box-sizing: border-box;
    font-size: 1rem;
    transition: border-color 0.2s;
}
.newsletter-card input:focus {
    outline: none;
    border-color: #0b6e4f;
}
.newsletter-card button {
    width: 100%;
    padding: 14px;
    background: #0b6e4f;
    color: white;
    border: none;
    border-radius: 8px;
    font-weight: 600;
    font-size: 1rem;
    cursor: pointer;
    transition: background 0.2s;
}
.newsletter-card button:hover { 
    background: #095c42; 
}
.newsletter-privacy {
    color: #9ca3af;
    font-size: 0.75rem;
    margin-top: 1rem;
}
</style>

<div class="newsletter-card">
    <h3>🧬 Genome Daily</h3>
    <p class="newsletter-tagline">Automated bioinformatics signals. No noise.</p>
    
    <!-- Replace 'YOUR_FORMSPREE_ID' with your actual ID from https://formspree.io -->
    <form action="https://formspree.io/f/YOUR_FORMSPREE_ID" method="POST">
        <input type="text" name="name" placeholder="First Name" required>
        <input type="email" name="email" placeholder="Work Email" required>
        <button type="submit">Subscribe Free</button>
    </form>
    <div class="newsletter-privacy">Join 1,000+ Bioinformaticians. Unsubscribe anytime.</div>
</div>
EOF
echo "✅ Created Shortcode: $SHORTCODE_FILE"

# 2. Copy the full landing page to 'static'
# This makes it available at yoursite.com/subscribe.html
if [ -f "$NEWSLETTER_DIR/subscribe.html" ]; then
    mkdir -p "$HUGO_DIR/static"
    cp "$NEWSLETTER_DIR/subscribe.html" "$HUGO_DIR/static/subscribe.html"
    echo "✅ Copied Landing Page: $HUGO_DIR/static/subscribe.html"
else
    echo "⚠️ Warning: subscribe.html not found in $NEWSLETTER_DIR"
fi

echo "---------------------------------------------------"
echo "🎉 Integration Complete!"
echo "1. Edit '$SHORTCODE_FILE' to add your real Formspree ID."
echo "2. Use {{< newsletter >}} in any markdown post."
echo "---------------------------------------------------"
