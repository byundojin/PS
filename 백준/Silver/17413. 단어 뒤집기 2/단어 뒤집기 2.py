s = input()

def print_temp(temp):    
    print(*(i[::-1] for i in temp.split()), end="")

temp = ""
angle = False
for i in s:
    if i == "<":
        print_temp(temp)
        temp = ""
        angle = True
    temp = f"{temp}{i}"
    if i == ">":
        print(temp, end="")
        temp = ""
        angle = False

print_temp(temp)