import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Solution {
    private static String solve(int n, String lydiaPath) {
        return "";
    }

    public static void main(String... args) {
        try {
            // BufferedReader in = new BufferedReader(new InputStreamReader (System.in));
            Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
            // int n = Integer.parseInt(in.readLine());
            int n = in.nextInt();
            int[] NARR = new int[n];
            int[] LARR = new int[n];
            int[][] nArr = new int[n][L];
            for (int i = 0; i < n; i++) {
                int N = in.nextInt();
                int L = in.nextInt();
                for (int j = 0; j < L; j++) {
                    nArr[i] = in.nextInt();
                }
            }
            for (int j = 0; j < n; j++) {
                String result = solve(nArr[j], pathArr[j]);
                System.out.print(String.format("Case #%d: %s", j + 1, result));
            }
        } catch (Throwable e) {
            e.printStackTrace();
            System.exit(1);
        }
    }
}