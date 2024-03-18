import random


class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

    def __str__(self):
        return f'Data = {self.data} next Node = {self.next_node}'


class LinkedList:
    def __init__(self, head_node=None):
        self.head = head_node
        
    def __iter__(self):
        return self.Iterator(self.head)
    
    def __str__(self):
        outp_string = ''
        currend_node = self.head
        i = 0
        while currend_node.next_node:
            outp_string += f'{i}: {currend_node.data}\n'
            i += 1
            currend_node = currend_node.next_node
        outp_string += f'{i}: {currend_node.data}'

        return outp_string

    def __len__(self):
        if self.head is None:
            return 0

        length = 1
        currend_node = self.head
        while currend_node.next_node:
            length += 1
            currend_node = currend_node.next_node

        return length

    def insert(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        else:
            node.next_node = self.head
            self.head = node

    def insert_ending(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return

        currend_node = self.head
        while currend_node.next_node:
            currend_node = currend_node.next_node

        currend_node.next_node = node


    class Iterator:
        def __init__(self, currend_node):
            self.currend_node = currend_node

        def __iter__(self):
            return self

        def __next__(self):
            while self.currend_node:
                data = self.currend_node.data
                self.currend_node = self.currend_node.next_node
                return data

            raise StopIteration


def main():
    linked_list = LinkedList()

    inputs = 5
    min = 0
    max = 20

    for i in range(inputs):
        linked_list.insert_ending(random.randint(min, max))

    for i in range(inputs):
        linked_list.insert(random.randint(min, max))

    print(f'{linked_list}')
    length = len(linked_list)
    print(f'Länge: ' ,{length})



if __name__ == '__main__':
    main()