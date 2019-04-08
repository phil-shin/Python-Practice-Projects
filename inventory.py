# inventory.py
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory): #function to cleanly display inventory & total item count
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items(): #cycle through items in inventory
        print(str(v)+' '+k) #display number of item in inventory
        item_total+=v       #add number of items to total item count
    print("Total number of items: " + str(item_total))

displayInventory(stuff)
