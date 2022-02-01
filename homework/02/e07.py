def output(message, times):
    i = 0
    while i < times:
        print(str(message), end ='')
        i = i + 1
    print()

message = input("Give message to repeat: ")
times = int(input("How many times?: "))

output(message, times)