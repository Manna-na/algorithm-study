import java.util.Arrays;
import java.util.Scanner;

class Main {
	public static void main(String[] args) {
		// N은 1 이상 1000이하
		Scanner sc = new Scanner(System.in);

		// N은 딱지놀이의 총 라운드 수를 나타낸다.
		int N = sc.nextInt();
		for (int n = 1; n <= N; n++) {
			// 어린이 A가 내는 딱지에 나온 그림의 총 개수 a개
			// 1 4
			// 어린이 A는 1개 내고 그림의 값은 4
			// 어린이 B가 내는 딱지에 나온 그림의 총 개수 b개
			// 4 3 3 2 1
			// 어린이 B는 4개 내고 그림의 값은 3 3 2 1개
			int[] countingA = new int[5];
			int[] countingB = new int[5];

			int count = sc.nextInt();
			for (int i = 0; i < count; i++) {
				countingA[sc.nextInt()]++;
			}

//				System.out.println(Arrays.toString(countingA));
//				System.out.println(findMax(countingA));
//				System.out.println(sum(countingA));
			count = sc.nextInt();
			for (int i = 0; i < count; i++) {
				countingB[sc.nextInt()]++;
			}
//				System.out.println(Arrays.toString(countingB));
//				System.out.println(findMax(countingB));
//				System.out.println(sum(countingB));

//			System.out.println(Arrays.toString(countingA));
//			System.out.println(Arrays.toString(countingB));
//			System.out.println(findMax(countingA));
//			System.out.println(findMax(countingB));
//			System.out.println(sum(countingA));
//			System.out.println(sum(countingB));
			
			
			if(countingA[4]>countingB[4]) {
				System.out.println("A");
			}else if(countingA[4]<countingB[4]) {
				System.out.println("B");
			}else {
				if(countingA[3]>countingB[3]) {
					System.out.println("A");
				}else if(countingA[3]<countingB[3]) {
					System.out.println("B");
				}else {
					if(countingA[2]>countingB[2]) {
						System.out.println("A");
					}else if(countingA[2]<countingB[2]) {
						System.out.println("B");
					}else {
						if(countingA[1]>countingB[1]) {
							System.out.println("A");
						}else if(countingA[1]<countingB[1]) {
							System.out.println("B");
						}else {
							System.out.println("D");
						}
				
					}
				}
			}

//			if (findMax(countingA) > findMax(countingB)) {
//				System.out.println("A");
//			} else if (findMax(countingA) < findMax(countingB)) {
//				System.out.println("B");
//			} else if (findMax(countingA) == findMax(countingB)) {
//				if (sum(countingA) > sum(countingB)) {
//					System.out.println("A");
//				} else if (sum(countingA) < sum(countingB)) {
//					System.out.println("B");
//				} else if (sum(countingA) == sum(countingB)) {
//					System.out.println("B");
//				}
//			}
		}
	}

	public static int findMax(int[] counting) {
		int max = -1;
		int maxIdx = -1;
		for (int i = 0; i < counting.length; i++) {
			if (max < counting[i]) {
				max = counting[i];
				maxIdx = i;
			} else if (max == counting[i]) {
				if (maxIdx < i) {
					maxIdx = i;
				}
			}
		}
		return maxIdx;
	}

	public static int sum(int[] counting) {
		int sumNum = 0;
		for (int i = 0; i < counting.length; i++) {
			sumNum += counting[i]*i;
		}
		return sumNum;
	}
}