# gutenburg api

import json,urllib.request
import random

def fetch_book_data(book_ID):
    try:
        url = "http://corpus-db.org/api/id/" + str(float(book_ID))
        #get data from corpus
        data = urllib.request.urlopen(url).read()
        #clean and convert data to json
        jsonified_data = json.loads(data)

        book_title = jsonified_data["title"]
        creator = jsonified_data["creator"]
        jsonified_data = creator.replace("'", "\"")
        creator_data = json.loads(jsonified_data)

        author_name = creator_data["author"]["agent_name"]

        return {"author": author_name, "title": book_title}
    except:

        return False

def fetch_random_book_data():
    found_book = False
    while not found_book:
        found_book = fetch_book_data(random.randrange(400, 800))

    return found_book

    