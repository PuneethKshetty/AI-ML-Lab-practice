G = {
    'A':[[('B',1),('C',1)],[('D',1)]],
    'B':[[('G',1)],[('H',1)]],
    'C':[[('J',1)]],
    'D':[[('E',1),('F',1)]],
    'G':[[('I',1)]]
}
H = {
    'A':1,
    'B':6,
    'C':2,
    'D':12,
    'E':2,
    'F':1,
    'G':5,
    'H':7,
    'I':7,
    'J':1
}

class graph:
    def __init__(self,S,G,H):
        self.s = S
        self.h = H
        self.g = G
        self.status = {}
        self.solved = {}
        self.parent = {}
     
    def mincost(self,v):
        mcost = 0
        mlist = {}
        mlist[mcost] = []
        flag = True
        for nt in self.g.get(v,''):
            c = 0
            l = []
            for n,w in nt:
                c+=self.h.get(n,0)+w
                l.append(n)
                
            if flag:
                mcost = c
                mlist[mcost] = l
                flag = False
            
            elif mcost > c:
                mcost = c
                mlist[mcost] = l
        return mcost,mlist[mcost]
    
    
    def p(self):
        print(self.solved)
        
    def aostar(self,v,back):
        print(v,self.solved)
        if self.status.get(v,0) >= 0:
            mcost,mlist = self.mincost(v)
            self.h[v] = mcost
            self.status[v] = len(mlist)
            sol = True
            for n in mlist:
                self.parent[n] = v
                if self.status.get(n,0)!=-1:
                    sol = False 
            if sol:
                self.status[v] = -1
                self.solved[v] = mlist
        
            
            if v!=self.s:
                self.aostar(self.parent[v],True)
            
            if not back:
                for n in mlist:
                    self.status[n] = 0
                    self.aostar(n,False)
                
a = graph('A',G,H)
a.aostar('A',False)
a.p()
