import java.util.Scanner;
import java.util.Stack;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		int cnt=0;
		for (int t = 0; t < T; t++) {
			Stack<Character> stack = new Stack<>();
			String str = sc.next(); 
			stack.add(str.charAt(0));
//			System.out.println(stack.peek());
			for (int i = 1; i < str.length(); i++) {
//				stack.add(str.charAt(i));
				if (!stack.isEmpty()&&str.charAt(i)==stack.peek()) {
					stack.pop();
				} else {
					stack.add(str.charAt(i));
				}
			}if(stack.isEmpty())cnt+=1;
		}
		System.out.println(cnt);
	}

}