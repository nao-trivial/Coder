import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int numero = scanner.nextInt();

        int contador = 1;
        int soma = 0;

        while (contador < numero) {
            if (contador % 3 == 0 || contador % 5 == 0) {
                soma += contador;
            }
            contador++;
        }

        System.out.println(soma);
    }
}
