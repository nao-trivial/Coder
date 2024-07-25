def encode_message(message):
    # Create a dictionary for letter mapping
    forward = "abcdefghijklmnopqrstuvwxyz"
    backward = forward[::-1]
    mapping = {forward[i]: backward[i] for i in range(len(forward))}
    
    # Encode the message
    encoded_message = ""
    for char in message.lower():
        if char in mapping:
            encoded_message += mapping[char]
        else:
            encoded_message += char
            
    return encoded_message

# Sample Input
input_message = input()

# Encode the message
encoded_message = encode_message(input_message)

# Print the encoded message
print(encoded_message)
