import requests, sys
from prettytable import PrettyTable

def get_starred(api_url, user, token):
    headers = {"Private-Token": "%s" % token}
    login = requests.get(api_url + '/projects?starred=true', headers=headers)

    c = 0

    print('Your Starred projects\n')

    table = PrettyTable(['Name', 'Stars', 'Link', 'Description']) # Header
    table.align = "l" # Text Align left

    if login.status_code == 200:
        for repo in login.json():
            name = repo["web_url"].split('/')[-1]
            stars = repo["star_count"]

            if not repo["description"] == None:
                description = repo["description"]
                # Max characters for description
                if len(description) >= 80:
                    description = description[:80] + '...'
            else:
                description = None

            result = name, stars, repo["web_url"], description
            table.add_row([result[0], result[1], result[2], result[3]])

            c+=1

        table.sortby = "Stars"
        table.reversesort = True
        print(table)

        print('\033[32mFound %i results\033[0m' % int(c))

    else:
        print('\033[31m[ERROR]\033[0m Cannot find any repos for this user')
