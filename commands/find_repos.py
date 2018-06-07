import requests, sys
from prettytable import PrettyTable

def find_repos(api_url, user, token, string):
    headers = {"Private-Token": "%s" % token}
    login = requests.get(api_url + 'search?scope=projects&search=' + string, headers=headers)

    c = 0

    data = login.json()

    table = PrettyTable(['Url', 'id', 'Stars', 'Description']) # Header
    table.align = "l" # Text Align left

    for i in range(len(data)):

        if not data[i]["description"] == None:
            description = data[i]["description"]
            # Max characters for description
            if len(description) >= 99:
                description = description[:99] + '...'
        else:
            description = None

        result = data[i]["web_url"], data[i]["id"], data[i]["star_count"], description
        table.add_row([result[0], result[1], result[2], result[3]])

        #print('%s %s ' % (result["items"][i]["html_url"].ljust(50), description))
        c+=1

    table.sortby = "Stars"
    table.reversesort = True
    print(table)

    print('\033[32m\nDisplaying %i out of %i results\033[0m' % (int(c), len(data)))
