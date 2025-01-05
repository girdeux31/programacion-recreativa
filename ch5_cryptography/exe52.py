from foo import transposition_encoder, transposition_decoder


print('Exercise 5.2')

message = 'Th1s 1s Transposition c0d3!_9'
delta = 6

print(f'Original message is \'{message}\'')

coded_message = transposition_encoder(message, delta)
print(f'Coded message is \'{coded_message}\'')

decoded_message = transposition_decoder(coded_message, delta)
print(f'Decoded message is \'{decoded_message}\'')