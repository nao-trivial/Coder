import java.util.Scanner;

public class PaintCostCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Entrada: número de cores
        int cores = scanner.nextInt();

        // Cálculo do valor total
        double valor = 40 + 5 * cores;
        valor += valor * 0.1; // Adicionando 10% de imposto

        // Saída: valor arredondado para o inteiro mais próximo
        System.out.println((int) Math.round(valor));

        scanner.close();
    }
}