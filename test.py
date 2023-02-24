
# class SimpleIterator:
#     def __init__(self, limit):
#         self.limit = limit
#         self.counter = 0

#     def __next__(self):
#         if self.counter < self.limit:
#             self.counter += 1
#             return self.counter
#         else:
#             self.counter = 1
#             return self.counter

# s_iter1 = SimpleIterator(3)

# print(next(s_iter1))
# print(next(s_iter1))
# print(next(s_iter1))
# print(next(s_iter1))
# print(next(s_iter1))


import secrets
import string
from traceback import print_tb


def generate_alphanum_crypt_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    # print(letters_and_digits)
    crypt_rand_string = ''.join(secrets.choice(
        letters_and_digits) for i in range(length))
    # print(crypt_rand_string)
    # print("Cryptic Random string of length", length, "is:", crypt_rand_string)
    return crypt_rand_string



list_organization = [generate_alphanum_crypt_string(16) for i in range(1000)]


# # generate_alphanum_crypt_string(16)
# for i in list_organization:
#     print(i)

# list_organization = []
# with open('new.txt', "w") as file:
    # file.write(list_organization)

print(list_organization)