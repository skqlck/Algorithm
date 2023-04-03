package Backtracking;

import java.util.Scanner;

public class SWEA1952 {
	static int[] prices = new int[4];
	static int[] days = new int[14];
	static int answer;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for (int tc = 1; tc <= T; tc++) {
			for (int i = 0; i < 4; i++) {
				prices[i] = sc.nextInt();
			}
			for (int i = 1; i < 13; i++) {
				days[i] = sc.nextInt();
			}
			answer = prices[3];
			Backtracking(1,0);
			System.out.printf("#%d %d\n",tc,answer);
		}
	}
	
	public static void Backtracking(int month, int totalPrice) {
		if (answer < totalPrice) {
			return;
		}
		if (month == 13) {
			if (answer > totalPrice) {
				answer =totalPrice;
			}
			return;
		}
		if (prices[0]*days[month] < prices[1]) {
			Backtracking(month+1,totalPrice+prices[0]*days[month]);
		}
		else {
			Backtracking(month+1,totalPrice+prices[1]);
		}
		
		if (month <= 10) {
			Backtracking(month+3,totalPrice+prices[2]);
		}
	}
}
