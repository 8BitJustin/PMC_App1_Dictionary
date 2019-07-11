import json

data = json.load(open("data.json"))

def dict_search():
    search = input("Word to search for: ")
    search = search.lower()
    if search in data:
        return data[search]
    else:
        return "Word doesn't exist within dictionary."

print(dict_search())