def dirReduc(arr):
    N,S,E,W = arr.count("NORTH"),  arr.count("SOUTH"),  arr.count("EAST"),  arr.count("WEST")
    cx1 = N - S
    cx2 = E - W
    fln =[]
    
    
    
    if cx1 > 0:
        for i in range(cx1):
            fln.append("NORTH")
    elif cx1 < 0:
        for i in range(cx1*-1):
            fln.append("SOUTH")

    
    if cx2 > 0:
        for i in range(cx2):
            fln.append("EAST")
    elif cx2 < 0:
        for i in range(cx2*-1):
            fln.append("WEST")
        else:
            pass
        
    
    return fln



a = ['NORTH', 'WEST', 'SOUTH', 'EAST']
print(dirReduc(a))

        