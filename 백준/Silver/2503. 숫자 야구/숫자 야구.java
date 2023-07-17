import java.util.*;

public class Main{
	static int N;
	// 세자리수, 스트라이크, 볼
	static ArrayList<checkBall> checkingBall;
	static int result;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		checkingBall = new ArrayList<>();
		for(int i=0;i<N; i++) {
			int number = sc.nextInt();
			int strike = sc.nextInt();
			int ball = sc.nextInt();
			checkBall Balls = new checkBall(number, strike, ball);
			checkingBall.add(Balls);		
		}
		System.out.println(countAns());
	}
	static int countAns() {
		int result = 0;
		for(int i = 123; i<=987; i++) {
			if(duplication(i))continue;
			int allTest = 0;
			for(int j = 0; j<N; j++) {
				checkBall current = checkingBall.get(j);
				int strikeCnt = 0;
				int ballCnt = 0;
				String curr = Integer.toString(current.number);
				String compare = Integer.toString(i);
				for(int k = 0; k<3; k++) {
					if(curr.charAt(k)==compare.charAt(k)) strikeCnt ++;
				}
				for(int k = 0; k<3; k++) {
					for(int h = 0; h<3; h++) {
						if(k!=h&&curr.charAt(k)==compare.charAt(h)) ballCnt++;
					}
				}
				if(current.strike==strikeCnt && current.ball==ballCnt) {
					allTest++;
				}
			}
			if(allTest == N) {
				result++;
			}			
		}
		return result;
	}
	static boolean duplication(int num) {
		String str = Integer.toString(num);
		if(str.charAt(0)==str.charAt(1)) {
			return true;
		}
		if(str.charAt(1)==str.charAt(2)) {
			return true;
		}
		if(str.charAt(0)==str.charAt(2)) {
			return true;
		}
		if(str.charAt(0)=='0'||str.charAt(1)=='0'||str.charAt(2)=='0') {
			return true;
		}
		return false;
		
	}
	
	// 세자리수, 스트, 볼
	static class checkBall{
		public int number;
		public int strike;
		public int ball;
		
		public checkBall(int number, int strike, int ball) {
			this.number = number;
			this.strike = strike;
			this.ball = ball;
		}
	}
}