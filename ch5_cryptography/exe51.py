from foo import cesar_encode


print('Exercise 5.1')

message = 'Th1s 1s Cesar c0d3!_9'
delta = 3

print(f'Original message is \'{message}\'')

coded_message = cesar_encode(message, delta)
print(f'Coded message is \'{coded_message}\'')

decoded_message = cesar_encode(coded_message, -delta)
print(f'Decoded message is \'{decoded_message}\'')