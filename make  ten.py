
import    itertools
import   sys
for  i  in  range(100):
    
    x=input("input 1th.number")
    y=input("input 2th.number")
    z=input("input 3th,number")
    p=input("input 4th.number")
    a=[x,y,z,p]
    b=["+","-","*","/" ]

    for  c  in   itertools.permutations(a,4):
        for  d in   itertools.product(b,repeat=3):  
             try:
                                           
                                           
                                            
                                              
                 
                                    
                                                  s1="("+c[0]+d[0]+c[1]+")"+d[1]+"("+c[2]+d[2]+c[3]+")"       
                                                  s2=c[0]+d[0]+"("+c[1]+d[1]+"("+c[2]+d[2]+c[3]+")"+")"
                                                  s3=c[0]+d[0]+"("+"("+c[1]+d[1]+c[2]+")"+d[2]+c[3]+")"
                                                  s4="("+c[0]+d[0]+"("+c[1]+d[1]+c[2]+")"+")"+d[2]+c[3]
                                                  s5="("+"("+c[0]+d[0]+c[1]+")"+d[1]+c[2]+d[2]+c[3]+")"
                                           
                                           
                                             

                                                  s=eval(s1)
                                                  if  s==10   :
                                       
                                                     print( s1+ "=10")
                                                  t=eval(s2)
                                                  if   t==10:
                                                     print(s2+"=10")
                                                 
                                                  u=eval(s3)
                                                  if   u==10:
                                                     print(s3+"=10")
                                                  v=eval(s4)
                                                  
                                                  if  v==10:
                                                     print(s4+"=10")
                                                  w=eval(s5)
                                                  
                                                
                                                 
                                                 
                                                  
                                                  if  w==10:
                                                     print(s5+"=10")
                                                 
             except ValueError   :
                 pass
             except ZeroDivisionError   :
                 pass
                                           
    q=input("to  stop  game  enter 1  else   enter  2  :   ")
    if  q=="1":
        print("game  over")
        sys.exit()                
                                           




                                   
