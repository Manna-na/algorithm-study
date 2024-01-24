import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
	static boolean[] visited;
	// 이차원 arraylist 배열
	static ArrayList<Integer>[] arr;
	static int M, N, R;
	static int[] result;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		StringBuilder sb = new StringBuilder();
		N = sc.nextInt(); // 정점의 수
		M = sc.nextInt(); // 간선의 수
		R = sc.nextInt(); // 시작 정점
		arr = new ArrayList[N + 1]; // arraylist 배열 생성, 정점번호 1부터 시작이니까 하나 크게 만들어주자
		for (int i = 1; i <= N; i++) {
			arr[i] = new ArrayList<>();// arraylist 인스턴스 생성
		}
		for (int i = 0; i < M; i++) {
			int u = sc.nextInt();
			int v = sc.nextInt();
			arr[u].add(v);// 양방향 간선이다.
			arr[v].add(u);
		}
		for(int i=1; i<=N;i++) {
			Collections.sort(arr[i]);
		}


		visited = new boolean[N+1];
		result = new int[N+1];
		
		bfs(R);
		for(int i = 1;i<N+1; i++) {
			sb.append(result[i]).append("\n");
		}
		System.out.println(sb);
	}

	static void bfs(int v) {
		Queue<Integer> queue = new LinkedList<>();
		visited[v] = true;
		queue.add(v);
		int curr = 0;
		int cnt=1;
		while (!queue.isEmpty()) {
			curr = queue.poll();
			result[curr] = cnt++;
			for (int y : arr[curr]) {
				if(!visited[y]) {
					visited[y] = true;
					queue.add(y);
				}
			}
	
		}
		
	}
}