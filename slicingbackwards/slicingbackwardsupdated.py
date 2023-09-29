letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[25:0:-1] #could use [::-1] as well 
print(backwards)

# create a slice that produces the characters qpo
print(letters[16:13:-1])

#slice the string to produce edcba

print(letters[4::-1])
#slice the string to producte the last 8 characters, in reverse order
print(letters[:-9:-1])

print(letters[-4:]) #wxyz
print(letters[-1:]) #z
print(letters[:1]) #a
print(letters[0]) #a