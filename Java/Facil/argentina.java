import java.util.Scanner;

public class Program {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int pesos = input.nextInt();
        int dollars = input.nextInt();

        double exchange = 0.02 * pesos;

        if (exchange > dollars) {
            if (exchange > dollars) {
                System.out.println('Dollars');
            } else {
                System.out.println('Pesos');
            }
        }
    }
}