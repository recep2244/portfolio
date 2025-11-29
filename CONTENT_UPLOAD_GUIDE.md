# Content Upload Instructions for Hugo Portfolio

This guide will help you add new blog posts and podcast episodes to your Hugo portfolio website.

## 📝 Adding Blog Posts

### Step 1: Edit the Data File
Open the file: `data/cv.yaml`

### Step 2: Add Your Blog Entry
Scroll to the `blogs:` section (near the end of the file) and add a new entry following this format:

```yaml
blogs:
  - title: "Your Blog Post Title"
    summary: "A brief 1-2 sentence description of what the post covers."
    link: "https://recepadiyaman.com/blog/your-post-url"
    tags: ["Tag1", "Tag2", "Tag3"]
```

### Example:
```yaml
  - title: "Optimizing Protein-Ligand Docking with Machine Learning"
    summary: "Exploring how ML models can improve docking pose prediction accuracy by 40% compared to traditional methods."
    link: "https://recepadiyaman.com/blog/ml-docking-optimization"
    tags: ["Machine Learning", "Docking", "Drug Discovery"]
```

### Step 3: Deploy
After editing, commit and push your changes:
```bash
git add data/cv.yaml
git commit -m "Add new blog post: [Your Title]"
git push origin main
```

The site will automatically rebuild and deploy via GitHub Actions.

---

## 🎙️ Adding Podcast Episodes

### Step 1: Upload Your Video to YouTube
1. Go to [YouTube Studio](https://studio.youtube.com/)
2. Click "Create" → "Upload videos"
3. Upload your podcast episode
4. Add a compelling title and description
5. Add relevant tags (e.g., "Bioinformatics", "Protein Engineering", "AI")
6. Set visibility to "Public"
7. Copy the video URL (e.g., `https://www.youtube.com/watch?v=ABC123XYZ`)

### Step 2: Extract the Video ID
From the URL `https://www.youtube.com/watch?v=ABC123XYZ`, the video ID is `ABC123XYZ`

### Step 3: Edit the Data File
Open the file: `data/cv.yaml`

### Step 4: Add Your Podcast Entry
Scroll to the `podcasts:` section and add a new entry:

```yaml
podcasts:
  - title: "Your Podcast Episode Title"
    description: "A brief description of what you discuss in this episode."
    youtube_url: "https://www.youtube.com/watch?v=YOUR_VIDEO_ID"
    date: "2024-12-15"
    duration: "42 min"
```

### Example:
```yaml
  - title: "Cryo-EM and AlphaFold: A Perfect Partnership"
    description: "Discussing how experimental structures and AI predictions complement each other in modern structural biology."
    youtube_url: "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    date: "2024-12-15"
    duration: "42 min"
```

### Step 5: Update Your YouTube Channel Link
If this is your first podcast, update your YouTube channel URL in the `contact:` section:

```yaml
contact:
  youtube: "https://www.youtube.com/@YourActualChannelName"
```

Replace `@YourActualChannelName` with your real channel handle.

### Step 6: Deploy
Commit and push your changes:
```bash
git add data/cv.yaml
git commit -m "Add new podcast episode: [Your Title]"
git push origin main
```

---

## 🚀 Quick Reference

### File Locations
- **Blog & Podcast Data**: `data/cv.yaml`
- **Blog Template**: `layouts/partials/blogs.html`
- **Podcast Template**: `layouts/partials/podcasts.html`

### Deployment
All changes are automatically deployed via GitHub Actions when you push to the `main` branch.

**Deployment URL**: https://recep2244.github.io/portfolio/

### Typical Deployment Time
- GitHub Actions build: ~2-3 minutes
- DNS propagation: Instant (GitHub Pages)

---

## 💡 Tips

### For Blogs:
- Keep summaries concise (1-2 sentences)
- Use 2-4 relevant tags
- Ensure your blog link is accessible

### For Podcasts:
- Create eye-catching YouTube thumbnails
- Use descriptive titles (good for SEO)
- Add timestamps in the YouTube description
- Engage with comments to build community
- Cross-promote on Twitter/LinkedIn

### YouTube Best Practices:
1. **Thumbnail**: Use high-contrast text, faces, or diagrams
2. **Title**: Front-load important keywords (e.g., "AlphaFold3 vs RoseTTAFold: ...")
3. **Description**: Include timestamps, links to papers, and your contact info
4. **Tags**: Use 5-10 relevant tags
5. **Playlists**: Organize episodes into themed playlists

---

## 🐛 Troubleshooting

### Blog not showing up?
- Check YAML syntax (indentation must be exact)
- Ensure the `link` field has a valid URL
- Clear your browser cache

### Podcast thumbnail not loading?
- Verify the YouTube video is set to "Public"
- Check that the video ID in the URL is correct
- Wait a few minutes for YouTube to process the video

### Changes not deploying?
1. Check GitHub Actions: https://github.com/recep2244/portfolio/actions
2. Look for any failed builds
3. Review error messages in the build logs

---

## 📧 Need Help?

If you encounter issues, check the GitHub Actions logs or reach out for assistance.

**Happy Publishing! 🎉**
