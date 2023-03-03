import json
from operator import truediv
import sort
def check_Year(student1,student2):
    if (student1["year"] == student2["year"]):
        return True
    return False

def check_groupSize(group, room):
    for i in room["size"]:
        if(len(group["size"]) == i["size"]):
            return True, len(group["size"])
    return False

def idealSearch():
    rooms = []

    #if size/year matches, find all rooms possible,
    #then using preferences, remove all rooms in 
    #not wanted buildings, 
    return
def bestSearch(group,room):
    rooms = []
    gs = list(check_groupSize(group,room))
    if (gs[0] == True):
        for i in room["size"]:
            if(i["size"] == gs[1]):
                rooms.append(i)
    #how many ppl can live in the group
    #if size of group/year matches assign room to group and remove room as an option
    return rooms

if __name__ == "__main__":
    with open("test.json") as json_file:
        data = json.load(json_file)
    with open("1.json") as json_file:
        t1 = json.load(json_file)
    with open("2.json") as json_file:
        t2 = json.load(json_file)
    with open("group.json") as json_file:
        t3 = json.load(json_file)
    #sort.firstSearch(data, t1)
    with open("test.json", "w") as out:
        json.dump(data, out, indent=4)
    print (data)