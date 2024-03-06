import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[][] map = new int[101][101];
		for (int i = 0; i < 4; i++) {
			int lx = sc.nextInt();
			int ly = sc.nextInt();
			int rx = sc.nextInt();
			int ry = sc.nextInt();

			for (int row = ly; row < ry; row++) {
				for (int col = lx; col < rx; col++) {
					map[row][col] = 1;
				}
			}
		}
		int sum = 0;
		for (int row = 0; row < map.length; row++) {
			for (int col = 0; col < map.length; col++) {
//				System.out.print(map[row][col]);
				sum+=map[row][col];
			}
//			System.out.println();
		}
		System.out.println(sum);
	}
}