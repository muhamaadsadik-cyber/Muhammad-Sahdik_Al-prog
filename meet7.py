#not,or,and,xor

print ("=====NOT=====")
a = True
b = not a
print("nilai dari b = ", b)

print ("=====XOR=====")
a = False
b = True
hasil = a ^ b 
print (a, "xor", b, "=", hasil)

print("====and====")
a = True
b = True
hasil = a and b 
print(a, "and", b, "=", hasil)

print("====or=====")
a = False
b = False
hasil = a or b
print(a, "or", b, "=", hasil)