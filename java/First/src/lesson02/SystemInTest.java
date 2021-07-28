package lesson02;

import java.io.IOException;

public class SystemInTest {

	public static void main(String[] args) {
		int i;
		
		try {
			System.out.print("Input a Alpabet: ");
			i = System.in.read();
			System.out.println(i);
			System.out.println((char)i);
		} catch (IOException e) {
			e.printStackTrace();
			System.out.println("Input Error");
		} System.out.println("Program1 is ended");
		
		
		int j;
		System.out.print("Input a word (Quit: Ctrl+z): ");
		try {
			while((j=System.in.read()) != -1) {
				System.out.print(((char)j));
			}
			System.out.println();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			System.out.println("Input Error");
		} System.out.println("Program2 is ended");
		System.exit(0);
	}

}
