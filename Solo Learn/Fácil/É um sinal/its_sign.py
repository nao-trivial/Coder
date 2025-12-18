def is_palindrome(word):
    left = 0
    right = len(word) - 1
    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    return True

def main():
    # Entrada de 4 palavras
    words = []
    for _ in range(4):
        words.append(input().strip())

    # Cheque se ao menos uma palavra é um palindromo
    is_palindrome_found = any(is_palindrome(word) for word in words)

    # Output result
    if is_palindrome_found:
        print("Open")
    else:
        print("Trash")

if __name__ == "__main__":
    main()
