import sys

with open(sys.argv[1], "r", encoding="utf-8") as file:
    l = file.readlines()    
    d = {}
    names = sys.argv[2].split(",")
    for i in l:
        i = i.split(":")
        d[i[0]]= i[1]
    for j in names:
        try:
            print("Name: {}, University: {}".format(j,d[j]), end="")   
        except: 
            print("No record of '{}' was found".format(j))

