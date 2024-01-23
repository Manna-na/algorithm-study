import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int x = sc.nextInt();
		int y = sc.nextInt();
		int w = sc.nextInt();
		int h = sc.nextInt();
		int[] arr = { x, y, w, h };
		int min = arr[0];
		for (int i = 0; i < arr.length - 1; i++) {
			for (int j = i + 1; j < arr.length; j++) {
				if (arr[j] < min) {
					min = arr[j];

				}
			}
		}
		if (w - x < h - y) {
			if (w - x < min) {
				System.out.println(w - x);
			} else {
				System.out.println(min);
			}
		} else {
			if (h - y < min) {
				System.out.println(h - y);
			} else {
				System.out.println(min);
			}
		}

	}
}
