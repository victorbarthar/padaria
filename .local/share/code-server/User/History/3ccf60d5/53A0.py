value = input()
x = value.split()
maior = int(x[0]) 
maior2 = int(x[1])
maior3 = int(x[2])
if maior >= maior2 and  maior >= maior3:
    print(f"{maior} eh o maior")
    
elif maior2 >= maior and maior2 >= maior3:
    print(f"{maior2} eh o maior")
    
else:
    print(f"{maior3} eh o maior")