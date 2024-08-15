#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

// Function to check if a word is a palindrome
bool is_palindrome(const std::string& word) {
    int left = 0;
    int right = word.length() - 1;

    while (left < right) {
        if (word[left] != word[right]) {
            return false;
        }
        left++;
        right--;
    }
    return true;
}

int main() {
    // Input four words
    std::vector<std::string> words(4);
    for (int i = 0; i < 4; i++) {
        std::getline(std::cin, words[i]);
    }

    // Check if at least one word is a palindrome
    bool is_palindrome_found = false;
    for (const auto& word : words) {
        if (is_palindrome(word)) {
            is_palindrome_found = true;
            break;
        }
    }

    // Output result
    if (is_palindrome_found) {
        std::cout << "Open" << std::endl;
    } else {
        std::cout << "Trash" << std::endl;
    }

    return 0;
}
