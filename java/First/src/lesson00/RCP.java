package lesson00;

import java.util.Scanner;
import java.util.Random;

public class RCP {

	public static void main(String[] args) {

		int i=0;
		int win=0,lose=0,same=0;

		while(i<10) {
			Scanner sc = new Scanner(System.in);
			System.out.println("Please input R/C/P");
			System.out.println("R:1, C:2, P:3");
			int me = sc.nextInt();

			Random random = new Random();
			int pc = ((random.nextInt(100))%3)+1;

			if(me == pc) {
				System.out.println("You are same with pc");
				same++;
			}
			else {
				switch(me) {
				case 1:
					if(pc==2) {
						System.out.println("You are R, pc is C. You win!");
						win++;
					}
					else {
						System.out.println("You are R, pc is P. You lose!");
						lose++;
					}
					break;
				case 2:
					if(pc==1) {
						System.out.println("You are C, pc is R. You lose!");
						lose++;
					}
					else {
						System.out.println("You are C, pc is P. You win!");
						win++;
					}
					break;
				case 3:
					if(pc==1) {
						System.out.println("You are P, pc is R. You win!");
						win++;
					}
					else {
						System.out.println("You are P, pc is C. You lose!");
						lose++;
					}
					break;
				}
			}
			i++;
		}
		System.out.printf("Total is %d, win is %d, lose is %d, same is %d",i, win, lose, same);
	}

}
