import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Scanner;

public class Main{
	public static void main(String[] args) throws IOException {
		long start= System.nanoTime();
		Scanner sc = new Scanner(System.in);
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int N = sc.nextInt();
		int[] arr = new int[2000001];
		for(int i = 0; i<N; i++) {
			arr[sc.nextInt()+1000000]++;
		}
		for(int i = 0; i<arr.length;i++) {
			if(arr[i]!=0) {
				bw.write(i-1000000+"\n");
			}
		}bw.flush();
	}
}