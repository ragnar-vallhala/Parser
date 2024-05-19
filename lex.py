import re
from util import Node

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value
        self.node = Node(value)    
    def __str__(self) -> str:
        return f"(Type: {self.type}, Value: {self.value}, Node: {self.node})"


class Tokenizer:
    
    def __init__(self, path):
        self.s = ""
        self.words = []
        self.tokens = []
        self.wordIndex = 0
        self.tokenIndex = 0
        
        with open(path, "r") as f:
            while True:
                line = f.readline()
                if not line:
                    break
                self.s += line
                
        self.lex()
        self.tokenize()
    
    def lex(self):
        self.words = list(self.s.split())
        for i in self.words:
            if ';' in i and i!=';':
                index = self.words.index(i)
                self.words.remove(i)
                i = i.replace(';',';$;')
                k=0
                for y in list(i.split(';')):
                    y=y.strip()
                    if y=='':
                        continue
                    if y!='$' and len(y)>0:
                       self.words.insert(index + k, y)
                    else:
                        self.words.insert(index + k,';' )
                    k+=1
        for i in self.words:
            if ',' in i and i!=',':
                index = self.words.index(i)
                self.words.remove(i)
                i = i.replace(',',',$,')
                k=0
                for y in list(i.split(',')):
                    
                    if y!='$' and len(y)>0:
                       self.words.insert(index + k, y)
                    else:
                        self.words.insert(index + k,',' )
                    k+=1
        for i in self.words:
            if '(' in i and i!='(':
                index = self.words.index(i)
                self.words.remove(i)
                i = i.replace('(','($(')
                k=0
                for y in list(i.split('(')):
                    
                    if y!='$' and len(y)>0:
                       self.words.insert(index + k, y)
                    else:
                        self.words.insert(index + k,'(' )
                    k+=1
        for i in self.words:
            if ')' in i and i!=')':
                index = self.words.index(i)
                self.words.remove(i)
                i = i.replace(')',')$)')
                k=0
                for y in list(i.split(')')):
                    
                    if y!='$' and len(y)>0:
                       self.words.insert(index + k, y)
                    else:
                        self.words.insert(index + k,')' )
                    k+=1
        self.words = self.words
    
    def getNextWord(self):
        r = self.words[self.wordIndex]
        self.wordIndex+=1
        return r
    
    def setWordIndex(self, i):
        self.wordIndex = i
    
    def getWordIndex(self):
        return self.wordIndex
    
    def tokenize(self):
        while self.wordIndex<len(self.words):
            token = self.getNextWord()
            self.findToken(token)
            
    
    def findToken(self, token):
        
        if token=='bool':
            self.tokens.append(Token("bool", "bool"))
            
        elif token=='char':
            self.tokens.append(Token("char", "char"))
            
        elif token=='float':
            self.tokens.append(Token("float", "float"))
            
        elif token=='int':
            self.tokens.append(Token("int", "int"))
            
        elif token=='long':
            i = self.getWordIndex()
            t = self.getNextWord()
            if t=='long':
                ii = self.getWordIndex()
                tt = self.getNextWord()
                if tt=='int':
                    self.tokens.append(Token("long_long_int", "long_long_int"))
                else:
                    self.tokens.append(Token("long_long", "long_long"))
                    self.setWordIndex(ii)
            elif t=='int':
                self.tokens.append(Token("long_int", "long_int"))
            elif t=='double':
                self.tokens.append(Token("long_double", "long_double"))
            else:
                self.tokens.append(Token("long", "long"))
                self.setWordIndex(i)
        elif self.isID(token):
            self.tokens.append(Token("ID", token))
        elif token==';':
            self.tokens.append(Token("SEMI", ';'))
        elif token==',':
            self.tokens.append(Token("COMMA", ","))
        elif token=='(':
            self.tokens.append(Token("LPAREN", "("))
        elif token==')':
            self.tokens.append(Token("RPAREN", ")"))
        else:
            print("Error: Unknown token: ", '['+token+']')
            exit()
            
    def isID(self,token):
        return re.match("[a-zA-Z_][a-zA-Z_0-9]*", token)

    def getNextToken(self) -> Token:
        if self.tokenIndex>=len(self.tokens):
            raise Exception("No more tokens")
        r = self.tokens[self.tokenIndex]
        self.tokenIndex+=1
        return r
    
    def getTokenIndex(self):
        return self.tokenIndex
    
    def setTokenIndex(self, i):
        self.tokenIndex = i
    
    def __len__(self) -> int:
        return len(self.tokens)

