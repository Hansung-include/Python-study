from cgi import print_arguments


a = 0
while a < 10:
    a = a + 1
    if a % 2==0: continue
    print(a)
