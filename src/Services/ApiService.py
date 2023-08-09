from sys import stderr
import requests
import datetime

class ApiService:
    source_url = "https://jsonplaceholder.typicode.com/todos/"
    storage_folder = "storage"
    todos = {}

    def __init__(self):
        pass

    def get_todos(self, source_url):
        """
        Gets all TODOs from source_url

        :return: json
        """
        print('Todos request', file=stderr)
        response = requests.get(source_url)
        if response.status_code == 200:
            print('Request OK', file=stderr)
            return response.json()
        else:
            print('Request NOT OK', file=stderr)
            return None

    def todos_to_csv(self, todos, storage_folder):
        """
        Saves the TODOs to the storage folder with CSV format (one file per row)

        :param todos:
        :param storage_folder:
        :return:
        """
        for todo in todos:
            filename = f"{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}_{todo['id']}.csv"
            with open(f"{storage_folder}/{filename}", "w") as f:
                f.write("userId,id,title,completed\n")
                f.write(f"{todo['userId']},{todo['id']},{todo['title']},{todo['completed']}\n")

    def run(self):
        print('Running ApiService', file=stderr)
        # TODO: follow README.md instructions

        self.todos = self.get_todos(self.source_url)
        self.todos_to_csv(self.todos, self.storage_folder)

        print('Finished ApiService. CSV Files saved to storage folder.', file=stderr)