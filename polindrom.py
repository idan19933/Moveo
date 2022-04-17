







def is_polindrom(given_list):
    Polindrom = True
    for i in range(len(given_list)//2):
        if given_list[i] != given_list[-i-1]:
           Polindrom = False
           return Polindrom
    return Polindrom

# print(is_polindrom("aba"))
#
#
#
# # def num_changer(given_num)
#
#
# raw_age = input("What is your age?: ")
#
# new_age = []
# for i in range(len(raw_age)):
#     new_age.append(raw_age[-1-i])
# opp_age = "".join(new_age)
# k = 77
# print(f"Your opposite age is -{opp_age}")



#
# my_list = [1, 2, 2, 3, 2, 3, 4, 5, 4, 1, 4, 5]
# new_list = []
# for i in my_list:
#     if i not in new_list:
#         new_list.append(i)
# print(new_list)




my_list = [1, 2, 2, 3, 2, 3, 4, 5, 4, 1, 4, 5]

for i in my_list:
    if my_list.count(i) > 1:
        my_list.remove(i)
    else:
        continue
print(my_list)


def max_num(num1,num2):
    if num1 > num2:
        return num1
    return num2


print(max_num(-12,-4))



this_str ="What a lovely day dont you think huh?!"
split_Str = this_str.split()
print(split_Str)
new_dict = {}
for i in split_Str:
    new_dict.update({i:len(i)})
for k in new_dict:








print(new_dict)
new_list = []


print(new_list)





