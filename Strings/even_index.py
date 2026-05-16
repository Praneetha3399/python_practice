# Print characters at even index

message = "Hello, World!"

for i in range(len(message)):
    if i % 2 == 0:
        print(message[i])

print(message[::2])


# Print characters at odd index

for i in range(len(message)):
    if i % 2 != 0:
        print(message[i])

print(message[1::2])