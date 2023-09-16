import java.util.Arrays;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int[] A = new int[N + 1];
		int[] dp = new int[N + 1];
		int max = Integer.MIN_VALUE;
		for (int i = 0; i < N; i++) {
			A[i] = sc.nextInt();
			dp[i] = A[i];
			if(max < dp[i]) max = dp[i];
		}
		for(int i = 1; i<N; i++) {
			if(dp[i]<dp[i-1]+A[i])dp[i] = dp[i-1]+A[i];
			if(max<dp[i]) max = dp[i];
		}
		
		System.out.println(max);
	}
}