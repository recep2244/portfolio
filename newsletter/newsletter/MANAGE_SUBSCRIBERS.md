# How to Manage Subscribers & Google Forms

## 1. Create a Google Form
1. Go to [Google Forms](https://forms.google.com).
2. Create a new form titled "Subscribe to Genome Daily".
3. Add a **Short answer** question: "Email Address".
   - Turn on **Required**.
   - (Optional) Add a "Name" field.
4. Click **Send** (top right) -> **Link icon** -> **Shorten URL**.
5. Copy this URL.

## 2. Update Configuration
1. Open `generate_config.json` in this repo.
2. Find `"subscribe_link": "INSERT_LINK_TO_YOUR_GOOGLE_FORM"`.
3. Paste your form link there.
4. Commit and push.

## 3. Managing Subscribers (Once a week)
Since we are keeping it simple, you will update the list manually.

1. Go to your Google Form -> **Responses** tab.
2. Click **View in Sheets** (green icon) or **Download CSV**.
3. Copy the emails.
4. Open `subscribers.csv` in your GitHub repo (or locally).
5. Paste the new emails at the bottom.
   - Format: `email,name,status`
   - Example: `newguy@gmail.com,,active`
6. Commit changes.

*This manual step ensures no spam bots get onto your mailing list automatically.*
