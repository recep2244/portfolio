# How to Deploy Your Hugo Site

Since you want to avoid Netlify, here are the two best alternatives. **Your project is already pre-configured for Option 1 (GitHub Pages).**

## Option 1: GitHub Pages (Recommended & Pre-configured)
Your project already includes a GitHub Actions workflow (`.github/workflows/hugo.yml`) to automatically deploy to GitHub Pages.

### Steps to Activate:
1.  **Push to GitHub**:
    Ensure your code is pushed to a GitHub repository (e.g., named `portfolio`).
    ```bash
    git add .
    git commit -m "Ready for deployment"
    git push origin main
    ```

2.  **Configure Repository Settings**:
    *   Go to your repository on GitHub.
    *   Navigate to **Settings** > **Pages** (in the left sidebar).
    *   Under **Build and deployment** > **Source**, select **GitHub Actions**.
    *   *Note: Do not select "Deploy from a branch". You must select "GitHub Actions" because we are using a custom workflow.*

3.  **Verify `baseURL`**:
    *   Open `hugo.yaml`.
    *   Ensure `baseURL` matches your GitHub Pages URL:
        *   Format: `https://<USERNAME>.github.io/<REPO_NAME>/`
        *   Current value: `https://recep2244.github.io/portfolio/` (Make sure your repo is named `portfolio`)

4.  **Check Deployment**:
    *   Go to the **Actions** tab in your repository.
    *   You should see a workflow running. Once green, your site is live!

---

## Option 2: Vercel (Easiest Setup)
Vercel is incredibly fast and requires zero configuration files.

1.  **Sign Up**: Go to [vercel.com](https://vercel.com) and sign up with GitHub.
2.  **Import Project**:
    *   Click **"Add New..."** > **"Project"**.
    *   Select your GitHub repository.
3.  **Configure**:
    *   **Framework Preset**: Vercel usually detects "Hugo" automatically.
    *   **Build Command**: `hugo --gc --minify` (default is usually fine).
    *   **Output Directory**: `public` (default).
4.  **Deploy**: Click **Deploy**.
5.  **Update BaseURL**:
    *   Once deployed, Vercel gives you a URL (e.g., `project-name.vercel.app`).
    *   Update `baseURL` in `hugo.yaml` to this new URL if you want links to work perfectly, although Vercel handles relative links well.

---

## Running Locally
Always check your site locally before deploying:
```bash
npm run dev
# OR
hugo server
```
