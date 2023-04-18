lst = [1,5,10,20,33]
sv = 5
upB = len(lst)-1
lowB = 0
mid = 0
Found = False
while not Found:
    mid = (upB+lowB)//2
    if lst[mid]==sv:
        Found = True
        print("The Item Is At Index",mid)
    elif mid>sv:
        
        
