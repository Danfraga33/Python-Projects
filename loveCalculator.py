print('the love calculator')
name1 = input("First Name?")
name2 = input('Second Name?')

combined_names = name1 + name2
lower_names = combined_names.lower()

t = lower_names.count('t')
r = lower_names.count('r')
u = lower_names.count('u')
e = lower_names.count('e')

l = lower_names.count('l')
o = lower_names.count('o')
v = lower_names.count('v')
e = lower_names.count('e')

firstDigits = t + r + u + e
secondDigits = l + o + v + e

score = int(str(firstDigits) + str(secondDigits))
print(f'Your love score is {score}')
