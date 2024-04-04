import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int[] str = new int[N];
		for(int i = 0; i<N; i++) {
			str[i] = sc.nextInt();
		}
		int v = sc.nextInt();
		int res = 0;
		for(int i = 0; i<N; i++) {
			if(str[i]==v) res++;
		}
		System.out.println(res);
	}
}