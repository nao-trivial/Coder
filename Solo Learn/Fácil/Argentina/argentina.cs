using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace Sololearn
{
    class Program
    {
        static void Main(string[] args)
        {
            int pesos, dollars;
            double exchange;
            
            pesos = Convert.ToInt32(Console.ReadLine());
            dollars = Convert.ToInt32(Console.ReadLine());
            
            exchange = 0.02 * pesos;
            
            if (exchange > dollars) {
                Console.WriteLine("Dollars");
            } else {
                Console.WriteLine("Pesos");
            }
        }
    }
}
