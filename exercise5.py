# THE Example one for Loop

for i in range(0, 10):
    print("Looping is ", i)

# THE Example two for Loop in list to show all item 
name =["hazem", "omar","abed", "Khamis"]

for item in name : 
    print(item,"serdah")

# The Example three for Loop in list to show all item 
count = 0 
while count < len(name):
    print(name[count])
    count+=1

# The Example Four for Loop in list to show all item 

for idx , item in enumerate(name): 
     print(idx,item)


# The Example Five for Loop in list to show all item 

favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    if dessert == 'Churros':
        print('Yes! One of my favorite desserts is', dessert)
        break 
        
    else:
    print('No sorry, not a dessert on my list')