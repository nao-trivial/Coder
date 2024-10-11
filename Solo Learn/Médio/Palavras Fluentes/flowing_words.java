import java.util.Scanner;

public class SentenceFlow {

    public static String checkSentenceFlow(String sentence) {
        String[] words = sentence.toLowerCase().split(" ");  // Converte para minúsculas e divide a frase em palavras

        for (int i = 1; i < words.length; i++) {
            if (words[i].charAt(0) != words[i - 1].charAt(words[i - 1].length() - 1)) {
                return "false";
            }
        }

        return "true";
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Entrada de exemplo
        String sentence = scanner.nextLine();
        
        // Saída de exemplo
        System.out.println(checkSentenceFlow(sentence));  // Saída: true
    }
}