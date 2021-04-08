mult =lambda a,b,c:(a+b)*c
soma = lambda a,b:a+b

print(mult(2,5,2))
print(soma(2,5))
print((lambda a,b,c:(a+b)*c)(2,5,2))

#
r = lambda x,func:x+func(x)
print(r(2,lambda x: x*x) )
print(r(2,lambda x:x+3))
