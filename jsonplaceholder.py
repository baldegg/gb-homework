import requests  # install with "pip install requests"
import json  # no installation needed - included with python 2.6+

todos_url = "https://jsonplaceholder.typicode.com/todos/"


"""Fetches newest 200 todos and presents them as JSON.  
Note: Because the ID given when we POST a new TODO is 201, it seems that the TODO list is chronological,
making 1-200 the OLDEST 200 TODOs.  However,  since we cannot actually add new TODOs beyond 200, 1-200 are also the 
newest 200 TODOs.  For simplicity's sake, I will use this  technicality to my advantage and assume that the JSON
returned contains the newest 200 TODOs :)"""
def get_newest_todos(url):
    todo200 = requests.get(url)
    return prettify(todo200.json())


"""POSTs a new TODO with specified title, body, and userId.  Returns reply from server including new TODO id."""
def post_new_todo(title, body, userId):

    # Tells server that our request will be in JSON format, using the UTF-8 charset, as per API documentation.
    headers = {
        "Content-type": "application/json; charset=UTF-8",
    }

    body = {
        "title": title,
        "body":  body,
        "userId": userId,
    }

    new_todo = requests.post(todos_url, json=body, headers=headers)
    return prettify(new_todo.json())


"""Deletes TODO of specified ID.  Returns appropriate message depending on whether TODO to be deleted was found."""
def delete_todo(id):
    delete_url = todos_url + str(id)
    deleted = requests.delete(delete_url)
    if deleted.status_code == 200:
        return "TODO " + str(id) + " Deleted."
    else:
        return "TODO " + str(id) + " not found."


"""Parses JSON returned from server into something legible from command line."""
def prettify(ugly_json):
    return json.dumps(ugly_json, indent=2)


# If run from command line, test each function and print results.
if __name__ == "__main__":
    print("Fetching latest 200 TODOs:")
    print(get_newest_todos(todos_url))
    print("Attempting to POST new TODO:")
    print(post_new_todo("hello", "world", 9000))
    print("Attempting to delete Todo #50 (exists) and #5000 (does not exist):")
    print(delete_todo(50))
    print(delete_todo(5000))

