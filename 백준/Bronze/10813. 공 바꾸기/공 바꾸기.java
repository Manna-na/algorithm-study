import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();
		int[] basket = new int[N+1];
		for(int i = 1; i<=N; i++){
			basket[i] = i;
		}
		for(int i = 0; i<M; i++) {
			int one = sc.nextInt();
			int two = sc.nextInt();
			int tmp = basket[one];
			basket[one] = basket[two];
			basket[two] = tmp;			
		}
		for(int i = 1; i<=N; i++) {
			System.out.print(basket[i]+" ");
		}
	}
}