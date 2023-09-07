import java.util.Scanner;
import java.util.Stack;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int Jamin = sc.nextInt();
		Stack<Integer> stack = new Stack<>();
		for (int i = 0; i < Jamin; i++) {
			int input = sc.nextInt();
			if (input == 0)
				stack.pop();
			else
				stack.push(input);
		}

		if (stack.isEmpty())
			System.out.println(0);
		else {
			// size 따로 변수 지정해 줘야한다. 안그러면 값이 달라져
			int size = stack.size();
			int sum = 0;
			for (int i = 0; i < size; i++) {
				sum += stack.peek();
				stack.pop();
			}
			System.out.println(sum);
		}
	}
}