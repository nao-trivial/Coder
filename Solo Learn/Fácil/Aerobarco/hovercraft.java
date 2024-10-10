import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int vendas = scanner.nextInt();
        int gastos = 2 * (int) Math.pow(10, 6) * 10;
        gastos += 1 * (int) Math.pow(10, 6);
        int lucro = vendas * 3 * (int) Math.pow(10, 6);

        if (lucro == gastos) {
            System.out.println("Broke Even");
        } else if (lucro < gastos) {
            System.out.println("Loss");
        } else if (lucro > gastos) {
            System.out.println("Profit");
        }
    }
}
