print("---------------------------list---------------------------------")
#List operations

#creating a list
Umesh=[7,0,5,4,5,6,9,7,8]
print("created list is",Umesh)

#Adding
Umesh.append(2)
print("after adding" ,Umesh)

#removing a element
Umesh.remove(0)
print(Umesh)

#clear all elements
Umesh.clear()
print(Umesh)

#join list
list1 = ["Umesh", "Aryan"]
list2 = ["Raj", "Rahul"]
list3 = list1 + list2
print("joined list is ",list3)

#-------------------------------------------------------------------
print("-----------------------------------------DICTIONARY-------------")
#dictionary operations

#creating a dictionary
Umesh= {1: 'engish', 2: 'hindi', 3: 'maths',4:'computer science'} 
print(Umesh)

#Adding
Umesh[5] = 'Sanskrit'
Umesh[6] = 'Science'
print(Umesh)

#to get Value
print(Umesh.get(3))

#removing a element
Umesh.pop(1)
print(Umesh)

#length
print(len(Umesh))

#-----------------------------------------------------------------
print("--------------------------------TUPLE-----------------------------------------")
#creating a tuple
Aryan= ("apple", "banana", "cherry")
print(Aryan)

#lenght
print("Length of tuple is")
print(len(Aryan))

#-----------------------------------------------------------------
print("--------------------------set--------------------------------------------------")
#creating a set
Raj= {"Umesh", "Aryan", "Raj", "Rahul"}
print(Raj)





