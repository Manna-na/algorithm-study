import java.util.Arrays;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		// 스위치 개수는 100이하인 양의 정수
		int switchNum = sc.nextInt();
		// 스위치 상태 배열
		// 1은 켜진 것, 0은 꺼진 것
		int[] switchArr = new int[switchNum + 1];
		for (int s = 1; s < switchNum + 1; s++) {
			switchArr[s] = sc.nextInt();
		}
//		System.out.println(Arrays.toString(switchArr));
		// 학생수는 100이하인 양의 정수
		int student = sc.nextInt();

		for (int s = 0; s < student; s++) {
			// 한학생의 성별, 학생이 받은 수
			int sex = sc.nextInt();
			// 학생이 받은 수
			int n = sc.nextInt();
			// 이건 남자
			if (sex == 1) {
				for (int i = 1; i < switchArr.length; i++) {
					if (i % n == 0)
						switchArr[i] = Math.abs(switchArr[i] - 1);
				}
//				System.out.println(Arrays.toString(switchArr));
			} // 이건 여자
			else {
				for (int i = 1; i < switchArr.length; i++) {
					// 여학생은 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아서, 그 구간에
					// 속한 스위치의 상태를 모두 바꾼다.
					if (n == i) {
						switchArr[n] = Math.abs(switchArr[i] - 1);
						for (int a = 1; a <= n - 1; a++) {
							if ((n - a) >= 0 && (n + a) <= switchNum&&switchArr[n - a] == switchArr[n + a]) {
									switchArr[n - a] = Math.abs(switchArr[n - a] - 1);
									switchArr[n + a] = Math.abs(switchArr[n + a] - 1);
									


							}else break;

						}
					}
//					System.out.println(Arrays.toString(switchArr));
				}

			}

		}
		for (int res = 1; res < switchArr.length; res++) {
			if (res == 21 || res == 41 || res == 61 || res == 81) {
				System.out.println();
				System.out.print(switchArr[res] + " ");
			} else {
				System.out.print(switchArr[res] + " ");

			}
		}

	}
}