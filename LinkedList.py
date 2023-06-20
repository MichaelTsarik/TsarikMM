class Node:
    def __init__(self, data=None):
        self.data = data
        self.next_node = None
        self.prev_node = None


class LinkedList:
    def __init__(self):
        self.node = None

    def add_to_end(self, new_data):
        new_node = Node(new_data)
        if self.node is None:
            self.node = new_node
            return
        after_node = self.node

        while after_node.next_node:
            after_node = after_node.next_node
        after_node.next_node = new_node
        new_node.prev_node = after_node
        self.node = new_node

    def add_to_start(self, new_data):
        new_node = Node(new_data)
        if self.node is None:
            self.node = new_node
            return
        before_node = self.node

        while before_node.prev_node:
            before_node = before_node.prev_node
        before_node.prev_node = new_node
        new_node.next_node = before_node
        self.node = new_node

    def go_to_start(self):
        current_node = self.node

        while current_node.prev_node:
            current_node = current_node.prev_node
        self.node = current_node

    def print_info(self):
        self.go_to_start()
        after_node = self.node
        print(after_node.data, end=', ')

        while after_node.next_node:
            after_node = after_node.next_node
            print(after_node.data, end=', ')


test_linked_list = LinkedList()

test_linked_list.add_to_start(500)
test_linked_list.add_to_end(100)
test_linked_list.add_to_end(300)
test_linked_list.add_to_end(400)
test_linked_list.add_to_start(1000)

test_linked_list.print_info()
