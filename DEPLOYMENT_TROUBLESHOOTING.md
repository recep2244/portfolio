# 🔧 Website Deployment Troubleshooting

## Current Status
Your Hugo site builds successfully locally (15 pages generated). The deployment workflow is configured, but the site isn't live yet.

## ✅ Step-by-Step Fix

### 1. Configure GitHub Pages (REQUIRED - Do this first!)

Go to: **https://github.com/recep2244/portfolio/settings/pages**

Under **"Build and deployment"**:
- **Source:** Select `GitHub Actions` from the dropdown
  - **NOT** "Deploy from a branch"
  - This is the most common issue!

Click **Save** if you made changes.

### 2. Verify Workflow Ran Successfully

Go to: **https://github.com/recep2244/portfolio/actions**

Look for:
- Workflow named "Deploy Hugo to GitHub Pages"
- Green checkmark ✅ (success) or red X ❌ (failure)

**If you see a red X:**
- Click on the failed workflow
- Click on "build" or "deploy" job
- Expand the failed step to see the error
- Common errors:
  - "Resource not accessible by integration" → GitHub Pages not enabled
  - "npm ci" fails → Delete `node_modules` and push again
  - "hugo command not found" → Workflow uses wrong Hugo setup

**If no workflows ran:**
- Make sure you pushed to the `main` branch
- Check that `.github/workflows/deploy.yml` exists in your repository

### 3. Force Re-run Workflow

If the workflow exists but didn't run:

1. Go to **Actions** tab
2. Click "Deploy Hugo to GitHub Pages" on the left
3. Click **Run workflow** button (top right)
4. Select `main` branch
5. Click green **Run workflow** button

### 4. Wait for Deployment

- Workflow takes 1-2 minutes
- Once complete, site will be at: `https://recep2244.github.io/portfolio/`
- First load might take an extra minute for CDN

### 5. Hard Refresh Your Browser

Even after deployment succeeds:
- **Windows/Linux:** `Ctrl + Shift + R`
- **Mac:** `Cmd + Shift + R`
- Or clear browser cache completely

## 🔍 Quick Diagnostics

### Check if workflow file exists:
```bash
ls .github/workflows/
```
Should show: `deploy.yml`, `hugo.yml`, `static.yml`

### Check if site builds locally:
```bash
npx hugo --minify
```
Should show "Total in X ms" with no errors

### Check if public directory was created:
```bash
ls public/
```
Should show: `index.html` and other files

## 🚨 Common Issues

### "404 - Site not found"
- **Cause:** GitHub Pages not configured to use GitHub Actions
- **Fix:** Step 1 above - select "GitHub Actions" as source

### "Workflow not running"
- **Cause:** No commits to trigger it
- **Fix:** Make a small change and push, or manually trigger (Step 3)

### "Workflow fails at 'npm ci'"
- **Cause:** Corrupted node_modules or cache
- **Fix:** Delete `node_modules` locally and push

### "Workflow fails at 'Build site'"
- **Cause:** Hugo build error
- **Fix:** Run `npx hugo --minify` locally to see the error

### "Site loads but looks broken"
- **Cause:** CSS/JS not loading (wrong baseURL)
- **Fix:** Verify `hugo.yaml` has `baseURL: 'https://recep2244.github.io/portfolio/'`

## 📞 Next Steps

1. Complete **Step 1** (configure GitHub Pages)
2. Check **Step 2** (verify workflow ran)
3 If workflow succeeded, wait 2 minutes then visit: `https://recep2244.github.io/portfolio/`
4. If still issues, send me the error message from the failed workflow step

## ✨ Expected Result

Once working, every push to `main` will automatically:
1. Build your Hugo site
2. Deploy to GitHub Pages
3. Update live site within 1-2 minutes

Your site URL: **https://recep2244.github.io/portfolio/**
