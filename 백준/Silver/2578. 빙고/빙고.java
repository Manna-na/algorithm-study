import java.util.Arrays;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		// 먼저 아래와 같이 25개의 칸으로 이루어진 빙고판에 1부터 25까지 자연수를 한 칸에 하나씩 쓴다
		// 차례로 수를 지워가다가 같은 가로줄, 세로줄 또는 대각선 위에 있는 5개의 모든 수가 지워지는 경우 그 줄에 선을 긋는다.
		// 이러한 선이 세 개 이상 그어지는 순간 "빙고"라고 외치는데, 가장 먼저 외치는 사람이 게임의 승자가 된다.

		// 빙고는 5줄
		// 우선 입력부터 받기
		int[][] map = new int[5][5];
		for (int row = 0; row < 5; row++) {
			for (int col = 0; col < 5; col++) {
				map[row][col] = sc.nextInt();
			}
		}
		// 사회자가 부르는 수를 차례로 지워나간다. 예를 들어 5, 10, 7이 불렸다면 이 세 수를 지운 뒤 빙고판의 모습은 다음과 같다

		int res = 0;
		int n = 0;
		while (res < 3) {
			int speak = sc.nextInt();

			for (int row = 0; row < 5; row++) {
				for (int col = 0; col < 5; col++) {
					if (speak == map[row][col]) {
						map[row][col] = 0;

						int count = 0;
						// 좌우에 map[row][c]==0이 있는지 check
						// 만약 map[row][c]==0이 나를 포함해서 5개 있으면 그건 빙고
						for (int c = 0; c < 5; c++) {
							if (map[row][c] == 0) {
								count++;
							}

						}
						if (count == 5) {
							res++;
//							System.out.println("1. row는 " + row + " col은 " + col + " 값은 " + speak);
						}
						count = 0;

						// 상하로 map[r][col]==0이 있는지 check
						// 만약 map[row][col]==0이 나를 포함해서 5개 있으면 그건 빙고
						for (int r = 0; r < 5; r++) {
							if (map[r][col] == 0) {
								count++;
							}
						}
						if (count == 5) {
							res++;
//							System.out.println("2. row는 " + row + " col은 " + col + " 값은 " + speak);
						}
						count = 0;

						// 오른쪽 아래로 내려가는 대각선에 걸리는 수
						if (row == col) {

							// 오른쪽 아래로 내려가는 대각선
							for (int i = 0; i < 5; i++) {
								if (map[i][i] == 0) {
									count++;
								}
							}
							if (count == 5) {
								res++;
//								System.out.println("3. row는 " + row + " col은 " + col + " 값은 " + speak);

							}
						}
						count = 0;
						// 왼쪽 아래로 내려가는 대각선에 위치한 좌표
						if (col + row == 4) {

							// 왼쪽 아래로 내려가는 대각선
							for (int i = 4; i >= 0; i--) {
								if (map[i][4 - i] == 0) {
									count++;
								}
							}
							if (count == 5) {
								res++;
//								System.out.println("4. row는 " + row + " col은 " + col + " 값은 " + speak);
							}

						}
						count = 0;

					}
				}
			}

			n++;

		}

		System.out.println(n);
	}
}