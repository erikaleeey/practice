class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        #start off with the head
        new_node = Node(value) #Node(value) runs the class constructor and returns a node object with value 
        if self.head is None:
            #empty linked list, just create a new node
            self.head = new_node 
        else:
            curr = self.head
            while(curr.next !=None):
                curr = self.next
            curr.next=new_node

    def prepend(self, value):
        #create a new node
        new_node = Node(value)
        if(self.head is None):
            self.head = new_node
        else:
            #set next to the head 
            new_node.next = self.head
            self.head = new_node

    def insert(self, index, value):
        new_node = Node(value)
        if(self.head is None):
            self.head = new_node
        else:
            curr = self.head
            counter = 0
            while(counter != index-1):
                curr = curr.next 
                counter +=1
            new_node.next = curr.next
            curr.next = new_node 

            
    def remove(self, value):
        # TODO: implement remove

    def find(self, value):
        # TODO: implement find

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
    ll.print_list()  # Expected: 5 -> 10 -> 20 -> None

    print("Find 10:", ll.find(10))  # Expected: True
    print("Find 99:", ll.find(99))  # Expected: False

#python3 ds_implement/linkedlist.py 