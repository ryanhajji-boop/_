
class Node:
    def __init__(self, data, next_node):
        self._data = data
        self._next_node = next_node

    def set_next(self, node):
        self._next_node = node

    def get_next(self):
        return self._next_node

    def get_data(self):
        return self._data

class LinkedList:
    """
    A stack using a singly linked list to create a stack.
    """
    def __init__(self):
        self._head_node = None
        self._size = 0

    def __len__(self):
        """ Allows the use of len(stack) to find the number of elements in the stack """
        
        return self._size

    def push(self, data):
        new_node = Node(data, self._head_node)
        self._head_node = new_node
        self._size += 1


    def pop(self):
        if self.is_empty():
            print("cannot pop from an empty stack")
            return None
        data = self._head_node.get_data()
        self._head_node = self._head_node.get_next()
        self._size = self._size - 1

        return data
        

    def peek(self):
        return self._head_node
    
    def is_empty(self):
        return self._size == 0
    
    def __str__(self):
        current_node = self._head_node
        string = ''
        while current_node != None:
            string += str(current_node.get_data()) + " -> "
            current_node = current_node.get_next()
        string += "None: That's the end of the linked list!"
        return string

if __name__ == "__main__":
    my_stack = LinkedList()

    my_stack.push(34)
    my_stack.push(33)
    my_stack.push(33)

    # my_stack.append(4)

    print(f"{my_stack}. The length is also {len(my_stack)}")

    # while not my_stack.is_empty():
    #     print(my_stack.pop())

