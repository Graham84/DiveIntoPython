def fac(n):
    print 'n = ', n
    if n > 1:
        return n * fac(n-1)
    else:
        print 'end of the line'
        return 1

    
fac(5)