import java.util.Arrays;
import java.util.Scanner;

public class Main{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		StringBuilder sb = new StringBuilder();
		int N = sc.nextInt();
		int[] arr = new int[N];
		for(int i = 0; i<N; i++) {
			arr[i] = sc.nextInt();
		}
		Arrays.sort(arr);
		int M = sc.nextInt();
		for(int i = 0; i<M; i++) {
			sb.append(binarySearch(arr, N, sc.nextInt())).append("\n");
		}
		System.out.println(sb);
	}
	public static int binarySearch(int[] arr, int N, int search) {
		int start = 0;
		int end = N-1;
		while(start<=end) {
			int mid = (start+end)/2;
			if(arr[mid]==search) {
				return 1;
			}
			if(arr[mid]>search) {
				end = mid-1;
			}else {
				start = mid+1;
			}
		}
		return 0;
	}
}