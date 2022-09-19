
x = []

for i in range(1 , 11):
    name = input("please enter 10 names:")
    name = name.lower()
    name = name.title()
    x.append(name)

    for new_name in x:
        print(new_name)
