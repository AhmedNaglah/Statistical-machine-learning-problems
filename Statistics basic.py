# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

n = int(input())

arr = list(map(int,input().split()))

arr2 = sorted(arr)
if n%2==0:
    pass
    median = (arr2[int(n/2)-1]+arr2[int(n/2)])/2
else:
    median = arr2[int(math.floor(n/2))]

mysum = 0
freq = {}

# conf interval is x = mean +- 1.96 * sd /sqrt(n)
# sd = sqrt( sum((x-mean)**2) /n)

for i in range(n):
    pass
    mysum+=arr[i]
    try:
        freq[arr[i]]+=1
    except:
        freq[arr[i]]=1
mean = mysum/n

sd = 0
freq_max = 0
mode = None
for i in range(n):
    elem = arr[i]
    sd+= (elem-mean)**2
    fq = freq[elem]
    if fq>=freq_max:
        if fq==freq_max:
            if elem<mode:
                mode =elem
        else:
            mode =elem    
        freq_max=fq
        
sd = (sd/n)**(0.5)

ci_lower = mean - 1.96*sd/(n)**(0.5)
ci_upper = mean + 1.96*sd/(n)**(0.5)

print(round(mean,1))
print(round(median,1))
print(mode)
print(round(sd,1))
print(str(round(ci_lower,1))+' '+ str(round(ci_upper,1)))


    
    
