# Cold Email Tool

A small Python tool for internship applications. It finds recruiter contacts at a company, writes a personalized cold email, and saves it as a Gmail draft with my resume attached. I review and send it myself.

## Files
- `find_emails.py` - finds contacts by company domain and department (uses the Hunter.io API)
- `write_email.py` - prints a cold email from a template
- `make_draft.py` - saves the email as a Gmail draft with the resume attached

## Setup
1. `pip install requests`
2. Set `HUNTER_API_KEY` and `GMAIL_APP_PASSWORD` as environment variables (never put them in the code).
3. Put a PDF with "resume" in its name in the folder.
4. Replace YOUR-EMAIL, YOUR-PHONE, and the name in the templates.

## Usage
    python find_emails.py amtrustgroup.com hr
    python make_draft.py recruiter@company.com "First Last" "Company" "Role" "reason"
