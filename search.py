import json
from difflib import get_close_matches

data = json.load(open("data.json"))

word = input("Word to search for: ")

def dict_search(word):
    if word.capitalize() in data:
        return data[word.capitalize()]
    else:
        word = word.lower()
        if word in data:
            return data[word]
        elif len(get_close_matches(word, data.keys())) > 0:
            run = input("Did you mean %s? " % get_close_matches(word, data.keys())[0])
            if run.lower() == 'y':
                return data[get_close_matches(word, data.keys())[0]]
            elif run.lower() == 'n':
                return "Word doesn't exist within dictionary."
            else:
                return "Entry not understood."
        else:
            return "Word doesn't exist within dictionary."

output = dict_search(word)

if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)