class EcuacionLineal:
    
    def __init__(self,a,b,c,d,e,f):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        self.e=e
        self.f=f

    def tieneSolucion(self):
        return (self.a*self.d - self.b*self.c)!=0
    
    def getX(self):
        return (self.e*self.d - self.b*self.f)/(self.a*self.d - self.b*self.c)
    
    def getY(self):
        return (self.a*self.f - self.e*self.c)/(self.a*self.d - self.b*self.c)
    
n=input("ingrese a,b,c,d,e,f: ").split()
a=float(n[0])
b=float(n[1])
c=float(n[2])
d=float(n[3])
e=float(n[4])
f=float(n[5])

ecuacion= EcuacionLineal(a, b, c, d, e, f)
if ecuacion.tieneSolucion():
        print("x= ",ecuacion.getX(),",Y= ",ecuacion.getY())
else:
        print("la ecuacion no tiene solucion")



        