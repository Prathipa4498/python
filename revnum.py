n = int(input())    
Rev = 0    
while(n > 0):    
    i = n %10    
    Rev = (Rev *10) +i    
    n = n //10 
print(Rev)   
