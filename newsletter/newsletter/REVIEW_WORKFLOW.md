# Paper Review Workflow

This workflow allows you to **manually review and select papers** before sending your newsletter.

## 🎯 Overview

Instead of automatically sending all generated papers, you now have a visual interface to:
1. Review all fetched papers
2. Select which ones to include (checkboxes)
3. Export only your selections
4. Send the curated newsletter

---

## 📋 Step-by-Step Workflow

### **Step 1: Generate Papers (As Usual)**
```bash
cd /home/recep/Desktop/Machine_Learning/projects/hugo/newsletter/newsletter
python generate_issue.py --date today
```

This creates: `issues/2025-01-15.json` (or whatever today's date is)

---

### **Step 2: Open the Review Interface**

**Option A: Open in Browser (Recommended)**
```bash
# Open the review interface
xdg-open review_papers.html
# or
firefox review_papers.html
```

**Option B: Use Python HTTP Server**
```bash
python -m http.server 8000
# Then visit: http://localhost:8000/review_papers.html
```

---

### **Step 3: Load & Review Papers**

In the interface:
1. Click **"📁 Load JSON File"**
2. Select your generated issue: `issues/2025-01-15.json`
3. **Review the papers** - you'll see all papers organized by section:
   - Quick Reads
   - AI News  
   - Industry News

---

### **Step 4: Select Papers**

Use the controls:
- **✓ Select All** - Include everything
- **✗ Deselect All** - Start fresh
- **Top 5** / **Top 10** - Quick selection
- **Manual checkboxes** - Click individual papers

**Tips:**
- Selected papers have a **blue border**
- The counter shows **X Selected** in real-time
- Papers are sorted by relevance

---

### **Step 5: Export Selected Papers**

When you're done selecting:
1. Click **"🚀 Export Selected Papers"**
2. Click **"💾 Download as JSON"**
3. Save as: `selected-papers-2025-01-15.json`

---

### **Step 6: Create Curated Issue**

Back in your terminal:
```bash
python review_helper.py issues/2025-01-15.json selected-papers-2025-01-15.json
```

This creates: `issues/2025-01-15-curated.json`

---

### **Step 7: Send the Newsletter**

Use the **curated** issue instead of the original:
```bash
# Dry run first
python send_newsletter.py --issue issues/2025-01-15-curated.json --dry-run

# Send for real
python send_newsletter.py --issue issues/2025-01-15-curated.json
```

---

## 🚀 Quick Workflow Script

Create a bash script to automate this:

```bash
#!/bin/bash
# review_and_send.sh

DATE=$(date +%Y-%m-%d)
ISSUE="issues/${DATE}.json"
SELECTED="selected-papers-${DATE}.json"
CURATED="issues/${DATE}-curated.json"

echo "📬 Generating papers for ${DATE}..."
python generate_issue.py --date today

echo ""
echo "✅ Papers generated! Opening review interface..."
echo "👉 Load this file: ${ISSUE}"
xdg-open review_papers.html

echo ""
read -p "Press ENTER after you've selected papers and downloaded the JSON..."

if [ ! -f "${SELECTED}" ]; then
    echo "❌ Selected papers file not found: ${SELECTED}"
    echo "   Make sure you downloaded it from the review interface"
    exit 1
fi

echo ""
echo "📝 Creating curated issue..."
python review_helper.py "${ISSUE}" "${SELECTED}" "${CURATED}"

echo ""
read -p "Ready to send? Press ENTER to continue (or Ctrl+C to cancel)..."

echo ""
echo "🚀 Sending newsletter..."
python send_newsletter.py --issue "${CURATED}"

echo ""
echo "✅ Done! Newsletter sent with your selected papers."
```

**Usage:**
```bash
chmod +x review_and_send.sh
./review_and_send.sh
```

---

## 💡 Pro Tips

### **Filter by Keywords**
In the browser console:
```javascript
// Show only AlphaFold-related papers
document.querySelectorAll('.paper-card').forEach(card => {
    if (!card.textContent.toLowerCase().includes('alphafold')) {
        card.style.display = 'none';
    }
});
```

### **Select by Section**
- Click the section title to collapse/expand
- Use browser search (Ctrl+F) to find specific topics

### **Save Your Selections**
- The interface exports a clean JSON
- You can reuse it or modify it manually
- Keep a backup for your records

---

## 🔧 Customization

### Add More Controls

Edit `review_papers.html` and add:

```html
<button class="btn btn-secondary" onclick="filterByKeyword('alphafold')">
    AlphaFold Only
</button>
```

```javascript
function filterByKeyword(keyword) {
    deselectAll();
    allPapers.forEach((paper, idx) => {
        const text = JSON.stringify(paper).toLowerCase();
        if (text.includes(keyword.toLowerCase())) {
            selectedIndices.add(idx);
        }
    });
    renderPapers();
    updateStats();
}
```

---

## 📝 Notes

- The review interface works **offline** (pure HTML/JS)
- No data is sent to any server
- All processing happens in your browser
- The interface is **mobile-friendly** if you need to review on your phone

---

## 🐛 Troubleshooting

**"No papers loaded"**
- Make sure you're loading the correct JSON file
- Check that `generate_issue.py` ran successfully

**Can't download JSON**
- Check browser download settings
- Try "Copy to Clipboard" instead

**Papers look wrong**
- Clear browser cache
- Reload the page
- Check the original JSON file

---

## 🎯 Next Steps

After setting up this workflow once:
1. It takes ~5 minutes to review and select papers
2. Much better quality control than blind auto-send
3. You maintain full editorial control

**Your subscribers will receive only the papers YOU chose!** 📬
