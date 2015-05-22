import random
def get_message():
    list =["HAHA!","You will never do it!","Just stop it!","Its just a number how hard can it be?","Can you count untill 5?"]
    index=random.randint(0,len(list)-1)
    return list[index]

def get_winmessage():
    list=["You had luck this time","Begginers luck!","This was easy","First and last time!"]
    index=random.randint(0,len(list)-1)
    return list[index]