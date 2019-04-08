# addtoinventory.py
#create function to add a list of items (loot) to existing inventory

def addToInventory(inventory, addedItems):
    for item in dragonLoot:
        inventory.setdefault(item, 0)
        inventory[item]+=1
    return inventory
    
# inventory.py

def displayInventory(inventory): #function to cleanly display inventory & total item count
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items(): #cycle through items in inventory
        print(str(v)+' '+k) #display number of item in inventory
        item_total+=v       #add number of items to total item count
    print("Total number of items: " + str(item_total))

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
