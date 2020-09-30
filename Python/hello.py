print("Hello, World!")

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist) #print all the list
print(thislist[1])  #print the second item, item start with 0
print(thislist[-1]) #print the last item, 1st item from the back
print(thislist[2:5]) #print 3rd to 6th items
print(thislist[2:]) #print 3rd to last items
thislist[2]="blackcurrant" #change or set 3rd items to new value
print(thislist)
thislist.append("rambutan") #add new item to the list after the last item
thislist.insert(1,"papaya") #add new item after the 2nd item
print(thislist)
print(len(thislist)) #print the length of the list
if "banana" in thislist:    #check if banana in the list
 print("Yes, 'banana' is in the fruits list")
list2 = ["mangosteen", "durian", "watermelon"]
list3 = thislist + list2    #append 2nd list to the 1st list and assign to new list
print(list3)

thistuple = ("apple", "banana", "cherry")
print(thistuple)
print(thistuple[1])
print(thistuple[2:5])
if "apple" in thistuple:
 print("Yes, 'apple' is in the fruits tuple")
print(len(thistuple))


thisset = {"apple", "banana", "cherry"} 
print(thisset)
thisset.add("orange") # add new item
print(thisset)
thisset.update(["orange", "mango", "grapes"]) # add more items to the whole set
print(thisset)
print(len(thisset)) # print the length of set
thisset.remove("mango") # remove an item
print(thisset)
set1 = {"a", "b" , "c"}
set2 = thisset.union(set1) #join 2 sets
print(set2)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
x = thisdict["model"] # can also be written as thisdict.get("model")
print(x)
thisdict["year"] = 2018 #update item value
print(thisdict)
for x, y in thisdict.items(): #looping through the dictionary
  print(x, y)
print(len(thisdict))
thisdict["color"] = "red" #add new item
print(thisdict)

a = 100
b = 23
c = 250
d = 100
if a > b:
 print("a is greater than b")

if a == d:
 print("a and d are equal")

if a > b and c > a:
  print("Both conditions are True")


if a < b:
 print("a is less than b")
elif a > b:
 print("a and d are equal")
else:
  print("a is greater than b")
  

