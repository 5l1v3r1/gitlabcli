import requests, sys

def profile(api_url, user, token):
    headers = {"Private-Token": "%s" % token}
    login = requests.get(api_url + 'user', headers=headers)

    # Get Data
    data = login.json()
    uname = data["username"]
    name = data["name"]
    location = data["location"]
    company = data["organization"]
    email = data["email"]
    url = data["web_url"]
    website = data["website_url"]
    created = data["created_at"]
    bio = data["bio"]

    print('''
    Username:      %s
    Name:          %s
    Location:      %s
    Company:       %s
    Email:         %s
    Profile URL:   %s
    Website:       %s
    Created:       %s
    Bio:           %s
    ''' % (uname, name, location, company, email, url, website, created, bio))
