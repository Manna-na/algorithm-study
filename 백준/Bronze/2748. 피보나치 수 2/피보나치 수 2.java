import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		// 이전 값들을 더한 값을 저장하는 배열을 만들자 
		long[] memo = new long[91];
		memo[0] = 0;
		memo[1] = 1;
//		memo[2] = memo[1]+memo[0]; //1+0
//		memo[3] = memo[2]+memo[1]; //1+1
//		memo[4] = memo[3]+memo[2]; //2+1=3
		for(int i = 2; i<=N; i++) {
			memo[i] = memo[i-1]+memo[i-2];
		}
		System.out.println(memo[N]);
		
	}

}