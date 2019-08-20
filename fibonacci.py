#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Estudiantes
#
# Created:     13/10/2017
# Copyright:   (c) Estudiantes 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def fibonacci(num):
    u=0
    pu=1
    n=num
    num=num-1
    for i in range(0,num+1):
        r=u+pu
        pu=u
        u=r
    return r;

def Rfibonacci(num):
    if(num>2):
        return Rfibonacci(num-1)+Rfibonacci(num-2)
    else:
        return 1



def main():
    pass
    num=int(input( "Ingresar Numero Positivo \n") )
    if num==0:
        print ("Promedio Indeterminado")
    else:
        print ("Fibonacci= ", fibonacci(num))

if __name__ == '__main__':
    main()