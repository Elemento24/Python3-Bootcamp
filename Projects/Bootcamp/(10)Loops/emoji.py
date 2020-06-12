# NESTED LOOPS

# for x in range(1, 11):
#     num = 0
#     while num < x:
#         print("\U0001f600", end="")
#         num += 1
#     print("\n")

# for num in range(1, 11):
#     count = 1
#     smileys = ""
#     while count <= num:
#         smileys += "\U0001f600"
#         count += 1
#     print(smileys)

# SINGLE LOOPS

# for x in range(1, 11):
#     print("\U0001f600"*x)

# times = 1
# while times < 11:
#     print("\U0001f600"*times)
#     times += 1

# CREATING A PYRAMID OF EMOJIS

for num in range(1, 21, 2):
    smileys = ""
    spaces = int((21-num)/2)
    for x in range(spaces):
        smileys += "  "
    for x in range(num):
        smileys += "\U0001f600"
    for x in range(spaces):
        smileys += " "
    print(smileys)
