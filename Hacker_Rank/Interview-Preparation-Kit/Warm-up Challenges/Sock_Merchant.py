# n=int(input())
# n2=input()
# ar=str(n2)
# ar=ar.split()
# pair={}
# total=0
# for i in ar:
#     if i not in pair:
#         pair[i]=1
#     else:
#         pair[i]+=1
# for j in pair:
#     store=pair[j]//2
#     total+=store
# print (total)



n=int(input("number of socks :"))
ar=input("colors of socks :").split()
pair={}
total=0

for i in ar:
    if i not in pair:
        pair[i]=1
    else:
        pair[i]+=1
for j in pair:
    store=pair[j]//2
    total+=store
print (total)

