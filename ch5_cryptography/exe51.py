from foo import cesar_encoder, cesar_decoder


print('Exercise 5.1')

message = 'Th1s 1s Cesar c0d3!_9'
delta = 3

print(f'Original message is \'{message}\'')

coded_message = cesar_encoder(message, delta)
print(f'Coded message is \'{coded_message}\'')

decoded_message = cesar_decoder(coded_message, delta)
print(f'Decoded message is \'{decoded_message}\'')