# list = [-12,5,7,8,1,2,-12,28,36,6,2,7,7]

# set=set()
# size = len(set)
# for x in list:
#     size = size+1
#     b = set.add(x)
#     if size !=len(set):
#         print(x)
#         size=size-1
# print (set)

# list.sort()
# print (list)
# for i in range(1,len(list)):
#     if list[i]==list[i-1]:
#         print(list[i])


dict = {"z": 3, 4: 7, 1: 6, 2: 2, 3: 3, "tt": 3, "ff": 6}
list = []
for k in dict:
    list.append(dict[k])

list.sort()
set = set()
for i in range(1, len(list)):
    if list[i] == list[i - 1]:
        set.add(list[i])

for key, value in dict.items():
    if value in set:
        print(f"{key} - {value}")
