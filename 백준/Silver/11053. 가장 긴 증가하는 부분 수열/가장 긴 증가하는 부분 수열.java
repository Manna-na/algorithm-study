import java.util.Arrays;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int[] A = new int[N];
		for(int i = 0; i<N; i++) {
			A[i] = sc.nextInt();
		}
		int[] dp = new int[N];
		for(int i = 0; i<N; i++) {
			dp[i]=1;
			for(int j = 0; j<i; j++) {
				if(A[i]>A[j]&&dp[i]<dp[j]+1)dp[i] = dp[j]+1;
				
			}
		}
//		System.out.println(Arrays.toString(dp));
		int res = dp[0];
		for(int i = 0; i<N; i++) {
			if(res < dp[i]) res = dp[i];
		}
		System.out.println(res);
	}
}