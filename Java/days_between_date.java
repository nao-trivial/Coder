import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.time.temporal.ChronoUnit;
import java.util.Scanner;

public class DaysBetweenDates {

    public static void main(String[] args) {
        // Create a Scanner object for reading input
        Scanner scanner = new Scanner(System.in);

        // Prompt the user for the first date (older date)
        // System.out.println("Enter the first date (older date) in the format 'Month DD, YYYY':");
        String date1 = scanner.nextLine();

        // Prompt the user for the second date (newer date)
        // System.out.println("Enter the second date (newer date) in the format 'Month DD, YYYY':");
        String date2 = scanner.nextLine();

        // Calculate and print the number of days between the two dates
        long daysBetween = calculateDaysBetween(date1, date2);
        System.out.println(daysBetween);
    }

    public static long calculateDaysBetween(String start, String end) {
        // Define the date format
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("MMMM d, yyyy");

        // Parse the dates
        LocalDate startDate = LocalDate.parse(start, formatter);
        LocalDate endDate = LocalDate.parse(end, formatter);

        // Calculate the number of days between the dates
        return ChronoUnit.DAYS.between(startDate, endDate);
    }
}
