import random 

history = {'Leo': ['Parham', 'Akhil', 'Zarine', 'Leo', 'Sri', 'David', 'Jeff', 'Ariana', 'Steven'],
 'Sri': ['Sophea', 'Steven', 'Kenneth', 'Leo', 'Sri', 'David', 'Jeff', 'Ariana', 'Sameer'],
 'David': ['Drew', 'Anika', 'Abi', 'Leo', 'Sri', 'David', 'Jeff', 'Ariana', 'Sara'],
 'Jeff': ['Jasmine', 'McAllister', 'Jeena', 'Leo', 'Sri', 'David', 'Jeff', 'Ariana', 'Parham'],
 'Ariana': ['Ani', 'Vedant', 'McAllister', 'Leo', 'Sri', 'David', 'Jeff', 'Ariana', 'Divya'],
 'Anika': ['David', 'Aiyush', 'Priya', 'Anika', 'Akhil', 'Meghan', 'Jasmine', 'Daniel', 'Ratan', 'Steven', 'Sophea'],
 'Akhil': ['Abi', 'Leo', 'Warren', 'Anika', 'Akhil', 'Meghan', 'Jasmine', 'Daniel', 'Ratan', 'Steven', 'Kelly'],
 'Meghan': ['McAllister', 'Isabelle', 'Ritik', 'Anika', 'Akhil', 'Meghan', 'Jasmine', 'Daniel', 'Ratan', 'Steven', 'Gracie','Duy'],
 'Jasmine': ['Jeff', 'Zarine', 'Jared', 'Anika', 'Akhil', 'Meghan', 'Jasmine', 'Daniel', 'Ratan', 'Steven', 'Priya'],
 'Daniel': ['Divya', 'Sophea', 'Vedant', 'Anika', 'Akhil', 'Meghan', 'Jasmine', 'Daniel', 'Ratan', 'Steven', 'Ritik'],
 'Ratan': ['Ritik', 'Bindu', 'Drew', 'Anika', 'Akhil', 'Meghan', 'Jasmine', 'Daniel', 'Ratan', 'Steven', 'Isabelle','Duy'],
 'Steven': ['Shreya', 'Sri', 'Ria', 'Anika', 'Akhil', 'Meghan', 'Jasmine', 'Daniel', 'Ratan', 'Steven', 'Leo'],
 'Ritik': ['Ratan', 'Sara', 'Meghan', 'Ritik', 'Priya', 'Isabelle', 'Warren', 'Vedant', 'Ria', 'Daniel','Duy'],
 'Priya': ['Sameer', 'Sara', 'Anika', 'Ritik', 'Priya', 'Isabelle', 'Warren', 'Vedant', 'Ria', 'Jasmine'],
 'Isabelle': ['Gracie', 'Meghan', 'Aiyush', 'Ritik', 'Priya', 'Isabelle', 'Warren', 'Vedant', 'Ria', 'Ratan', 'Drew','Duy'],
 'McAllister': ['Meghan', 'Jeff', 'Ariana', 'Zarine', 'Jeena', 'Shreya', 'Sophea', 'Aiyush', 'Parham','Sara','McAllister'],
 'Warren': ['Vedant', 'Abi', 'Akhil', 'Zarine', 'Ritik', 'Priya', 'Isabelle', 'Warren', 'Vedant', 'Ria', 'Chanan'],
 'Vedant': ['Zarine', 'Ani', 'Daniel', 'Warren', 'Ritik', 'Priya', 'Isabelle', 'Warren', 'Vedant', 'Ria', 'Jared'],
 'Ria': ['Sara', 'Duy', 'Steven', 'Ritik', 'Priya', 'Isabelle', 'Warren', 'Vedant', 'Ria', 'Kenneth'],
 'Zarine': ['Warren', 'Jasmine', 'Leo', 'Vedant', 'Zarine', 'Jeena', 'Shreya', 'Sophea', 'Aiyush', 'Parham', 'Abi','McAllister'],
 'Jeena': ['Jared', 'Jeff', 'Kelly', 'Zarine', 'Jeena', 'Shreya', 'Sophea', 'Aiyush', 'Parham', 'McAllister'],
 'Shreya': ['Steven', 'Drew', 'Sara', 'Zarine', 'Jeena', 'Shreya', 'Sophea', 'Aiyush', 'Parham', 'Bindu','McAllister'],
 'Sophea': ['Sri', 'Daniel', 'Jared', 'Zarine', 'Jeena', 'Shreya', 'Sophea', 'Aiyush', 'Parham', 'Anika','McAllister'],
 'Aiyush': ['Anika', 'Chanan', 'Isabelle', 'Zarine', 'Jeena', 'Shreya', 'Sophea', 'Aiyush', 'Parham', 'Ani','McAllister'],
 'Parham': ['Leo', 'Divya', 'Chanan', 'Zarine', 'Jeena', 'Shreya', 'Sophea', 'Aiyush', 'Parham', 'Jeff','McAllister'],
 'Sara': ['Ria', 'Ritik', 'Shreya', 'Sara', 'Sameer', 'Kenneth', 'Gracie', 'Bindu', 'Abi', 'David','McAllister'],
 'Sameer': ['Priya', 'Sara', 'Divya', 'Sara', 'Sameer', 'Kenneth', 'Gracie', 'Bindu', 'Abi', 'Sri'],
 'Kenneth': ['Kelly', 'Ariana', 'Sri', 'Sara', 'Sameer', 'Kenneth', 'Gracie', 'Bindu', 'Abi', 'Ria'],
 'Gracie': ['Isabelle', 'Kelly', 'Ani', 'Sara', 'Sameer', 'Kenneth', 'Gracie', 'Bindu', 'Abi', 'Meghan'],
 'Bindu': ['Chanan', 'Ratan', 'Inbar', 'Sara', 'Sameer', 'Kenneth', 'Gracie', 'Bindu', 'Abi', 'Shreya'],
 'Abi': ['Akhil', 'Warren', 'David', 'Sara', 'Sameer', 'Kenneth', 'Gracie', 'Bindu', 'Abi', 'Zarine'],
 'Ani': ['Ariana', 'Vedant', 'Gracie', 'Aiyush', 'Ani'],
 'Divya': ['Daniel', 'Parham', 'Sameer', 'Ariana', 'Divya'],
 'Kelly': ['Kenneth', 'Gracie', 'Jeena', 'Akhil', 'Kelly'],
 'Jared': ['Jeena', 'Jasmine', 'Sophea', 'Vedant', 'Jared'],
 'Drew': ['David', 'Shreya', 'Ratan', 'Isabelle', 'Drew','Duy'],
 'Chanan': ['Bindu', 'Aiyush', 'Parham', 'Warren', 'Chanan'],
 'Duy': ['Ria', 'Meghan', 'Ritik', 'Duy', 'Drew', 'Ratan', 'Isabelle']}



