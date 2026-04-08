#kalena jay & sujalkumar(jerry)
#7/4/2026
#function of tuple

a=("apple","banana","mango","chiku","papaya")
print(a)

print(len(a))

print(type(a))

b = tuple((1,2,3,4,5,6))
print(b)

print(a[3])

print(max(a))

print(min(a))

print(a[-1])

print(a[2:4])

print(a[:2])

print(a[2:])

print(a[-4:-1])

#tuple ma value badlva mate
y = list(a)
y.append("kiwi")
a = tuple(y)
print(a)

y = list(a)
y[3] = "cucumber"
a = tuple(y)
print(a)

y = list(a)
y.remove("kiwi")
a = tuple(y)
print(a)

y = list(a)
y.insert(0, "Jerry")
a = tuple(y)
print(a)