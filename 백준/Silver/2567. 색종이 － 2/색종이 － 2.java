import java.util.Arrays;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		// 첫째 줄에 색종이의 수가 주어진다, 색종이의 수는 100이하이다.
		int N = sc.nextInt();
		// 가로, 세로의 크기가 각각 1--인 정사각형 모양의 흰색 도화지
		int[][] map = new int[101][101];
		for(int i = 0; i<N; i++) {
			int lx = sc.nextInt();
			int ly = sc.nextInt();
			for(int row = ly; row<ly+10; row++) {
				for(int col = lx; col < lx+10;col++) {
					map[row][col]=1;
				}
			}
		}
//		for(int row = 0; row<24;row++) {
//			for(int col = 0; col<25; col++) {
//				System.out.print(map[row][col]+" ");
//			}System.out.println();
//		}
//		
		// 델타 탐색 
		// 상 하 좌 우 좌상 좌하 우상 우하 
		// 8방탐색을 할 필요가 없어요
		// 꼭지점은 고려해줄 필요가 없어요
		// 아아아아아아아아안아아아아
		int[] dr = {-1, 1, 0, 0};
		int[] dc = {0, 0, -1, 1};
		int count = 0;
		// 만약 답이 맞으면 row와 col의 범위 바꿔줘야해 101로
		for(int row = 0; row<101; row++) {
			for(int col = 0; col<101; col++) {
				if(map[row][col]==1) {
					for(int d =0;d<4;d++) {
						// 델타 탐색 위한 임시행과 임시열 만들기
						int rr = row+dr[d];
						int cc = col+dc[d];
						if(rr>=0&&cc>=0&&rr<102&&cc<102&&map[rr][cc]==0) {
							count++;
//							break;
						}
					}
					
				}
			}
		}
		System.out.println(count);
	}
}