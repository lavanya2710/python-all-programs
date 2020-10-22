class node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class linkedlist:
    def __init__(self):
        self.head=None
    def printlist(self):
        if self.head is None:
            return
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref
    def add(self,new_data):
        new_node=node(new_data)
        new_node.ref=self.head
        self.head=new_node
    def end(self,new_data):
        new_node=node(new_data)
        if self.head is not None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_node
    def after(self,new_data,x):
        n=self.head
        while n is not None:
            if x==n.data:
                break
            else:
                n=n.ref
        if n is None:
            print("not found")
        else:
            new_node=node(new_data)
            new_node.ref=n.ref
            n.ref=new_node
    def before(self,new_data,x):
        if self.head is none:
            return 
        if self.head==x:
            new_node=node(new_data)
            new_node.ref=n.ref
            n.ref=new_node
            return
        return
        n=self.head
        while n.ref is not None:
            if n.ref.data==x:
                break
            n=n.ref
        if n.ref is not None:
            return
        else:
            new_node=node(new_data)
            new_node.ref=n.ref
            n.ref=new_node
