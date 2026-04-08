#functin of set
#kalena sujalkumar(jerry) & jay
#07/04/2026

x = set(("Sujal", "Jay", "Jerry", "Meet", "Gopal"))
print(x)

print(type(x))

x.add("jalambhai")
print(x)

x.remove("Jay")
print(x)

x.pop()
print(x)

x.discard("Meet")
print(x)

y = (("Jay", "Rajveer", "Rakshaan"))
x.update(y)
print(x)

print(len(x))

print(max(x))

print(min(x))

print(sorted(x))

print(all(x))


s = {2, 4, 7}
a = {4, 7, 2}

print(s >= a)