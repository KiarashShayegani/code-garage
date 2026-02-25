# Just a simple example of using list comprehension here brosky..
response = {
    "data": [
        {"id": 1, "status": "ok"},
        {"id": 2, "status": "error"},
        {"id": 3, "status": "ok"}
    ]
}

def logChecker(response):
    print('Successfull connections:')
    [print(((str(log['id']) + ' --> ' + log['status'])), end =' | ') for log in response["data"] if log['status'] == 'ok' ]
    print('\nFailed connections:')
    [print((str(log['id']) + ' --> ' + log['status']), end= ' | ') for log in response["data"] if log['status'] == 'error' ]

print('======= Logger =======\n')
logChecker(response)
