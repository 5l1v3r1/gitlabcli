import requests
from prettytable import PrettyTable

def get_issues(api_url, user, token, id):
    headers = {"Private-Token": "%s" % token}
    login = requests.get(api_url + 'projects/' + id + '/issues', headers=headers)

    c = 0

    table = PrettyTable(['Updated at', 'Author', 'Title', 'State', 'Link']) # Header
    table.align = "l" # Text Align left

    data = login.json()

    for i in range(len(data)):
        # Grab data for each issue
        date = data[i]["updated_at"]
        author = data[i]["author"]["username"]
        title = data[i]["title"]
        state = data[i]["state"]
        url = data[i]["web_url"]

        # Max title length is 70 characters
        if len(title) >= 35:
            title = title[:35] + '...'

        result = date, author, title, state, url
        table.add_row([result[0], result[1], result[2], result[3], result[4]])

        c+=1

    print(table)
    print('\033[32mDisplaying %i issues\033[0m' % int(c))
