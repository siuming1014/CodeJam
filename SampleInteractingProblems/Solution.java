import java.util.Scanner;

public class Solution {
    public static int solve(int a, int b) {
        return (a + b) / 2;
    }
    public static void interact(Scanner input, int a, int b) {
        int m = solve(a, b);
        System.out.println(m);
        String s = input.next();
        if (s.equals("CORRECT")) {
            return;
        } else if (s.equals("TOO_SMALL")) {
            interact(input, m + 1, b);
        } else {
            interact(input, a, m - 1);
        }
    }

    public static void main(String args[]) {
        Scanner input = new Scanner(System.in);
        int T = input.nextInt();
        for (int ks = 1; ks <= T; ks++) {
            int a = input.nextInt();
            int b = input.nextInt();
            int n = input.nextInt();
            interact(input, a + 1, b);
        }
    }
}