# How to Deploy Your Hugo Site

## Option 1: Netlify (Recommended)
1.  **Create a GitHub Repository**:
    *   Go to GitHub and create a new repository (e.g., `my-portfolio`).
    *   Push your code to this repository:
        ```bash
        git init
        git add .
        git commit -m "Initial commit"
        git branch -M main
        git remote add origin https://github.com/YOUR_USERNAME/my-portfolio.git
        git push -u origin main
        ```
2.  **Connect to Netlify**:
    *   Go to [Netlify.com](https://www.netlify.com) and sign up.
    *   Click "Add new site" -> "Import from an existing project".
    *   Select "GitHub" and choose your repository.
3.  **Configure Build Settings**:
    *   **Build command**: `hugo`
    *   **Publish directory**: `public`
    *   Netlify should detect these automatically.
4.  **Deploy**: Click "Deploy site". It will be live in seconds!

## Option 2: GitHub Pages
1.  Update `hugo.yaml`:
    ```yaml
    baseURL: "https://YOUR_USERNAME.github.io/my-portfolio/"
    ```
2.  Push your code to GitHub.
3.  Go to Repository Settings -> Pages.
4.  Select "GitHub Actions" as the source.
5.  Hugo provides a pre-built action for this.

## Running Locally
Always check your site locally before deploying:
```bash
hugo server
```
