import os
import sys
import requests

API_KEY = os.environ.get("HUNTER_API_KEY")

def find_contacts(domain, department=None):
    url = "https://api.hunter.io/v2/domain-search"
    params = {"domain": domain, "api_key": API_KEY, "limit": 10}
    if department:
        params["department"] = department

    response = requests.get(url, params=params).json()

    if "data" not in response:
        print("Hunter returned an error:", response)
        return

    data = response["data"]
    print("Company:", data.get("organization"))
    print("Email pattern:", data.get("pattern"))
    print()
    for person in data["emails"]:
        name = f"{person.get('first_name')} {person.get('last_name')}"
        print(name, "|", person.get("position"), "|", person["value"])

domain = sys.argv[1]
department = sys.argv[2] if len(sys.argv) > 2 else None
find_contacts(domain, department)
