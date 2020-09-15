class Node:
    def __init__(self, data):
        self.data = data
        self.next_element = None


class LinkedList:
    def __init__(self):
        self.head_node = None

    def get_head(self):
        return self.head_node

    def is_empty(self):
        return True if self.head_node is None else False

    def insert_at_head(self, data):
        temp_node = Node(data)
        temp_node.next_element = self.head_node
        self.head_node = temp_node
        return self.head_node

    def print_list(self):
        if (self.is_empty()):
            print("list is empty")
            return False
        temp_node = self.head_node
        while self.head_node is not None:
            print(temp_node.data, end="->")
            temp_node = temp_node.next_element
        print(temp_node.data, "-> None")
        return True


singleLinkList = LinkedList()
singleLinkList.print_list()
print("Inserting Values in the list")
for i in range(1, 10):
    singleLinkList.insert_at_head(i)
singleLinkList.print_list()
