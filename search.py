import json
from difflib import get_close_matches

data = json.load(open("data.json"))

word = input("Word to search for: ")

def dict_search(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.upper() in data:
        return data[word.upper()]
    elif word.title() in data:  # if user entered "texas" this will check for "Texas" as well.
        return data[word.title()]
    elif len(get_close_matches(word, data.keys())) > 0:
        run = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0])
        if run.lower() == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif run.lower() == "n":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

output = dict_search(word)

if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)