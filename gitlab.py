#!/usr/bin/python3
# Link to docs:
# requests: http://docs.python-requests.org/en/master/user/quickstart/
# API:      https://docs.gitlab.com/ee/api/
import requests, os, sys, time, getpass, readline, hashlib
from auth import user, token

# Import commands
from commands.get_repos import *
from commands.get_starred import *
from commands.search_user import *
from commands.clone import *
from commands.clone_all import *
from commands.delete_repo import *
from commands.create_repo import *
from commands.edit_repo import *
from commands.find_repos import *
from commands.profile import *
from commands.delete_all import *
from commands.follow import *
from commands.block import *
from commands.get_issues import *
from commands.get_commits import *
from commands.star import *
from commands.get_files import *
from commands.emails import *
from commands.create_user import *

api_url = 'https://www.gitlab.com/api/v4/'

error = '\033[31m[ERROR]\033[0m Invalid username or password'

banner = '''\033[37m

888       888          888                                              888
888   o   888          888                                              888
888  d8b  888          888                                              888
888 d888b 888  .d88b.  888  .d8888b .d88b.  88888b.d88b.   .d88b.       888888 .d88b.
888d88888b888 d8P  Y8b 888 d88P"   d88""88b 888 "888 "88b d8P  Y8b      888   d88""88b
88888P Y88888 88888888 888 888     888  888 888  888  888 88888888      888   888  888
8888P   Y8888 Y8b.     888 Y88b.   Y88..88P 888  888  888 Y8b.          Y88b. Y88..88P
888P     Y888  "Y8888  888  "Y8888P "Y88P"  888  888  888  "Y8888        "Y888 "Y88P"



 .d8888b.  d8b 888    888               888                  d8888 8888888b. 8888888
d88P  Y88b Y8P 888    888               888                 d88888 888   Y88b  888
888    888     888    888               888                d88P888 888    888  888
888        888 888888 888       8888b.  88888b.           d88P 888 888   d88P  888
888  88888 888 888    888          "88b 888 "88b         d88P  888 8888888P"   888
888    888 888 888    888      .d888888 888  888        d88P   888 888         888
Y88b  d88P 888 Y88b.  888      888  888 888 d88P       d8888888888 888         888
 "Y8888P88 888  "Y888 88888888 "Y888888 88888P"       d88P     888 888       8888888
\033[0m'''

info = '''
\033[37mCommands:\033[0m
    \033[37mGlobal:\033[0m
    clone <url>                       | Clone a project
    clone all <username>              | Clone all user projects
    clear                             | Clear terminal screen
    exit/quit                         | Exit the console

    \033[37mUsers:\033[0m
    get repos <username>              | Get all users projects
    get starred                       | Get all your starred projects
    get issues <project_id>           | Show issues for this project
    get commits <project_id>          | Show all commits for this project
    get files <project_id>            | List files in this project
    search <user>                     | Search for a user
    find <string>                     | Search for projects by string
    blocks                            | List blocked users
    star/unstar <project_id>          | Star or unstar a users project

    \033[37mYour account:\033[0m
    profile                           | Show your profile
    delete <project_id>               | Delete a project
    create <project_name>             | Create a project
    edit <project_id>/<item>/<string> | Valid Items: name, description, homepage, visibility
    donothitenternow                  | Do Not Hit Enter Now -> DELETES ALL YOUR PROJECTS !!

    \033[37mSudo:\033[0m
    add email <user_id> <email>                       | Add a email account for this user
    block/unblock <user_id>                           | Block/unblock this user
    create_user <email> <password> <username> <name>  | Create a new user
    delete_user <user_id>                             | Delete a user
'''

