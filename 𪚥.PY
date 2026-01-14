import random as r
import math as m
上 = 0
下 = 0

class 𪚥:

    #a=0 #fal
    #uncontrolled destruction section
    def æ_(self, æ): #ascii range
        a =[char for char in æ]
        for x in a:
            a[a.index(x)] = chr(r.randrange(0,128))
        return "".join(a)
    
    def maganda(self, ka): #random list char
        pagkamahalan = ['l','o','v','e']
        a =[char for char in ka]
        for x in a:
            a[a.index(x)] = r.choice(pagkamahalan)
        return "".join(a)
    
    def mooie(self, je): #mathcomb
        a =[char for char in je]
        for x in a:
            a[a.index(x)] = str(m.comb(r.randrange(0,129),r.randrange(0,129)))
        return "".join(a)
    
    def _(self, _) -> str: # random bin
        a =[ord(char) for char in _]
        for x in a:
            a[a.index(x)] = str(x%2)
        return "".join(a)
    


    #controlled destruction section