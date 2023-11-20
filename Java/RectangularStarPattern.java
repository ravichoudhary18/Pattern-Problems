public class RectangularStarPattern {
    public static void main(String[] args) {
        int rows = 5; // Number of rows
        int columns = 7; // Number of columns

        // Nested loops to print the pattern
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                System.out.print("* "); // Print a star followed by a space
            }
            System.out.println(); // Move to the next line after completing a row
        }
    }
}