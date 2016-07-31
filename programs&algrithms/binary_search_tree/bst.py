class TreeNode:

    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


    def __str__(self):
        return str(self.val)


    def __repr__(self):
        return "<Node: " + str(self) + ">"



class Tree:

    def __init__(self, root_node):
        self.root = TreeNode(root_node)



    def insert(self, data):

        def _insert(ex_node, data):

            if data <= ex_node.val:
                if ex_node.left == None:
                   ex_node.left = TreeNode(data)
                else:
                   _insert(ex_node.left, data)
            else:
                if ex_node.right == None:
                    ex_node.right = TreeNode(data)
                else:
                    _insert(ex_node.right, data)

        _insert(self.root, data)


    def search(self, data):

        def _search(curr_node, data):
            if curr_node == None:
                return False
            if data == curr_node.val:
                return True
            elif data < curr_node.val:
                return _search(curr_node.left, data)    # have to return from everywhere it recurse, it is not like that if you return halfway, it's gonna jump out from the recursion; NO, it always go back to the first fuction you called!!!!!!
            else:
                print("curr_node.right", curr_node.right)
                return _search(curr_node.right, data)


        return _search(self.root, data)


# --------------------------------------------
#
# If gonna return, you have to return from every recursion step/stage,
# if you return halfway, it's NOT gonna jump out from the recursion and terminate it
# it always go back all the way to the point when you first call the fuction.
#
# ---------------------------------------------

    def preorder(self):

        def _preorder(node):
            if node != None:
                print(node)
                _preorder(node.left)
                _preorder(node.right)

        _preorder(self.root)





    def postorder(self):

        def _postorder(node):
            if node != None:

                # puting print at the end will result in printing from the leaves to the top XD, unexpected first thought
                _preorder(node.left)
                _preorder(node.right)
                print(node)

        _postorder(self.root)




    def inorder(self):

        def _inorder(node):

            if node.left != None:
                _inorder(node.left)

            print(node)

            if node.right != None:
                _inorder(node.right)

        _inorder(self.root)



    def balance(self):
        pass




# ---------------------------------------------
#
# the sequence of the statements within a recursive function makes a big difference !
#
# ---------------------------------------------

if __name__ == "__main__":

        tree = Tree(23)
        tree.insert(12)
        tree.insert(34)
        tree.insert(5)
        tree.insert(20)
        tree.insert(30)
        tree.insert(50)
