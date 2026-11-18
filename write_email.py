import sys

if len(sys.argv) < 4:
    print('Usage: python write_email.py "Full Name" "Company" "Role" ["optional reason you like the company"]')
    sys.exit()

full_name = sys.argv[1]
company = sys.argv[2]
role = sys.argv[3]
reason = sys.argv[4] if len(sys.argv) > 4 else ""

first_name = full_name if "team" in full_name.lower() else full_name.split()[0]

reason_line = ""
if reason:
    reason_line = f"I'm especially interested in {company} because {reason}. "

email = f"""Subject: {role} application - Ronil Manger (UB)

Hi {first_name},

I'm a computer science junior at the University at Buffalo, and I recently applied for the {role} position at {company}. {reason_line}I wanted to introduce myself and share how interested I am in the role.

I interned at EPMware, where I helped build an internal AWS dashboard that shows Elastic Beanstalk environment data, and I helped with debugging, testing, and code reviews. I also build Java projects using object-oriented design.

I've attached my resume. If you have a few minutes, I'd welcome a short conversation about the internship. Thank you for your time.

Best,
Ronil Manger
YOUR-PHONE
YOUR-EMAIL
"""

print(email)
