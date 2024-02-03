import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

class Main{
	static ArrayList<Integer>[] graph;
	static int N, M, R;
	static boolean[] visited;
	static long[] depth, result;
	static int index;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();
		R = sc.nextInt();
		
		graph = new ArrayList[N+1];
		for(int i = 1;i<graph.length; i++) {
			graph[i] = new ArrayList<>();
		}
		depth = new long[N+1];
		result = new long[N+1];
		Arrays.fill(depth, -1);
		for(int i =0;i<M;i++) {
			int u = sc.nextInt();
			int v = sc.nextInt();
			graph[u].add(v);
			graph[v].add(u);
		}
		for(int i = 1; i<graph.length; i++) {
			Collections.sort(graph[i]);
		}
		visited = new boolean[N+1];
		depth[R] = 0; // 재귀 돌리는 거여서 dfs 함수 내에다가 선언하면 안되는...?
		index = 1;
		dfs(R);
//		System.out.println(Arrays.toString(depth));
//		System.out.println(Arrays.toString(result));
		long sum = 0;
		for(int i=1;i<=N;i++) {
			sum+=result[i]*depth[i];
		}
		System.out.println(sum);
	
	}
	private static void dfs(int r) {
		visited[r]= true;
//		result[index++] = r;
		result[r] = index++; //정점 방문 순서 배열
		for(int c : graph[r]){
			//r의 인접 노드
			if(!visited[c]) {
				depth[c] = depth[r]+1; // 현재 나의 깊이는 내 이전 깊이+1이지
				dfs(c);
			}
		}
	}
}