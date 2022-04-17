import os
secret_num = 4
guess_counter = 0
#
# while guess_counter <3:
#     guess = input("Type your guess: ")
#     guess_counter+=1
#     if int(guess) == secret_num:
#         print("You won!")
#         break
#     else:
#         if int(guess) > secret_num:
#             print("Your guess is too high.Try again")
#             break
#         elif int(guess) < secret_num:
#             print("Your guess is too low.Try again")
#             continue
# print("Maybe next time..")


# secret_num = 4
# guess_counter = 0
# while guess_counter<3:
#     guessing_number = int(input("Your guess: "))
#     if guessing_number<secret_num:
#         print("Your number is too low")
#         guess_counter +=1
#         if guess_counter>=3:
#             print("Sorry you lost!")
#             break
#     elif guessing_number>secret_num:
#         print("Your number is too high")
#         guess_counter += 1
#         if guess_counter>=3:
#             print("Sorry you lost!")
#             break
#     elif guessing_number==secret_num:
#          print("You won!")
#          break



mydict= {}
mystring = "sdfsdgsdgdsgdsgsddsaaaa"
for i in mystring:
    if mydict.get(i):
        mydict[i] += 1
    else:
        mydict[i] = 1
print(mydict)