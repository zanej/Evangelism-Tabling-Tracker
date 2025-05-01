# Evangelism-Tabling-Tracker
This is a lightweight Flask web app built for Texas A&amp;M’s THRIVE South Asian InterVarsity chapter to track conversations during evangelism tabling. It allows student leaders to log gospel conversations, prayer requests, contact info, and follow-up needs, all stored locally using SQLite.


# THRIVE Evangelism Tabling Tracker

This is a lightweight Flask web app built for Texas A&M University's THRIVE South Asian InterVarsity chapter. It helps student leaders track evangelism conversations during tabling, log prayer requests, record contact info, and flag follow-up needs. The project uses a simple maroon-themed interface inspired by Texas A&M's colors, with a Bible verse footer and THRIVE branding.

## Features

- Add new evangelism conversations with fields for:
  - Name
  - Contact info
  - Spiritual topic
  - Prayer request
  - Follow-up status
- View a full log of all conversations in reverse chronological order
- Local SQLite database that saves all entries persistently
- Includes a THRIVE logo, favicon, and a footer with Romans 10:14

## Tech Stack

- Python with Flask
- HTML/CSS (inline styling)
- SQLite for the backend database

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/your-username/thrive-evangelism-tracker.git
cd thrive-evangelism-tracker
Set up a virtual environment and install Flask:

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate      # On Windows
# or
source venv/bin/activate   # On Mac/Linux

pip install flask
Run the app:

bash
Copy
Edit
python app.py
Then open your browser and go to http://127.0.0.1:5000.

Project Structure
pgsql
Copy
Edit
.
├── app.py
├── evangelism_log.db          # Created automatically when the app runs
├── static/
│   └── thrive_logo.png        # Logo used in header and favicon
├── templates/
│   ├── index.html             # Homepage with log table
│   └── add.html               # Form to add a new conversation
└── README.md
Purpose
This project was built to serve the needs of THRIVE South Asian InterVarsity at Texas A&M. It’s designed to make gospel tabling more intentional by keeping track of who we talk to, what was shared, and how we can continue walking alongside people through prayer and follow-up.

Verse
“How can they believe in the one of whom they have not heard? And how can they hear without someone preaching to them?”
— Romans 10:14

Future Ideas
Add CSV export

Add user login support for multiple team members

Add email reminders for follow-ups

Deploy the app online for easier team access

Built by and for students involved in THRIVE South Asian InterVarsity at Texas A&M University.

vbnet
Copy
Edit

Let me know if you want a version with screenshots, live links, or deploy instructions later.
