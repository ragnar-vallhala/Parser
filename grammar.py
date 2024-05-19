from colorama import Fore, Style
import re
from lex import Token
class CFG:
    
    def __init__(self,path):
        self.terminal=[]
        self.non_terminal=[]
        self.start = []
        self.rules={}
        self.parse(path)
        self.reductions=0
        self.declared =[]
    
                
    def canReduce(self, tokens: list):
        arr=[]
        for i in tokens:
            arr.append(i.type)
        #uncomment to check redeclaration
        # if len(tokens)==1:
        #     if tokens[0].type=='ID':
        #         if tokens[0].value in self.declared:
        #             raise Exception(f"{Fore.RED}Redeclaration of variable {tokens[0].value}")
        #         else:
        #             self.declared.append(tokens[0].value)
        for j in self.rules.keys():
            for k in self.rules[j]:
                if k==arr:
                    self.reductions+=1
                    print(f"{Fore.YELLOW}{str(arr):<40}{Fore.RED}{'->':^40}{Fore.YELLOW}[{j}]{Style.RESET_ALL}")
                    t = Token(j,j)
                    t.node.children = tokens
                    return (True,t)
        return (False,"")
    
        
        
            
        
        
    
    def print_rules(self) -> None:
        for i in self.rules.keys():
            print(i, end=":")
            for j in self.rules[i]:
                for k in j:
                    print(k, end=" ")
                print()
            print(";")
            

        
    def parse(self,path:str):
        s=""
        count=0
        with open(path,'r') as f:
            while count<2:
                line = f.readline().strip()
                if line=='%%':
                    count+=1
                elif len(line)>0:
                    s+=line + '\n'
        i=0
        while i<len(s):
            while i<len(s) and s[i]!='^':
                if s[i]=='%':
                    i+=1
                    token=''
                    while i<len(s) and  s[i]!=':':
                        token+=s[i]
                        i+=1
                    i+=1
                    if token=="non_terminal":
                        elements=""
                        while i<len(s) and s[i]!='\n':
                            elements+=s[i]
                            i+=1
                        self.non_terminal=list(elements.split())
                    elif token=="terminal":
                        elements=""
                        while i<len(s) and s[i]!='\n':
                            elements+=s[i]
                            i+=1
                        self.terminal=list(elements.split())
                    elif token=="start":
                        elements=""
                        while i<len(s) and s[i]!='\n':
                            elements+=s[i]
                            i+=1
                        self.start=list(elements.split())
                        if len(self.start)>1:
                            raise Exception(f'Start symbol can only be one.')
                    else:
                        raise Exception(f'Unknown definition {Fore.RED + token + Style.RESET_ALL} in the grammar.')
                i+=1
            while i<len(s):
                token=''
                while i<len(s) and s[i]!=':':
                    if re.match(r"\W+",token):
                        token=""
                    else:
                        token+=s[i]
                        i+=1
                if i>=len(s):
                    break
                if token not in self.non_terminal:
                    raise Exception(f'{Fore.RED + token + Style.RESET_ALL} is not a non-terminal.')
                else:
                    productions=[]
                    words=""
                    while i<len(s) and s[i]!=';':
                        if re.match(r"\W+",words):
                            words=""
                        elif s[i]=='\n':
                            i+=1
                            continue
                        elif s[i]=='|':
                            i+=1
                            words=list(words.split())
                            productions.append(words)
                            words=""
                        else:
                            words+=s[i]
                            i+=1
                    if s[i]==';':
                        words=list(words.split())
                        productions.append(words)
                        words=""
                    self.rules[token]=productions
                
            i+=1


if __name__ == "__main__":
    g=CFG("grammar.txt")
    print(g.rules)
