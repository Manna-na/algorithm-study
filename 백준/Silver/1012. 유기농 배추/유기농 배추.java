import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

// 이거 왜 방문처리로 하면 안되는거야?
class pair {
	int x, y;

	public pair(int x, int y) {
		this.x = x;
		this.y = y;
	}

}

public class Main {
	static int N, M, K;
	static int[][] map;
	static boolean[][] visited;
	static int[] dr = new int[] { -1, 1, 0, 0 };
	static int[] dc = new int[] { 0, 0, -1, 1 };

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for (int tc = 0; tc < T; tc++) {
			M = sc.nextInt();// 배추밭 가로길이
			N = sc.nextInt();// 배추밭 세로길이
			K = sc.nextInt();
			map = new int[N][M];
			for (int i = 0; i < K; i++) {
				int col = sc.nextInt();
				int row = sc.nextInt();
				map[row][col] = 1;
			}
			visited = new boolean[N][M];
			bfs();
		}

	}

	private static void bfs() {
		Queue<pair> q = new LinkedList<>();
		int cnt = 0;
		for (int row = 0; row < N; row++) {
			for (int col = 0; col < M; col++) {
				if (map[row][col] == 1) {
//					visited[row][col] = true;
					map[row][col] = 2;
					q.add(new pair(row, col));
					while (!q.isEmpty()) {
						pair p = q.poll();
						int a = p.x;
						int b = p.y;
						for (int d = 0; d < 4; d++) {
							int rr = a + dr[d];
							int cc = b + dc[d];
							if (rr < N && cc < M && rr >= 0 && cc >= 0) {
//								if (!visited[rr][cc] && map[rr][cc] == 1) {
								if (map[rr][cc] == 1) {
									// visited[rr][cc] = true;
									q.add(new pair(rr, cc));
									map[rr][cc] = 2;

								}
							}
						}

					}
					cnt++;

				}
			}
		}
		System.out.println(cnt);

	}

}