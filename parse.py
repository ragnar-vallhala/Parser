from lex import Tokenizer
from grammar import CFG
from util import Stack , Tree
from colorama import Fore, Style

class Parser:
    
    def __init__(self, source, grammar):
        self.tokenizer = Tokenizer(source)
        self.grammar = CFG(grammar)
    
    def parse(self):
        print('-'*120)
        print(f"{Fore.GREEN}{'!!!Derrivations!!!':^120}{Style.RESET_ALL}")
        print('-'*120)
        i=0
        stack = Stack()
        while i<len(self.tokenizer):
            stack.push(self.tokenizer.getNextToken())
            stack1 = Stack()
            while len(stack)>0:
                stack1.arr.insert(0,stack.pop())
                _, result = self.can_reduce(stack1)
                if not _:
                    for res in result:
                        stack1.push(res)
                else:
                    stack.push(result)
                if len(stack)==0:
                    for res in stack1.arr:
                        stack.push(res)
                    break
                    
            i+=1
        print(stack)
        if len(stack)>1 or stack.head().type!=self.grammar.start[0]:
            raise Exception(f"{Fore.RED}{'Parsing failed!!!':^120}{Style.RESET_ALL}")
        else:
            print(f"{Fore.GREEN}{'Parsing successful!!!':^120}{Style.RESET_ALL}")
            return stack
        
    
    def can_reduce(self, stack:Stack):
        arr=[]
        while len(stack)>0:
            arr.insert(0,stack.pop())
            
        _,reduction = self.grammar.canReduce(arr)
        if not _:
            return _,arr
        else:
            return True, reduction         
            
            

if __name__ == "__main__":
    parser = Parser("input.txt", "grammar.txt")
    print('-'*120)
    print(f"{Fore.GREEN}{'!!!Rules!!!':^120}{Style.RESET_ALL}")
    print('-'*120)
    print(f'{Fore.LIGHTBLUE_EX}', end='')
    print(parser.grammar.print_rules())
    print(f'{Style.RESET_ALL}', end='')
    stack = parser.parse()
    token = stack.pop()
    
    print( "Root token : ",f"{Fore.YELLOW}", token.type, f'{Style.RESET_ALL}')
    
    t = Tree()
    t.root = token
    t.display_tree()    
    print('-'*120)
    print(f"{Fore.GREEN}{'!!!END!!!':^120}{Style.RESET_ALL}")
    print('-'*120)
    
