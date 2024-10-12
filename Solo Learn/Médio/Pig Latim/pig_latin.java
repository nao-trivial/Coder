import java.util.Scanner;

public class PigLatinConverter {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        
        String[] palavras = input.split(" ");
        StringBuilder resultado = new StringBuilder();
        
        for (String palavra : palavras) {
            char primeiraLetra = palavra.charAt(0);
            String novaPalavra = palavra.substring(1) + primeiraLetra + "ay";
            resultado.append(novaPalavra).append(" ");
        }
        
        System.out.println(resultado.toString().trim());
    }
}
