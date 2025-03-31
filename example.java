public class Mystery {
    public static int mystery1(int n) {
        if (n <= 0) {
            throw new IllegalArgumentException("Input should be a positive integer.");
        }
        if (n == 1) return 0;
        if (n == 2) return 1;
        return mystery1(n - 1) + mystery1(n - 2);
    }

    public static void main(String[] args) {
        int n = 10;
        System.out.println("Mystery(" + n + ") = " + mystery1(n));
    }
}