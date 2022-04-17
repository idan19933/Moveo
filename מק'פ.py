


myArray = [1,2,5,3,4,6,7,8,9,2,3,4,5,6,72,3,4,5,62,4,5,2,4,4,6]


h = []
for i in range(1,len(myArray)+1):
    if i in myArray:
        h.append(i)
print(h)

x = 1
# for i in range(len(myArray)):
#     myArray[i] = myArray[i] + (i)
#     x += 1
#
# print(myArray)