# Python App Exercise

## Exercise
- Use the ApiService to fetch TODOs from an API and save them into the _storage_ folder
    - TODOs can be accessed from this URL: https://jsonplaceholder.typicode.com/todos/
    - Each TODO should be saved on a single file in CSV format
    - The filename must contain the TODO "id" prefixed with the current date.
        - Example: 2021_04_28_123.csv


## Extra points
- Use _requests_ library from [PyPI](https://pypi.org/project/requests/)


# Angel Navas - Solution proposal

## Rationale 
In this example the above rules have been followed, creating multiple csv files from individual "alls" present in the REST request response.
Being an exercise, the use of an API service has been simplified, integrating all its functions within ApiService.
In a real case, the separation of functionalities, and given that these services can evolve, a greater separation should be chosen, with the part of creating files in App.py and leaving ApiService only for the download of the REST request.



## Possible improvements
- Add user id to file name for better identification.
- Load the received data to a database, for a better performance in intensive use of resources.
- Better handling of errors in case the folder does not exist or the data received is not correct or does not exist.
-Create unit tests to detect possible failures automatically.