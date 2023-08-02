
"""line = '*'
max_length = 6
space = 6
while len(line) <= max_length*2:
    print(" " * space + line + " " * space)
    line += "**"
    space -= 1
space = 0
while len(line) > 0:
    print(" " * space + line + " " * space)
    line = line[:-2]
    space+= 1
"""
"""
name = "Shuayb"
age = 20
HasAndriodPhone = False
person = {"name":"Shuayb", "age" : 20, "HasAndriodPhone" :False}

print("{} is aged {}, and owns an {}.".format(
    person["name"],
    person["age"],
    "Andriod Phone" if person["HasAndriodPhone"] else "iPhone"
))

for key,value in person.items():
    print("The key {} has the value {} of the type {} ".format(key,person[key],type(value)))
"""

