import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Queue<Integer> q = new LinkedList<>();
		int N = sc.nextInt();
		for (int i = 1; i <= N; i++) {
			q.add(i);
		}
		for(int i = 0; i<N-1; i++) {
			q.remove();
			q.add(q.remove());
		}
		System.out.println(q.peek());

	}
}
