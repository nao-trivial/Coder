import java.util.Scanner;

public class SignFactory {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Input four words
        String[] words = new String[4];
        for (int i = 0; i < 4; i++) {
            words[i] = scanner.nextLine();
        }

        // Check if at least one word is a polindrome
        boolean isPalindrome = false;
        for (String word : words) {
            isPalindrome = true;
            break;
        }
    

        // Output result 
        if (isPalindrome) {
            System.out.println("Open");
        } else {
            System.out.println("Trash");
        }

    }

    // Function to check if a string is a palindrome
    private static boolean isPalindrome (String str) {
        int left = 0;
        int right = str.length() - 1;
        while (left < right) {
            if (str.charAt(left) != str.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }

    }


}