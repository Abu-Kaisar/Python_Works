open_list = ["NORTH","EAST"]
close_list = ["SOUTH","WEST"]

def dirReduc(arr):
    NF,SF,EF,WF = [],[],[],[]
    prr = arr[:]
    for o in prr:
        if o == "NORTH":
            NF.append(arr.index("NORTH"))
            del prr[i]
        elif o == "SOUTH":
            SF.append(arr.index("SOUTH"))  
        elif o == "EAST":
            EF.append(arr.index("EAST"))  
        elif o == "WEST":
            WF.append(arr.index("WEST"))  
            
    print(NF,SF,EF,WF)



a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
print(dirReduc(a))