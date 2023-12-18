import java.util.Arrays;
import java.util.Scanner;

public class Main {
	static int k, n;
	static int[][] memo;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int testCase = sc.nextInt();
		for (int tc = 1; tc <= testCase; tc++) {
			k = sc.nextInt(); // 층
			n = sc.nextInt(); // 호
			memo = new int[k+1][n+1];
			for(int i = 0; i<=n; i++) {
				memo[0][i] = i;
			}
			for(int i = 0; i<=k; i++) {
				memo[i][0] = 0;
				memo[i][1] = 1;
			}
			for(int i = 1; i<=k; i++) {
				for(int j = 2; j<=n; j++) {
					memo[i][j] = memo[i][j-1]+memo[i-1][j];  
				}
			}
			
			System.out.println(memo[k][n]);
			
		}
	}

	
}
