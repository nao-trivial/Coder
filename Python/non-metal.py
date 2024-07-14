def replace_numbers_with_words(phrase):
    # Dictionary mapping numbers to their words
    number_words = {
        '0': 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine',
        '10': 'ten'
    }
    
    # Split the phrase into words
    words = phrase.split()
    
    # Replace numbers with words
    updated_words = [number_words[word] if word in number_words else word for word in words]
    
    # Join the words back into a phrase
    updated_phrase = ' '.join(updated_words)
    
    return updated_phrase

# Sample Input
input_phrase = input()

# Get the updated phrase
output_phrase = replace_numbers_with_words(input_phrase)

print(output_phrase)  # Output: "i need two pumpkins and three apples"
