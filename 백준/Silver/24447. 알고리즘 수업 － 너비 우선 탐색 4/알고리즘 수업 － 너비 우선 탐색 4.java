import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

class Main{
	static ArrayList<Integer>[] graph;
	static long[] result, meeting;
	static boolean[] visited;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt(); //정점의 수
		int M = sc.nextInt(); //간선의 수
		int R = sc.nextInt(); //시작 정점
		
		graph = new ArrayList[N+1];
		for(int i = 1; i<graph.length; i++) {
			graph[i] = new ArrayList<>();
		}
		result = new long[N+1];
		meeting = new long[N+1];
		Arrays.fill(result, -1);
		for(int i = 0; i<M; i++) {
			int u = sc.nextInt(); // 정점
			int v = sc.nextInt(); // 정점
			
			graph[u].add(v); //양방향 그래프
			graph[v].add(u);
		}
		for(int i =1;i<=N;i++) {
			Collections.sort(graph[i]);
		}
		visited = new boolean[N+1];
		bfs(R);
//		System.out.println(Arrays.toString(result));
//		System.out.println(Arrays.toString(meeting));
		long sum = 0;
		for(int i =1;i<=N; i++) {
			sum += result[i]*meeting[i];
		}
		System.out.println(sum);
	}
	private static void bfs(int r) {
		Queue<Integer> q = new LinkedList<>();
		visited[r] = true;
		result[r]= 0;
		q.add(r);
		int index=1;
//		int curr = 0; //탐색 정점을 0으로 설정해야하는 이유는..?
		while(!q.isEmpty()) {
			int curr = q.poll();
			meeting[curr]=index++;
			// 탐색 정점의 인접 정점을 모두 탐색해야한다.
			for(int c : graph[curr]) {
				if(!visited[c]) {
					visited[c] = true;
					q.add(c);
					result[c] = result[curr]+1;
				}
			}
		}
		
	}
}