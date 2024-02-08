import java.util.Arrays;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		StringBuilder sb = new StringBuilder();
		int N = sc.nextInt();
		int[] arr1 = new int[N];
		for(int i = 0; i<N; i++) {
			arr1[i] = sc.nextInt();
		}
		int M = sc.nextInt();
		Arrays.sort(arr1);
		for(int i = 0; i<M; i++) {
			sb.append(binarySearch(arr1, N, sc.nextInt())+" ");
		}
		System.out.print(sb);
	}
	public static int binarySearch(int[] arr1, int N, int search) {
		int start = 0;
		int end = N-1;
		while(start<=end) {			
			int mid = (start+end)/2;
			if(arr1[mid]==search) {
				return 1;
			}
			if(arr1[mid]>search) {
				end = mid-1;
			}else {
				start = mid+1;
			}
			
		}
		return 0;
		
	}
}
