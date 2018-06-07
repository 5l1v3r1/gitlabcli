import requests
from prettytable import PrettyTable

def get_commits(api_url, token, id):
    headers = {"Authorization": "token %s" % token}
    login = requests.get(api_url + 'projects/' + id + '/repository/commits', headers=headers)

    data = login.json()

    table = PrettyTable(['Date', 'Author', 'Committer', 'Message']) # Header
    table.align = "l" # Text Align left

    for i in range(len(data)):
        date = data[i]["committed_date"].strip('Z')
        author = data[i]["author_name"]
        committer = data[i]["committer_name"]
        message = data[i]["title"]

        # Grab title only
        if "\n" in message:
            message = message.split('\n')[0]

        result = date, author, committer, message
        table.add_row([result[0], result[1], result[2], result[3]])

    # Print table
    print(table)
