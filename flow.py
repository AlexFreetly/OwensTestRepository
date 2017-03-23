def f(x):
    n=x 
    if int(n)==n:
        if n%2==0:
            if n%3==0:
                return ('is a multiple of 6')
            else: 
                return ('is even')
        else: 
            return ('is odd')
    else:
        return ('is not an integer')
                
            
def f_test():
    works = True
    if f(12) != 'is a multiple of 6':
            works = False
    if f(5) != 'is odd':
            works= False
    if f(2) != 'is even':
            works = False 
    if works==True: 
        print ('Alex is cool')
    else: 
        print ('works=false')
        
