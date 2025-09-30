class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0


    def append(self, value):
        #start off with the head
        new_node = Node(value) #Node(value) runs the class constructor and returns a node object with value 
        if self.head is None:
            #empty linked list, just create a new node
            self.head = new_node 
            self.length += 1
        
        elif(self.head.next is None):
            #one node list
            self.head.next = new_node
            self.length +=1
            
        else:
            curr = self.head
            
            while(curr.next !=None):
                curr = curr.next
            curr.next=new_node
            self.length += 1

    def prepend(self, value):
        #create a new node
        new_node = Node(value)
        if(self.head is None):
            self.head = new_node
            self.length +=1
        else:
            #set next to the head 
            new_node.next = self.head
            self.head = new_node
            self.length += 1

    def insert(self, index, value):
        if(index<0):
            raise IndexError("Negative index")
        if(index > self.length):
            raise IndexError("Out of bounds")
        
        #create new node
        new_node = Node(value)
        #if list empty
        if(self.head is None):
            self.head = new_node
            self.length += 1
        #non empty list
        else:
            curr = self.head
            counter = 0
            while(counter != index-1):
                curr = curr.next 
                counter +=1
            new_node.next = curr.next
            curr.next = new_node 
            self.length +=1

            
    def remove(self, value):
        curr = self.head
        #empty list
        if(self.head ==None):
            return
        #removing head
        if(curr.value == value):
            self.head = curr.next
            self.length -= 1
        #removing non head

        while(curr.next != None):
            if curr.next.value == value:
                curr.next = curr.next.next
                self.length -=1
                return

            else:
                curr = curr.next 
                


    def find(self, value):
        curr = self.head

        #empty list
        if (self.head == None):
            return False
        
        #one node list
        if(curr.next == None):
            if(curr.value == value):
                return True
            else: return False

        #non empty more than one node list
        while(curr.next != None):
            print("while loop")
            if(curr.value == value):
                return True 
            else:
                curr = curr.next
        return False

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")


# ---------- TEST ----------
if __name__ == "__main__":

    
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.prepend(5)
    ll.insert(1, 15)
    ll.print_list()  # Expected: 5 -> 15 -> 10 -> 20 -> None

    ll.remove(15)
    ll.remove(5)
    ll.remove(10)
    ll.remove(20)
    ll.print_list()  # Expected: 5 -> 10 -> 20 -> None

    ll.insert(0,10)
    print(ll.find(10))
    ll.print_list()

    print("Find 10:", ll.find(10))  # Expected: True
    print("Find 99:", ll.find(99))  # Expected: False
    

#python3 ds_implement/linkedlist.py 