import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Solution {
    private static String solve(int n, String lydiaPath) {
        char[] pathArr = new char[2 * n - 2];
        for (int i = 0; i < pathArr.length; i++) {
            pathArr[i] = (lydiaPath.charAt(i) == 'E') ? 'S' : 'E';
        }
        return String.valueOf(pathArr);
    }

    public static void main(String... args) {
        try {
            BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
            int n = Integer.parseInt(in.readLine());
            int[] nArr = new int[n];
            String[] pathArr = new String[n];
            for (int i = 0; i < n; i++) {
                nArr[i] = Integer.parseInt(in.readLine());
                pathArr[i] = in.readLine();
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