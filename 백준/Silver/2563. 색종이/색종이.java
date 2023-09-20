import java.util.Scanner;

public class Main{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int testCase = sc.nextInt();
		boolean[][] map = new boolean[100][100];		
		for(int tc=0; tc<testCase; tc++) {
			int col = sc.nextInt();
			int row = sc.nextInt();
			for(int r = row; r<row+10; r++) {
				for(int c = col; c<col+10; c++) {
					if(map[r][c]==true)map[r][c]=true;
					else map[r][c]=true;
				}
			}
		}
		int count = 0;
		for(int r=0;r<100;r++) {
			for(int c = 0; c<100; c++) {
				if(map[r][c]==true)count++;
			}
		}
		System.out.println(count);

	}
}