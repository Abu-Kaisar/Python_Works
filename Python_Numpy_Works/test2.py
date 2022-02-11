def dirReduc(arr):
    for i in arr:
        if i == "NORTH":
            if "SOUTH" in arr:
                del arr[arr.index("NORTH")]
                jst = arr.index("SOUTH")
                del arr[jst]
        
    for i in arr:
        if i == "EAST":
            if "WEST" in arr:
                del arr[arr.index("EAST")]
                jst = arr.index("WEST")
                del arr[jst]
            
    arr2 = []
    for i in arr:
        if i not in arr2:
            arr2.append(i)
    return arr2





a = ['NORTH', 'WEST', 'SOUTH', 'EAST']
print(dirReduc(a))