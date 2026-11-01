a = [ 12 ,24 ,31 ,43 ] 
lambdaFunc1 = lambda x : x % 5
print(a)
y = sorted(a,key = lambdaFunc1)
print(y)