def menu():
    try:

        # Start Menu
        while True:
            opt = input('[gitlab] > ')

            # Menu commands
            if opt == '?' or opt == 'help':
                print(info)
            elif opt == 'exit' or opt == 'quit':
                sys.exit(0)
            elif opt == 'clear':
                os.system('clear')
            elif opt.startswith('search '):
                username = opt.split(' ')[1]
                search_user(api_url, user, token, username)
            elif opt.startswith('get repos '):
                username = opt.split(' ')[2]
                get_repos(api_url, user, token, username)
            elif opt.startswith('get starred'):
                get_starred(api_url, user, token)
            elif opt.startswith('clone all '):
                username = opt.split(' ')[-1]
                clone_all(api_url, user, token, username)
            elif opt.startswith('clone '):
                url = opt.split(' ')[1]
                clone(url)
            elif opt.startswith('delete '):
                id = opt.split(' ')[1]
                delete_repo(api_url, user, token, id)
            elif opt.startswith('create issue '):
                username = opt.split(' ')[2]
                repo = opt.split(' ')[3]
                create_issue(api_url, user, token, username, repo)
            elif opt.startswith('create '):
                repo = opt.split(' ')[1]
                create_repo(api_url, user, token, repo)
            elif opt.startswith('edit '):
                id = opt.split('/')[0][5:]
                item = opt.split('/')[1]
                value = opt.split('/')[2]
                edit_repo(api_url, user, token, item, value, id)
            elif opt.startswith('get followers '):
                username = opt.split(' ')[-1]
                get_followers(api_url, user, token, username)
            elif opt.startswith('get following '):
                username = opt.split(' ')[-1]
                get_following(api_url, user, token, username)
            elif opt.startswith('find '):
                string = opt.replace('find ', '')
                string = string.replace(' ', '+')
                find_repos(api_url, user, token, string)
            elif opt.startswith('profile'):
                profile(api_url, user, token)
            elif opt == 'donothitenternow':
                delete_all(api_url, user, token)
            elif opt.startswith('follow '):
                username = opt.split(' ')[1]
                follow(api_url, user, token, username)
            elif opt.startswith('unfollow '):
                username = opt.split(' ')[1]
                unfollow(api_url, user, token, username)
            elif opt.startswith('block '):
                user_id = opt.split(' ')[1]
                block(api_url, user, token, user_id)
            elif opt.startswith('unblock '):
                user_id = opt.split(' ')[1]
                unblock(api_url, user, token, user_id)
            elif opt == 'blocks':
                blocks(api_url, user, token)
            elif opt.startswith('get issues '):
                id = opt.split(' ')[2]
                get_issues(api_url, user, token, id)
            elif opt.startswith('get commits '):
                id = opt.split(' ')[2]
                get_commits(api_url, token, id)
            elif opt.startswith('star '):
                id = opt.split(' ')[1]
                star(api_url, user, token, id)
            elif opt.startswith('unstar '):
                id = opt.split(' ')[1]
                unstar(api_url, user, token, id)
            elif opt.startswith('get files '):
                id = opt.split(' ')[2]
                get_files(api_url, user, token, id)
            elif opt.startswith('add email '):
                user_id = opt.split(' ')[2]
                email = opt.split(' ')[3]
                add_email(api_url, user, token, user_id, email)
            elif opt.startswith('create_user '):
                email = opt.split(' ')[1]
                password = opt.split(' ')[2]
                username = opt.split(' ')[3]
                name = opt.split(' ')[4]
                create_user(api_url, user, token, email, password, username, name)
            elif opt.startswith('delete_user '):
                user_id = opt.split(' ')[1]
                delete_user(api_url, user, token, user_id)
            else:
                print('\033[31m[ERROR]\033[0m Invalid option')
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        print('\033[31m[ERROR]\033[0m %s' % e)
        return menu()

# Login script start here

try:

    if user == '' and token == '':
        print('''
        Please login with your credentials below.
        Put your username and token in auth.py for static values

        Generate a token here: https://gitlab.com/profile/personal_access_tokens

        Please note that for some commands you'll need special permissions.

        ''')

        user = input('Username: ')
        token = getpass.getpass('Token: ')
    else:
        pass

except KeyboardInterrupt:
    print('\n'); sys.exit(0)

headers = {"Private-Token": "%s" % token}
testlogin = requests.get("https://www.gitlab.com/api/v4/user", headers=headers)

if testlogin.status_code == 200:
    print('Login \033[32m[OK]\033[0m')

    print(banner)
    profile(api_url, user, token)

    menu()
else:
    print(error); sys.exit(1)
