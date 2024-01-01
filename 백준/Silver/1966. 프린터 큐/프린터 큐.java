import java.util.Collections;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int t=0;t<T;t++) {
			Queue<Integer> qWeight = new LinkedList<>();
			Queue<Integer> qIndex = new LinkedList<>();
			int N = sc.nextInt();
			int M = sc.nextInt();
			for(int i = 0; i<N; i++) {
				qWeight.add(sc.nextInt());
				qIndex.add(i);
			}
			int cnt = 1;
			while(!qWeight.isEmpty()) {
				int Max = Collections.max(qWeight);
				int curW = qWeight.poll();
				int curI = qIndex.poll();
				if(curW==Max) {
					if(curI==M) {
						System.out.println(cnt);
						break;
					}
					cnt++;
				}else {
					qWeight.add(curW);
					qIndex.add(curI);
				}
			}
			
		}
	}
}