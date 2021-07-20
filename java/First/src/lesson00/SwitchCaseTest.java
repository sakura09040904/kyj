package lesson00;
import java.util.Scanner;

public class SwitchCaseTest {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		System.out.println("Please input your score:");
		int score = (input.nextInt())/10;
		
		switch(score) {
		case 9:
			System.out.println("Your grade is A");
			break;
		case 8:
			System.out.println("Your grade is B");
			break;
		case 7:
			System.out.println("Your grade is C");
			break;
		case 6:
			System.out.println("Your grade is D");
			break;
			
		}

	}

}
