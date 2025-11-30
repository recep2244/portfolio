# GitHub Pages Setup Instructions

Your Hugo site now has an automated deployment workflow! Follow these steps to enable GitHub Pages:

## Step 1: Configure GitHub Pages Settings

1. Go to your repository on GitHub: `https://github.com/recep2244/portfolio`
2. Click on **Settings** (top navigation)
3. In the left sidebar, click **Pages** (under "Code and automation")
4. Under **Source**, select:
   - **Source:** `GitHub Actions` (not "Deploy from a branch")
5. Click **Save**

## Step 2: Trigger the Workflow

The workflow will automatically run when you push to the `main` branch. You can also:
- Go to **Actions** tab in your repository
- Click on "Deploy Hugo site to Pages" workflow
- Click **Run workflow** button
- Select the `main` branch
- Click **Run workflow**

## Step 3: Check Deployment Status

1. Go to the **Actions** tab in your repository
2. You should see a workflow run called "Deploy Hugo site to Pages"
3. Wait for it to complete (usually 1-2 minutes)
4. Once complete, your site will be live at: `https://recep2244.github.io/portfolio/`

## Troubleshooting

### If the workflow fails:
- Check the error message in the Actions tab
- Ensure your `hugo.yaml` has the correct `baseURL: 'https://recep2244.github.io/portfolio/'`
- Make sure GitHub Pages is enabled in Settings → Pages

### If the site doesn't update:
- Hard refresh your browser: `Ctrl+Shift+R` (Windows/Linux) or `Cmd+Shift+R` (Mac)
- Clear your browser cache
- Wait a few minutes for CDN to update

## Current Setup

✅ **Workflow File:** `.github/workflows/hugo.yml`  
✅ **Base URL:** `https://recep2244.github.io/portfolio/`  
✅ **Branch:** `main`  
✅ **Hugo Version:** 0.128.0 Extended

Your site will automatically deploy whenever you push changes to the `main` branch!
