using System;
using System.Globalization;

class Program
{
    static void Main()
    {
        // Console.WriteLine("Enter a date (MM/DD/YYYY or Month Day, Year):");
        string input = Console.ReadLine();

        DateTime date;
        string[] formats = { "MM/dd/yyyy", "MMMM dd, yyyy" };

        if (DateTime.TryParseExact(input, formats, CultureInfo.InvariantCulture, DateTimeStyles.None, out date))
        {
            Console.WriteLine(date.DayOfWeek);
        }
        else
        {
            Console.WriteLine("None");
        }
    }
}
