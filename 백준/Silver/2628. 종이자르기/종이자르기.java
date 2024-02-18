import java.util.Arrays;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		// 종이의 가로
		int row = sc.nextInt();
		// 종이의 세로
		int col = sc.nextInt();
		
		// 점선 입력받을 배열 생성
		int[] rowLine = new int[101];
		rowLine[col]++;
		rowLine[0]++;
		int[] colLine = new int[101];
		colLine[row]++;
		colLine[0]++;
		
		// 점선의 개수
		int N = sc.nextInt();
		for(int i = 0; i<N; i++) {
			// 세로인지 가로인지
			int direction = sc.nextInt();
			// 가로로 자르는 점선
			if(direction==0) {
				rowLine[sc.nextInt()]++;
			// 세로로 자르는 점선
			}else if(direction==1){
				colLine[sc.nextInt()]++;
			}
		}
		int maxRow = 0;
		int maxCol = 0;
		for(int i = 0; i<100; i++) {
			int rowLength = 0;
			int colLength = 0;
			for(int j = i+1; j<101; j++) {
				if(rowLine[i]==1&&rowLine[j]==1) {
					rowLength = j-i;
//					System.out.println(rowLength);
					break;
				}
//				if(colLine[i]==1&&colLine[j]==1) {
//					colLength = j-i;
//					System.out.println(j-i);
//					break;
//				}
			}
			if(maxRow<rowLength) maxRow = rowLength;
//			if(maxCol<colLength) maxCol = colLength;
		}
		for(int i = 0; i<100; i++) {
			int rowLength = 0;
			int colLength = 0;
			for(int j = i+1; j<101; j++) {
//				if(rowLine[i]==1&&rowLine[j]==1) {
//					rowLength = j-i;
//					System.out.println(j-i);
//					break;
//				}
				if(colLine[i]==1&&colLine[j]==1) {
					colLength = j-i;
//					System.out.println(colLength);
					break;
				}
			}
//			if(maxRow<rowLength) maxRow = rowLength;
			if(maxCol<colLength) maxCol = colLength;
		}
		
		System.out.println(maxRow*maxCol);
	}
}