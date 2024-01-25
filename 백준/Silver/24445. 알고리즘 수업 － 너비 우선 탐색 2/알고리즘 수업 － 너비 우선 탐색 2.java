import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
	static int N, M, R;
	static boolean[] visited;
	static ArrayList<Integer>[] arr;
	static int[] res; // 결과 출력 배열

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		StringBuilder sb = new StringBuilder();
		N = sc.nextInt(); // 정점의 수
		M = sc.nextInt(); // 간선의 수
		R = sc.nextInt(); // 시작 정점
		arr = new ArrayList[N + 1]; // 정점번호 1부터 시작
		for (int i = 1; i <= N; i++) {
			arr[i] = new ArrayList<>(); // 인스턴스 생성
		}
		for (int i = 0; i < M; i++) {
			int u = sc.nextInt();
			int v = sc.nextInt();
			arr[u].add(v);
			arr[v].add(u);// 양방향 리스트
		}
//		System.out.println(Arrays.toString(arr));
		// 내림차순 정렬하래
		for (int i = 1; i <= N; i++) {
			Collections.sort(arr[i]);
			Collections.reverse(arr[i]);
		}

		visited = new boolean[N + 1];
		res = new int[N + 1];
		bfs(R);
		for(int i = 1; i<=N;i++) {
			sb.append(res[i]).append("\n");
		}
		System.out.println(sb);

	}

	public static void bfs(int r) {
		Queue<Integer> queue = new LinkedList<>();
		visited[r] = true; // 방문할 때 visited true로 바꿔
		queue.add(r); // 큐에 넣어
		int cnt = 1;
		int curr = 0;
		while (!queue.isEmpty()) {
			curr = queue.poll();
			res[curr] = cnt++; // 정점의 방문 순서 배열에 넣기
			for (int y : arr[curr]) {
				if (!visited[y]) {
					visited[y] = true;
					queue.add(y);
				}
			}
		}

	}
}