import requests, sys
from prettytable import PrettyTable

def get_repos(api_url, user, token, username):
    headers = {"Private-Token": "%s" % token}
    login = requests.get(api_url + 'users/' + username + '/projects', headers=headers)

    c = 0

    table = PrettyTable(['Name', 'id', 'Stars', 'Link', 'Description']) # Header
    table.align = "l" # Text Align left

    data = login.json()

    if login.status_code == 200:
        for i in range(len(data)):

            if not data[i]["description"] == None:
                description = data[i]["description"]
                # Max characters for description
                if len(description) >= 80:
                    description = description[:80] + '...'
            else:
                description = None

            result = data[i]["web_url"].split('/')[-1], data[i]["id"], data[i]["star_count"], data[i]["web_url"], description
            table.add_row([result[0], result[1], result[2], result[3], result[4]])

            c+=1

        table.sortby = "Stars"
        table.reversesort = True
        print(table)

        print('\033[32mFound %i results\033[0m' % int(c))
    else:
        print('\033[31m[ERROR]\033[0m Cannot find any projects for this user')
