# How to Activate the Subscription Form

I have created the `subscribe.html` page with a beautiful, embedded email form. 

**However, static pages (like GitHub Pages) cannot "save" emails by themselves.** They need a backend service to catch the submission.

## The Easiest Solution: Formspree (Free)

1.  Go to **[Formspree.io](https://formspree.io/)** and sign up (it's free).
2.  Click **"New Form"** and name it "Genome Daily".
3.  Copy the **Endpoint URL** they give you (e.g., `https://formspree.io/f/xvqrlqbw`).
4.  Open `subscribe.html` in this repo.
5.  Find `action="https://formspree.io/f/YOUR_FORMSPREE_ID"` and replace the URL with yours.
6.  Commit and push.

Now, whenever anyone enters their email on your site:
1.  Formspree will email YOU the new subscriber.
2.  You simply copy/paste that email into the `subscribers.csv` file in this repo once a week.

## Alternative: Google Forms
If you prefer not to use Formspree:
1.  Create a Google Form with an Email field.
2.  Get the "Pre-filled Link" for the email field.
3.  This is complicated to embed directly. I highly recommend **Formspree** or **Tally.so** instead for a clean look.
