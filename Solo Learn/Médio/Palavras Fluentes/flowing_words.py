def check_sentence_flow(sentence):
    words = sentence.lower().split()  # Convert to lowercase and split the sentence into words
    
    for i in range(1, len(words)):
        if words[i][0] != words[i-1][-1]:  # Check if the first letter of the current word matches the last letter of the previous word
            return 'false'
    
    return 'true'

# Sample Input
sentence = input()
# Sample Output
print(check_sentence_flow(sentence))  # Output: true
