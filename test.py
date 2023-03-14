class complex (object):
    def __init__(self,real, imag = 0):
            
        self.real = float(real)
        self.imag = float(imag)
            
    def __add__(self, other):
        return complex(self.real + other.real, self.imag + other.imag)
            
    def __radd(self ,other):
        return complex(self.real + other.real, self.imag + other.imag)
                
            
c1 = complex(2,3)
c2 = complex(4,5)

print((c1+4.0).real,(c1+4.0).imag)