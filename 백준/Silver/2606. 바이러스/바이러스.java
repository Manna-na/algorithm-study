import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

class Main{
	// bfs 문제네요
	static int N, V, cnt;
	static ArrayList<Integer>[] graph;
	static boolean[] visited;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt(); //컴퓨터의 수
		V = sc.nextInt(); //네트워크상 연결된 컴퓨터 쌍의 수? 뭐 걍 간선의 수지
		
		graph = new ArrayList[N+1];
		for(int i = 0; i<graph.length; i++) {
			graph[i] = new ArrayList<>();
		}
		
		for(int i =0;i<V; i++) {
			int u = sc.nextInt();
			int v = sc.nextInt();
			
			graph[u].add(v);
			graph[v].add(u);
		}
		visited = new boolean[N+1];
		cnt = 0;
		bfs(1);
		System.out.println(cnt-1);
	}
	private static void bfs(int r) {
		Queue<Integer> q = new LinkedList<>();
		visited[r] = true;
		q.add(r);
		while(!q.isEmpty()) {
			int curr = q.poll();
			cnt++;
			for(int c : graph[curr]) {
				if(!visited[c]) {
					visited[c] = true;
					q.add(c);
					
				}
			}
		}
	}
}