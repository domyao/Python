

class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return "<Node: " + str(self) + ">"


class LinkedList:


    def __init__(self, data = None):
        self.head = Node(data)


# - Notes----------------------------
#
# __init__ shoule be short, simple
# Anything thoughts other than the simple initialization should be considered into a seperate method.
#
#----------------------------------------------

    def __str__(self):
        base = ""
        for item in self:
            base += "{} => ".format(item)
        return base + "None"


    def __repr__(self):
        return "LinkedList: " + str(self)

# - Notes----------------------
#
# diff between __repr__ and __str__
#
#--------------------------



    def __iter__(self):
        """
        return a generator consist of the nodes
        """

        node = self.head

        while node != None:
            yield node         #do not "do it a favor", return a generator of the value of the nodes. better to keep the raw data.
            node = node.next




    def __len__(self):
        """
        get the length of the Linked List
        """

        count = 0
        node = self.head

        while node != None:
            count += 1
            node = node.next

        return count




    def add(self, data):
        """
        Add a single data to the end of the LinkedList
        Return: the new LinkedList object
        """

        last = self.peek()
        last.next = Node(data)
        return self






    def delete(self, data):
        """
        Delete the given data form the linked list.
        Return True if succeed, False if given data is not found
        """
        pre_node, node_to_delete = self.search(data)

        if pre_node == None:
            self.head = self.head.next
            return True

        if node_to_delete == None:
            return False

        pre_node.next = node_to_delete.next
        node_to_delete.next = None

        return True




# -----------------------------------------
#
# prevent the bad shit in the very beginning
#
# -----------------------------------


    def peek(self):
        """
        return the last item in the Linked List
        """

        node = self.head
        while node.next != None:
            node = node.next
        return node

        # while node != None:
        #     last = node
        #     node = node.next
        #
        # return last

    def push(self, data):
        """
        add the data to the front
        """
        self.head = Node(data, self.head)



    def search(self, data):
        tar_node = self.head
        pre_node = None

        while tar_node != None and tar_node.data != data:
            pre_node = tar_node
            tar_node = tar_node.next

        return (pre_node, tar_node)


# ----------------------------------------------------
# order matters:
#
#     while tar_node.data != data and tar_node != None :
#
#     will have error
#
# ------------------------------------------------



    def insert_after_data(self, insert_after, data_to_insert):
        """
        Insert new data at a specific location, which is defined by the data it would be insert after.
        Return True if succeed, False if the location is invalid.

        @param: data to insert after, data to insert
        Does it lose the advantage of linked list this way?


        """
        node_insert_after = self.search(insert_after)[1]

        if node_insert_after == None:
            return False
        else:
            new_node = Node(data_to_insert, node_insert_after.next)
            node_insert_after.next = new_node
            return True



    def insert_after(self, insert_after, data_to_insert):
        """
        Insert new data at a specific location, which is defined by the node it would be insert after.

        @param: node to insert after, data to insert

        """
        new_node = Node(data_to_insert, insert_after.next)
        insert_after.next = new_node





    def extend(self, *data):
        """
        Add a single data or a list of data at the end of the Linked list
        Return: the new LinkedList object


        """

        last = self.peek()
        for item in data:
            last.next = Node(item)
            last = last.next

        return self




    def print_forwards(self):

        """
        Print the elements within the Linkedlist forwards

        """

        for data in self:
            print(data)




    def print_backwards(self):

        """
        Print the elements within the Linkedlist backwards

        """
        node = self.head

        def _print_backwards(node):
          if node != None:
              _print_backwards(node.next)
              print(node.data)

        _print_backwards(self.head)






    @classmethod
    def linkedlist(cls, head_data, *data):
        """
        transform a list of data into Linked List, linkedlist(), acts like str(), list()
        A WHOLE NEW CONSTRUCTOR

        """

        new_list = cls(head_data)
        new_list.extend(*data)
        return new_list

