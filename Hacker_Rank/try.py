# def count_substring(string, sub_string):
#     store=[]
#     final=[]
#     for i in string.lower():
#         for j in sub_string.lower():
#             if i == j:
#                 store.append(j)
#                 for k in store:
#                     if k not in final:
#                         final.append(k)

#     return len(final)


# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
    
#     count = count_substring(string, sub_string)
#     print(count)

add=''
string = input().strip()
sub_string = input().strip()
print(string,sub_string)
for i in string:
	for j in sub_string:
		if j==i:
			add+=j
print(add)