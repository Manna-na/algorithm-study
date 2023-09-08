import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
	static ArrayList<Integer>[] map;
	static int N, M, V;
	static boolean[] visited;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();
		V = sc.nextInt();
		map = new ArrayList[N + 1]; // 정점번호는 1부터 N까지니까
		for (int i = 1; i <= N; i++) {
			map[i] = new ArrayList<>();
		}
		for (int i = 0; i < M; i++) {
			int s = sc.nextInt();
			int e = sc.nextInt();
			map[s].add(e);
			map[e].add(s);

		}
		// 오름차순으로 정렬
		for (int i = 1; i <= N; i++) {
			Collections.sort(map[i]);

		}
		visited = new boolean[N + 1];
		dfs(V);
		System.out.println();
		visited = new boolean[N + 1];
		bfs(V);

	}

	static void dfs(int x) {
		visited[x] = true;
		System.out.print(x + " ");
		for (int y : map[x]) {
			if (!visited[y]) {
				dfs(y);
			}
		}
	}

	static void bfs(int x) {
		Queue<Integer> queue = new LinkedList<>();
		visited[x] = true;
		queue.add(x);
		while (!queue.isEmpty()) {
			int y = queue.poll();
			System.out.print(y + " ");
			for (int i : map[y]) {
				if (!visited[i]) {
					visited[i] = true;
					queue.add(i);
				}
			}
		}
	}

}