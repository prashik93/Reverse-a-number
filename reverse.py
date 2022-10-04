num=12345
temp=num
rev =0
count=0

while num>0:
    rem=num%10
    rev=(rev*10)+rem
    num=num//10
    count+=1

print(rev)
print(count)

same_position=(count+1)/2
print(same_position)
