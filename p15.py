#24/march/26
#sujalkumar kalena
#python list function

a = [5, 4, 3, 2, 1]
b = [1, 2, 3]
c = [1, 1, 1, 2]

#1-use append to add the element 10 to the end of list-append
a.append(10)
print(a)


#2-clear all element from list b-clear
b.clear()
print(b)


#3-returns the number of times a specified element appears in the list.-count
d = c.count(1)
print(d)	


#4-adds elements from another list to the end of the current list.-extend()
a.extend(b)
print(a)

#5-sorts the list in exsesting order-sort()
a.sort()
print(a)


#6-reverses the order of the elements in the list.-reverse()
a.reverse()
print(a)


#7-this method removes and returns an element from a list-pop()
a.pop()
print(a)

#8-this method inserts an item at specific index in a list-insert()
a.insert(0, 2)
print(a)

#9-this method is a helpful tool when we want to find the psition of a specific item in a list.-index
k = a.index(2)
print(k)

#10-this function removes the first occurence of a given itemfrom list.-remove()
a.remove(2)
print(a)


print(min(a))
print(max(a))
print(len(a))
print(sum(a))
print(a[2])
