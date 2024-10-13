import java.util.Scanner;
import java.lang.Math;

public class Program
{
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int houses = input.nextInt();
        double resultado;
        //your code goes here
        
        resultado = (2.0 / houses) * 100;
        double inteiro = Math.floor(resultado);
        
        if (resultado > inteiro) {
        inteiro += 1;
        System.out.println((int)inteiro);
        } else {
        System.out.println((int)inteiro);
        }   
    }
}

