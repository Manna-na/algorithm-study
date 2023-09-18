import java.util.Arrays;
import java.util.Scanner;

public class Main {
	static int[] arr;
	static int N, M;
	static int[] result;
	static boolean[] visited;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();
		arr = new int[N];
		result = new int[M];
		visited = new boolean[N];
		for (int i = 0; i < N; i++) {
			arr[i] = i+1;
		}
		perm(0);
	}
	
	
	
	public static void perm(int idx) {
		// 기저조건 : 만약 idx 끝까지 다 돌았으면 출력하고 끝내기
		if(idx==M) {
			for(int i = 0; i<M; i++) {
				System.out.print(result[i]+" ");
			}System.out.println();
			return; // 나를 부른 곳에 다시 가자
		}
		
		// idx : 내가 현재 보고 있는 값
		// 전체 요소 돌아봐야 해
		for(int i = 0; i<N; i++) {
			//바보야... 이미 숫자를 썼으면 그건 안보고 지나가야지? 
			if(visited[i]) continue;
			
			result[idx]=arr[i];
			visited[i] = true;
			perm(idx+1);
			visited[i] = false;
			
		}
		
	}

}