import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
	//다음 N 개의 각 줄에는 학생의 성별 S와 학년 Y(1 ≤ Y ≤ 6)가 공백으로 분리되어 주어진다. 
	Scanner sc = new Scanner(System.in);
	//첫 번째 줄에는 수학여행에 참가하는 학생 수를 나타내는 정수 N(1 ≤ N ≤ 1,000)과 
	int N = sc.nextInt();
	//한 방에 배정할 수 있는 최대 인원 수 K(1 < K ≤ 1,000)가 공백으로 분리되어 주어진다. 
	int K = sc.nextInt();
	int[][] counting = new int[7][2];
	for(int i = 0; i<N; i++) {
		//성별 S는 0, 1중 하나로서 여학생인 경우에 0, 남학생인 경우에 1로 나타낸다. 
		int sex = sc.nextInt();
		// 남학생인 경우
		if(sex==1) {
			counting[sc.nextInt()][0]++;
		}else {
			counting[sc.nextInt()][1]++;
		}
	}
//	for(int i = 1; i<=6; i++) {
//		for(int j = 0; j<2; j++) {
//			System.out.print(counting[i][j]+" ");
//		}System.out.println();
//	}
	
	int count = 0;
	for(int i = 1; i<=6; i++) {
		if(counting[i][0]>0&&counting[i][0]<=K) {
			count++;
		}else if(counting[i][0]>K) {
			if(counting[i][0]%K!=0) {
				count=count+(counting[i][0]/K)+1;
			}else if(counting[i][0]%K==0) {
				count=count+(counting[i][0]/K);
			}
		}
		if(counting[i][1]>0&&counting[i][1]<=K) {
			count++;
		}else if(counting[i][1]>K) {
			if(counting[i][1]%K!=0) {
				count=count+(counting[i][1]/K)+1;
			}else if(counting[i][1]%K==0) {
				count=count+(counting[i][1]/K);
			}
		}
	}
	System.out.println(count);
		
	}
}