def add_groups_to_history(history, groups):
    for group in groups:
        for person in group:
            for chum in group:
                if chum not in history[person]:
                    history[person].append(chum)
    return history

def find_matches(history):
    match_set = {}
    groups = []
    options = history.keys()
    random.shuffle(options)
    while len(options) > 0:
        person = options[-1]
        inv_map = {v: k for k, v in match_set.items()}
        if person in inv_map:
            choice = inv_map[person]
            match_set[person] = choice
        else:
            choice = None
            while choice is None or choice == person or choice in history[person]:
                if len(options) == 1:
                    break
                if set(options).issubset(set(history[person])):
                    random_key = random.choice(match_set.keys())
                    random_value = match_set[random_key]
                    del match_set[random_key]
                    del match_set[random_value]
                    options.append(random_key)
                    options.append(random_value)
                choice = random.choice(options)
            if len(options) == 1:
                break
            match_set[person] = choice
            # print(options, person, choice)
            options.remove(person)
            options.remove(choice)
        # print(person, match_set[person])
    for person in match_set:
        group = set()
        group.add(person)
        group.add(match_set[person])
        groups.append(group)
    
    if len(options) == 1:
        print("a group of three!")
        groups[-1].add(options[0])
    else:
        print("no groups of three!")
    print(groups)
    history = add_groups_to_history(history, groups)
    print(history)
    
    
find_matches(history)
