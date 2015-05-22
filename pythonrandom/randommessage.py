import random
import json
def get_message():
    list =["HAHA!","You will never do it!","Just stop it!","Its just a number how hard can it be?","Can you count untill 5?"]
    index=random.randint(0,len(list)-1)
    return list[index]

def get_winmessage():
    list=["You had luck this time","Begginers luck!","This was easy","First and last time!"]
    index=random.randint(0,len(list)-1)
    return list[index]

def get_record_list():
    f = open('recordstable.json', 'r')
    record = json.load(f)
    f.close()
    return record

def print_records(records):
    for name in records:
        print (name +": "+ str(records[name]))

def save_record(records,name,score):
    if name in records and records[name] >= score:
        return False

    records[name] = score
    f = open('recordstable.json', 'w')
    json.dump(records,f)
    f.close()
    return True