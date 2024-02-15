from copy import copy
tab=[]
for i in range(18):
    tab.append([0])
    tab.append([1])
i=2
n=6


while(i<=n):
    
    if(i%2==0):
        for j in range(int(i*i/2),i*i-1):
            tab[j]=copy(tab[j-int(i*i/2)])
            tab[j].append(0)
            
        for j in range(0,int(i*i/2)-1):
            tab[j].append(1)
    if(i%2!=0):
        for j in range(int(i*i/2),i*i-2):
            tab[j]=copy(tab[j-int(i*i/2)])
            tab[j].append(0)
            
        for j in range(0,int(i*i/2)-1):
            tab[j].append(1)

    
        
        
    
        
    
    i+=1
print(tab)
print(len(tab))

