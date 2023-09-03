import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class Main{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int m = sc.nextInt();
		int n = sc.nextInt();
		isPrime(m, n);
	}
	private static void isPrime(int m, int n) {
		List<Integer> prime = new ArrayList<>(); // 소수 저장할 배열
		boolean[] check = new boolean[1000001]; // 소수인지 체크할 배열	
		
		for(int i = 2; i<=n ;i++) {//m이상 n이하의 소수를 구하는것
			if(check[i]==false) {
				prime.add(i);
				for(int j=i*2; j<=n; j+=i) {//i의 배수에 해당하는 수들을 지우러 가자
					check[j] = true;
				}
			}
			
		}
		for(int a:prime) {
			if(m<=a&&a<=n) {
				System.out.println(a);
			}
		}
	}
}