import os
import sys
import time
import imaplib
import mimetypes
from email.message import EmailMessage

GMAIL = "YOUR-EMAIL"
APP_PASSWORD = os.environ.get("GMAIL_APP_PASSWORD")

if len(sys.argv) < 5:
    print('Usage: python make_draft.py email "Full Name" "Company" "Role" ["reason"]')
    sys.exit()

to_addr = sys.argv[1]
full_name = sys.argv[2]
company = sys.argv[3]
role = sys.argv[4]
reason = sys.argv[5] if len(sys.argv) > 5 else ""

resumes = [f for f in os.listdir(".")
           if "resume" in f.lower() and f.lower().endswith((".pdf", ".docx"))]
if not resumes:
    print("No resume found. Put a file with 'resume' in its name in this folder.")
    sys.exit()
resume_path = resumes[0]

first_name = full_name if "team" in full_name.lower() else full_name.split()[0]
reason_line = ""
if reason:
    reason_line = f"I'm especially interested in {company} because {reason}. "

subject = f"{role} application - Ronil Manger (UB)"
body = f"""Hi {first_name},

I'm a computer science junior at the University at Buffalo, and I recently applied for the {role} position at {company}. {reason_line}I wanted to introduce myself and share how interested I am in the role.

I interned at EPMware, where I helped build an internal AWS dashboard that shows Elastic Beanstalk environment data, and I helped with debugging, testing, and code reviews. I also build Java projects using object-oriented design.

I've attached my resume. If you have a few minutes, I'd welcome a short conversation about the internship. Thank you for your time.

Best,
Ronil Manger
YOUR-PHONE
YOUR-EMAIL
"""

msg = EmailMessage()
msg["From"] = GMAIL
msg["To"] = to_addr
msg["Subject"] = subject
msg.set_content(body)

kind = mimetypes.guess_type(resume_path)[0] or "application/octet-stream"
maintype, subtype = kind.split("/")
with open(resume_path, "rb") as f:
    msg.add_attachment(f.read(), maintype=maintype, subtype=subtype, filename=resume_path)

imap = imaplib.IMAP4_SSL("imap.gmail.com")
imap.login(GMAIL, APP_PASSWORD)
imap.append("[Gmail]/Drafts", "\\Draft", imaplib.Time2Internaldate(time.time()), msg.as_bytes())
imap.logout()

print("Draft saved with", resume_path, "attached. Open Gmail > Drafts to review and send.")
