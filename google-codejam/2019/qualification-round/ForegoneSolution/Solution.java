import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Solution {
	private static String[] solve(String n) {
		String a = "";
		String b = "";
		for (char c : n.toCharArray()) {
			if (c == '4') {
				a = a.concat("2");
				b = b.concat("2");
			} else {
				a = a.concat(new String(new char[] { c }));
				if (b.length() > 0) {
					b = b.concat("0");
				}
			}
		}
		return new String[] { a, b };
	}

	public static void main(String... args) {
		try {
			BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
			int n = Integer.parseInt(in.readLine());
			String[] nArr = new String[n];
			for (int i = 0; i < n; i++) {
				nArr[i] = in.readLine();
			}
			for (int j = 0; j < n; j++) {
				String[] result = solve(nArr[j]);
				System.out.print(String.format("Case #%d: ", j + 1));
				System.out.println(String.join(" ", result[0], result[1]));
			}
		} catch (Throwable e) {
			e.printStackTrace();
			System.exit(1);
		}
	}
}