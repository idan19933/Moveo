# d = {'x': 10, 'y': 20, 'z': 30}
# for dict_key, dict_value in d.items():
#     print(dict_key,'->',dict_value)
#
#
# x = d.items()
# print(x)
#
# d = {'x': 10, 'y': 20, 'z': 30}
# e = {'x': 10, 'y': 20, 'z': 30}
#
# for i in d:
#     d[i] = d[i] + e[i]
# print(d)
#
# print(d.keys())
#
# strstr = "1234abcd"
# srt = strstr[::-1]
# print(srt)
#
# Sample_String ='The quick Brow Fox'
# lower_Case_counter = 0
# Upper_Case_counter = 0
# for i in Sample_String:
#     if i.islower():
#         lower_Case_counter += 1
#     elif i.isupper():
#         Upper_Case_counter += 1
#
# print(lower_Case_counter)
# print(Upper_Case_counter)
#
#
#
# def unique_items(given_list):
#     given_list = list(dict.fromkeys(given_list))
#     return given_list
#
# def uniquey_items(given_list):
#     ne_list = []
#     for i in given_list:
#         if i in ne_list:
#             continue
#         else:
#             ne_list.append(i)
#     return  ne_list
#
#
# def prime_number(num):
#     if num/num == 1 and num/1 == 0:
#         print(f"{num} Is a prime number")
#     else:
#         print(f"{num} Is not a prime number")
#
# print(prime_number(6))
#
# print(uniquey_items([1,2,3,3,4,5,6,6,6,7]))
# print(unique_items([1,2,3,3,4,5,6,6,6,7]))
#
#
# for x in range(2,7):
#     print(x)
#
# def test_prime(n):
#     if (n==1):
#         return False
#     elif (n==2):
#         return True;
#     else:
#         for x in range(2,n):
#             if(n % x==0):
#                 return False
#         return True
# print(test_prime(13))
#
#
# def even_num(num_list):
#     even_nums = []
#     for i in num_list:
#         if i % 2 == 0:
#             even_nums.append(i)
#         else:
#             continue
#     return even_nums
#
# print(even_num([1,2,3,44,5,78,5,4,66,223,2244]))

program = 'a = 5\nb=10\nprint("Sum =", a+b)'
exec(program)

def Is_Polindrom(given_list):
    for i in range(len(given_list)//2):
        if given_list[i] != given_list[-i-1]:
            return False
    return True

print(Is_Polindrom([1,2,1,2,1]))



def string_printer(give_string):
    return exec(give_string)

print(string_printer("print(hello world)"))