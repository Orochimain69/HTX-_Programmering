


def main(n):
    m=0    
    
    def fund(n):
            global m
            if n > 0:
                m = n+ fund(n-1)
            if n == 0:
                return(n)
            if n == 5:
                return(m)

            
    for k in range(n):
        m += fund(n)
    
    print(m)

main(5)
