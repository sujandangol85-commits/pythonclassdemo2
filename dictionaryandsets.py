#1. dictionary(Mutable)
# marks = {
#     "Sujan": 54,
#     "Lisa": 52,
#     "Rita": 76,
#     1: "Shyam"
# }

# print(marks, type(marks))
# print(marks["Sujan"]) #corresponding of Sujan

#methods of dictionary
# print(len(marks))
# print(marks.items()) #print all of the above(keys+values)
# print(marks.keys()) #print the keys (agadiko)
# print(marks.values()) #print the values (pxadiko)
# marks.update({"Sujan":100, "Sita":34}) #updating the values +addition
# print(marks.items())

# print(marks.get("Sujan6")) #diff between these 2 is that get return none if the name doesn't exist and
# print(marks["Sujan6"])  #it returns error if name doesn't exist if exists then both are same


# print(marks.clear()) #clears all item from dictionary
# print(marks.popitem()) #returns the last item of dictionary(LIFO)
# print(marks.pop("Lisa"))#Removes the specified key and returns its value Output: 52



#2. SETS(Non repititing values only)(unordered, unindexed)

# s=set() #empty set
# print(type(s))

# a={5,4,5,3,2,5,7,3,8} #5 ekchoti matra print hunxa
#methods of sets
# print(a)
# a.add(576)
# a.update([65,3,"sujan"])
# print(len(a))
# a.remove(5) #remove certain values from sets
# a.clear() #empties the set
# print(a.pop()) #removes random element from set and retrns the removed value
# print(a)

#Important one : UNION AND INTERSECTION

set1={3,4,5,2,54,"Sujan"}
set2={3,65,23,1,76,2}

# print(set1.union(set2)) #dubai ko value print tara no repeated ones
# print(set1.intersection(set2)) #dubai ko ma common vako values print
# print(set1.difference(set2)) #dubai ko ma common vako values print (set1 ma vako tara set 2 ma navako value return)

print({3, 4}.issubset(set1) )  # True
print(set1.issuperset({3,4}) )  # True



