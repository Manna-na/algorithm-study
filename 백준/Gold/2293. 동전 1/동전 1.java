import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int K = sc.nextInt();
		int[] coin = new int[N+1];
		int[] dp = new int[K+1];
		for(int i = 1; i<=N; i++) {
			coin[i] = sc.nextInt();
		}
		dp[0] = 1;
		// 동전의 종류에 따라 최대 K번까지의 경우의 수가 발생한다..?
		for(int i = 1; i<=N; i++) {
			for(int j = coin[i]; j<=K; j++) {
				dp[j] += dp[j-coin[i]];
			}
		}
		System.out.println(dp[K]);
		
	}
}