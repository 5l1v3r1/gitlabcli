import requests, sys
from prettytable import PrettyTable

def search_user(api_url, user, token, username):
    headers = {"Private-Token": "%s" % token}
    login = requests.get(api_url + 'users?search=' + username, headers=headers)

    data = login.json()

    c = 0

    table = PrettyTable(['Username', 'Name', 'id', 'Profile', 'Projects', 'State']) # Header
    table.align = "l" # Text Align left

    if login.status_code == 200:
        # Get Data
        for i in range(len(data)):
            username = data[i]["username"]
            name = data[i]["name"]
            id = data[i]["id"]
            url = data[i]["web_url"]
            state = data[i]["state"]

            headers = {"Private-Token": "%s" % token}
            get_projects = requests.get(api_url + 'users/' + username + '/projects', headers=headers)
            data2 = get_projects.json()

            projects = len(data2) # Count projects

            result = username, name, id, url, int(projects), state
            table.add_row([result[0], result[1], result[2], result[3], result[4], result[5]])

            c+=1

        print(table)
        print('\033[32m\nDisplaying %i out of %i results\033[0m' % (int(c), len(data)))

    else:
        print('\033[31m[ERROR]\033[0m User does not exist')
