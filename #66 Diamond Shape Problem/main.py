    #          A
    #        /   \ 
    #      /      \ 
    #    B         C
    #     \       /
    #      \     /
    #        \  /
    #          D 

class a :
    def __init__(self) -> None:
        self.syhari = 'content of a'
    pass

class b(a):
    def __init__(self) -> None:
        self.syhari = 'content of b'
    pass

class c(a):
    def __init__(self) -> None:
        self.syhari = 'content of c'
    pass

class d(b,c):
    def __init__(self) -> None:
        self.syhari = 'content of d'
    pass

d1 = d()
print(d1.syhari)    

#if no content in d then 
# order is d(b,c) => content of b
# order is d(c,b) => content of c
# our priority is based from left to right