public class FibonacciSeries {

    public static void main(String[] args) {
        int n = 10; // Number of terms in the Fibonacci series
        int firstTerm = 0;
        int secondTerm = 1;

        System.out.println("Fibonacci Series up to " + n + " terms:");

        for (int i = 1; i <= n; i++) {
            System.out.print(firstTerm + " ");

            // Compute the next term
            int nextTerm = firstTerm + secondTerm;
            // Update the values of firstTerm and secondTerm
            firstTerm = secondTerm;
            secondTerm = nextTerm;
        }
    }
}
