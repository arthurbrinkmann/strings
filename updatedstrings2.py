number = input("Please enter a series of numbers, using any separators you like")
separtors = ""

for char in number:
    if not char.isnumeric():
        separtors = separtors + char

#print(separtors)

#Below is very advanced code
#Built in features example below
values="".join(char if char not in separtors else " " for char in number).split()
print(sum([int(val) for val in values]))