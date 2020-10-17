def even_or_odd(number):
    num = int(input("Enter a number: "))
    if ((num) % 2) == 0:
        print ("{0} is Even".format(num))
    else:
        print ("{0} is Odd".format(num))


print (even_or_odd(2))
print (even_or_odd(0))
print (even_or_odd(-1))