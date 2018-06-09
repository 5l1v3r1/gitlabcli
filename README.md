# gitlab.py v0.0.4

***

Interract with the GitLab API. Find info about users and repos.

You'll need to login with your GitLab username and API token, which you can generate here: https://gitlab.com/profile/personal_access_tokens

Installation:
```Shell
pip install -r required.txt
```

Note auth.py:
```Python
# Your username
user = ''

# Your access token
token = ''
```

Usage:
```Shell
python gitlab.py
```

Features:
```Shell
Commands:
    Global:
    clone <url>                       | Clone a project
    clone all <username>              | Clone all user projects
    clear                             | Clear terminal screen
    exit/quit                         | Exit the console

    Users:
    get repos <username>              | Get all users projects
    get starred                       | Get all your starred projects
    get issues <project_id>           | Show issues for this project
    get commits <project_id>          | Show all commits for this project
    get files <project_id>            | List files in this project
    search <user>                     | Search for a user
    find <string>                     | Search for projects by string
    blocks                            | List blocked users
    star/unstar <project_id>          | Star or unstar a users project

    Your account:
    profile                           | Show your profile
    delete <project_id>               | Delete a project
    create <project_name>             | Create a project
    edit repo/item/string             | Valid Items: name, description, homepage, private
    donothitenternow                  | Do Not Hit Enter Now -> DELETES ALL YOUR PROJECTS !!

    Sudo:
    add email <user_id> <email>                       | Add a email account for this user
    block/unblock <user_id>                           | Block/unblock this user
    create_user <email> <password> <username> <name>  | Create a new user
    delete_user <user_id>                             | Delete a user

```

Base code:
```Python

headers = {"Private-Token": "%s" % token}
login = requests.get('https://www.gitlab.com/api/v4/projects', headers=headers)
print(login.json()) # Show other links and format from here.

```

Test API:
```Shell
curl -H "PRIVATE-TOKEN: <TOKEN>" -i https://www.gitlab.com/api/v4/projects
```

GET command template (example):
```Python
import requests, os, sys

def command_name(api_url, user, token, key_in_dict):

    headers = {"Private-Token": "%s" % token}
    login = requests.get(api_url, headers=headers)

    output = login.json()

    print(output.keys()) # output all keys in dict
    data = output[key_in_dict] # Which will be "html_url" in this case.

# Usage:
#command_name(api_url, user, token, "html_url")

# Add on top of github.py
#from commands.command_name import *
```

POST command template (example):
```Python
import requests, json, sys, os

def create_repo(api_url, user, token, repo):
    headers = {"Private-Token": "%s" % token}
    payload = {'name': '%s' % repo, 'description': 'Created with Gitlab API', 'visibility': 'public'}
    login = requests.post(api_url + 'projects', headers=headers, data=payload)

    if login.status_code == 201:
        print('\033[32m[OK]\033[0m Project created')
    else:
        print('\033[31m[%s]\033[0m Cannot create project')


```
