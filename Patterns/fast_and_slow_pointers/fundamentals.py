fast = head 
slow = head 



#Conditioning on fast
while fast and fast.next:
    pass

'''
Largely driven by length

- For Singly Linked List
Even numbered node length -> is odd due to presence of None
    Fast lands on None
Odd numbered node length -> is even due to presence of None
    Fast lands on the last element
'''