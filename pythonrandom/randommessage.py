import random
import json
from  os.path import isfile

filerecord = "recordstable.json"


def get_message():
    list = ["HAHA!", "You will never do it!", "Just stop it!", "Its just a number how hard can it be?",
            "Can you count untill 5?"]
    index = random.randint(0, len(list) - 1)
    return list[index]


def get_winmessage():
    list = ["You had luck this time", "Begginers luck!", "This was easy", "First and last time!"]
    index = random.randint(0, len(list) - 1)
    return list[index]


def get_record_list():
    if isfile(filerecord):
        f = open(filerecord, 'r')
        record = json.load(f)
        f.close()
        return record
    else:
        return {}


def print_records(records):
    for name in records:
        print(name + ": " + str(records[name]))


def get_champion(records):
    champion = ""
    result = 0
    for name in records:
        if result < records[name]:
            result = records[name]
            champion = name

    return {
        "name": champion,
        "score" : result
    }


def save_record(records, name, score):
    if name in records and records[name] >= score:
        return False

    records[name] = score
    f = open(filerecord, 'w')
    json.dump(records, f)
    f.close()
    return True
