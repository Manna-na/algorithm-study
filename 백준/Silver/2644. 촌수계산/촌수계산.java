import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

class Main {
	// bfs 문제?
	static ArrayList<Integer>[] graph;
	static int N, M, cnt;
	static boolean[] visited;
	static int[] depth;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt(); // 노드 수
		int start = sc.nextInt();
		int end = sc.nextInt();
		M = sc.nextInt(); //간선의 수
		graph = new ArrayList[N+1];
		for(int i = 1; i<graph.length; i++) {
			graph[i] = new ArrayList<>();
		}
		
		for(int i = 0; i<M; i++) {
			int u = sc.nextInt();
			int v = sc.nextInt();
			graph[u].add(v);
			graph[v].add(u);
		}
		
		for(int i = 1; i<graph.length; i++) {
			Collections.sort(graph[i]);
		}
		visited = new boolean[N+1];
		depth = new int[N+1];
		Arrays.fill(depth, -1);
		bfs(start, end);
		System.out.println(depth[end]);
		
		
		
		
	}
	private static void bfs(int start, int end) {
		Queue<Integer> q=new LinkedList<>();
		visited[start] = true;
		q.add(start);	
		depth[start]=0;
		
		while(!q.isEmpty()) {
			int curr = q.poll();
//			System.out.print(curr+" ");
			for(int c : graph[curr]) {

				if(!visited[c]) {
					visited[c] = true;
					q.add(c);
					depth[c] = depth[curr]+1;
				}
			}
		}		
	}
	
	
	
	
}