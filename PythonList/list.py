list=[1,2,4,3]

#add specific index 
list.insert(1,34)

#append 
for i in range(1,11):
  list.append(i)
list.append('Harun')
print(f'List = {list}')


# add more value in list 
list.extend([4,3,2,5])
print(f"After extend ={list}")

#remove a value from list 
list.remove(34)
print(f"After remove = {list}")

#remove specific index
list.pop(2)
print(f"After pop list ={list}")

#use slice 
print(f" use slice list={list[1:3]}")
print(f" use slice list={list[3:]}")  #after 3 to end 


#reverse 
list2=[34,53,"Mizan", "Elma", "Arif"]
print(f"does not Modify list ={list2[::-1]}")  # does not modify list
list2.reverse()
print(f"Modify list={list2}")
