import json

data = json.load(open("data.json"))

def dict_search():
    search = input("Word to search for: ")
    for k,v in data.items():
        if search == k:
            print(v)

dict_search()