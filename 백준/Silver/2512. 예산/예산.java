import java.util.Arrays;
import java.util.Scanner;

class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int[] arr = new int[N];
		for(int i = 0; i<N; i++) {
			arr[i] = sc.nextInt();
		}
		// 
		int max = sc.nextInt(); 
		int ans = 0;
		
		// 이분탐색이에욥 정력 해줘요
		Arrays.sort(arr);
		
		int end = arr[N-1];
		int start = 0;
		while(start<=end) {
			int mid = (start+end)/2;
			int sum = 0;
			for(int i = 0; i<arr.length; i++) {
				if(arr[i] >= mid) sum+= mid; // 주어진 예산의 값이 배정된 예산의 값보다 크면 배정된 예산의 값으로 갱신한다.
				else sum += arr[i]; // 배정된 예산 값이 더 작으면 주어진 예산을 그냥 더해
			}
			if(sum>max) end = mid-1; // 총 예산보다 sum값이 클 수 없다. 상한 수정 필요
			else {
				start = mid +1; 
				ans = Math.max(ans, mid); //정해진 총액 이하에서 가능한 한 최대의 총 예산을 배정해야한다.
			}
		}System.out.println(ans);
	}
}