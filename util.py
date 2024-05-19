from colorama import Fore, Style
class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children is not None else []
    
    def __str__(self):
        ch=''
        for i in self.children:
            ch+=f'{i.value},'
        if len(ch)>0:
            ch=ch[:-1]
        s=f'(Value: {self.value}, Children: [{ch}])'
        return s
    
    
class Tree:
    def __init__(self):
        self.root = None
        self.positions = {}
    
    def add_node(self, value, parent=None):
        node = Node(value)
        if parent is None:
            if self.root is None:
                self.root = node
            else:
                raise ValueError("Root node already exists")
        else:
            parent.children.append(node)
        return node
    
    def display_tree(self, node=None, depth=0, start=1):
        if start==1:
            print('-'*120)
            print(f"{Fore.GREEN}{'!!!Parse Tree!!!':^120}{Style.RESET_ALL}")
            print('-'*120)
        if node is None:
            node = self.root
        self.printNode(node.value)
        for i, child in enumerate(node.node.children):
            if i < len(node.node.children) - 1:
                print(Fore.RED + '  ' * depth + '├─' + Style.RESET_ALL, end='')
            else:
                print(Fore.RED + '  ' * depth + '└─' + Style.RESET_ALL, end='')
            self.display_tree(child, depth + 1,0)
    
    def assign_positions(self, node=None, depth=0):
        if node==None:
            return
        self.positions[node] = (depth, len(self.positions))
        for child in node.node.children:
            self.assign_positions(child, depth+1)
            
            

    def is_below_position(self, node, position):
        return self.positions[node][0] == position[0] and self.positions[node][1] > position[1]

    # def display_tree(self, node=None):
    #     if node==None:
    #         node = self.root
            
    #     stack=[node]
    #     while len(stack)>0:
    #         node = stack.pop()
    #         print(node.value)
    #         for child in node.node.children:
    #             stack.append(child)
                
    def printNode(self, value:str)->None:
        types = ['long_long_int', 'long_long', 'long_int', 'float', 'int', 'char', 'bool', 'long', 'long_double', 'long']
        color=''
        if value=='stmt_list':
            color=Fore.GREEN
        elif value=='stmt' or value=='ID_list':
            color=Fore.BLUE
        elif value=='type':
            color=Fore.BLUE      
        elif value==';' or value in types:
            color=Fore.MAGENTA      
        elif value==',':
            color=Fore.YELLOW      
        else:
            color=Fore.WHITE
        
        print(color+value+Style.RESET_ALL)
                
                
                
class Stack:
    
    def __init__(self, stack=None):
        self.arr = []
        if stack is not None:
            self.arr = stack.arr.copy()
    
    def push(self,value):
        self.arr.append(value)
    
    def pop(self):
        return self.arr.pop()
    
    def head(self):
        return self.arr[-1]
    
    def tail(self):
        return self.arr[0]

    def __len__(self):
        return len(self.arr)
    
    def __str__(self):
        s=''
        for i in self.arr:
            s+=str(i)
            s+=' -> '
        return s[:-4]
    
    
