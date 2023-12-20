
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N= sc.nextInt();
		int[][] size = new int[N][2];
		for(int row = 0; row<N; row++) {
			for(int col = 0;col<2;col++) {
				size[row][col] = sc.nextInt();
			}
		}
		int height = 0;
		int weight = 0;
		int[] ranking = new int[N];
		for(int i = 0; i<N; i++) {
			int rank = 1;     
			for(int j =0; j<N; j++) {
				if(size[i][0]<size[j][0]&&size[i][1]<size[j][1]) rank++;
			}
			System.out.print(rank+" ");
		}
		
	}

}
