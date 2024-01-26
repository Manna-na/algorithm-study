import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
	static int N, M, R;
	static ArrayList<Integer>[] arr;
	static boolean[] visited;
	static int[] res;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		StringBuilder sb = new StringBuilder();
		N = sc.nextInt(); // 정점 개수
		M = sc.nextInt(); // 간선 개수
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
		visited = new boolean[N + 1];
		res = new int[N + 1];
		
		for(int i = 1; i<=N;i++) {
			res[i] = -1; //방문되지 않은 노드의 깊이는 -1이므로 -1로 초기화 해준다.
		}
		bfs(R);
		for (int i = 1; i <= N; i++) {
			sb.append(res[i] + "\n");
		}
		System.out.println(sb);
	}

	public static void bfs(int r) {
		Queue<Integer> queue = new LinkedList<>();
		visited[r] = true; // 시작 정점 넣어줘
		queue.add(r);
		res[r] = 0; // 배열에 시작 정점 깊이 저장
		int curr = 0; // 탐색 정점 번호 초기화
		while (!queue.isEmpty()) {			
			curr = queue.poll(); // 현재 정점 번호는 curr다. 
			for (int y : arr[curr]) { // 탐색 정점의 인접 정점에 대해서 
				if (!visited[y]) { // 아직 방문하지 않은 인접 정점이라면 
					visited[y] = true; //방문 처리
					queue.add(y);//큐에 넣어
					res[y] = res[curr]+1;// 내 정점(y) 깊이는 나를 불러낸 정점(curr) 깊이 +1이다
				}
			}
		}
	}
}