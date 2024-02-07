import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
	static int N, M, R;
	static ArrayList<Integer>[] arr;
	static boolean[] visited;
	static int[] ans;
	static int order = 1;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		StringBuilder sb = new StringBuilder();
		N = sc.nextInt(); // 정점의 수
		M = sc.nextInt(); // 간선의 수
		R = sc.nextInt(); // 시작 정점
		arr = new ArrayList[N + 1];
		for (int i = 1; i <= N; i++) {
			arr[i] = new ArrayList<>();
		}
		for (int i = 0; i < M; i++) {
			int u = sc.nextInt();
			int v = sc.nextInt();
			arr[u].add(v);
			arr[v].add(u);
		}
		for (int i = 1; i <= N; i++) {
			Collections.sort(arr[i]);
		}
		visited = new boolean[N+1];
		ans = new int[N + 1];
		dfs(R);
		for(int i = 1 ; i<ans.length; i++) {
			sb.append(ans[i]).append("\n");
		}
		
		System.out.println(sb);
	
	}

	public static void dfs(int r) {
		visited[r] = true;
		ans[r] = order++;

		for (int v : arr[r]) {

			if (!visited[v]) {
				dfs(v);
			}
		}
	}

}