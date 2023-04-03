package Tree;

import java.util.Scanner;

public class SWEA5207 {
	static int N;
	static int M;
	static int[] A;
	static int[] B;
	static int[] check;
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for (int tc = 1; tc <= T; tc++) {
			N = sc.nextInt();
			M = sc.nextInt();
			A = new int[N];
			check = new int[1000001];
			for (int i = 0; i<N; i++) {
				A[i] = sc.nextInt();
			}
			B = new int[M];
			for (int i = 0; i<M; i++) {
				B[i] = sc.nextInt();
			}
			BinarySearch(0,N-1,"none");
			int answer = 0;
			for (int b : B) {
				if (check[b]==1) {
					answer += 1;
				}
			}
			System.out.printf("#%d %d",tc,answer);
		}
	}
	public static void BinarySearch(int start, int end, String before) {
		if (start > end) {
			return;
		}
		int middle = (start+end)/2;
		check[A[middle]] = 1;
		if (before != "left") {
			BinarySearch(start,middle-1,"left");
		}
		if (before != "right") {
			BinarySearch(middle+1,end,"right");
		}
	}
	
}
