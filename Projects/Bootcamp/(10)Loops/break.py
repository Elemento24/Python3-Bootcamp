# while True:
#     command = input("Type 'exit' to exit : ")
#     if command == "exit":
#         break

times = int(input("How many times do I have to tell you? "))

for time in range(times):
    print("CLEAN UP YOUR ROOM!")
    if time >= 4:
        print("Do you even listen anymore!")
        break
