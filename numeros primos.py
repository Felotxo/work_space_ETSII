a = 13
b = a // 2    # division entera
while b > 1:
    if a % b == 0: 
    print ("(b) es factor de (a)".format(b,a))
    break
b -= 1
else:
    print ("{} es primo".format(a))
print ("\nfuera del bucle.")


