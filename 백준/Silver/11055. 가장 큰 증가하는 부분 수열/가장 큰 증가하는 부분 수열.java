import java.util.Scanner;

class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int[] A = new int[N];
		// A는 수열 A다.
		for (int i = 0; i < N; i++) {
			A[i] = sc.nextInt();
		}
		// D[N] = 수열 A의 합이 가장 큰 증가하는 부분 수열의 합
		int[] D = new int[N];
		// 조건1. i>j
		for (int i = 0; i < N; i++) {
			D[i] = A[i];
			for (int j = 0; j < i; j++) {
				// 조건2. A[i] > A[j]
				// 조건3. D[i] < D[j] + A[i] -> 가장 큰 합을 구하기 위한 과정
				if (A[i] > A[j] && D[i] < D[j] + A[i]) {
					D[i] = D[j] + A[i];
				}
			}
		}
		// D[N]이 가장 큰 값일 수가 없다. 최대값 구하자
		int res = Integer.MIN_VALUE;
		for(int i = 0; i<N; i++) {
			if(res<D[i]) res = D[i];
		}
		System.out.println(res);
	}
}