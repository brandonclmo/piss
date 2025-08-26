numbers_str = input()
numbers_list_str = numbers_str.split()

Ix = int(numbers_list_str[0]) #first
Cx = int(numbers_list_str[1]) # second
Id = int(numbers_list_str[2]) # third
Cd = int(numbers_list_str[3]) # fourth

x= Ix + Id 
x2 = Ix - Id 
y = Cx + Cd
y2 = Cx - Cd 

penis = [x, x2, y, y2]
dupe = set([n for n in penis if penis.count(n) > 1 and n >= 1 ])

if dupe:
    print((str(d) for d in dupe))
else:
    print("No answer.")



        

