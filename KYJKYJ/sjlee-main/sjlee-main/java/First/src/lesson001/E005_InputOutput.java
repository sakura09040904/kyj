package lesson001;

import java.util.Scanner;

public class E005_InputOutput {

	public static void main(String[] args) {
		// 자바의 출력문
		// System.out.println(); or
		// System.out.print(); or
		// System.out.printf();
		
		System.out.println("println");// 행단위 출력
		System.out.println("println");// 행단위 출력
		
		System.out.print("print\t");
		System.out.print("print\n");
		
		System.out.printf("%d\n", 10);
		System.out.printf("값 %d\n", 10);
		
		System.out.println("hello" + " java");
		
		
		
		//============  Input Statement
		// create an object of Scanner
		// 클래스(타입) 객체참조변수 = new 클래스생성자()
		Scanner input = new Scanner(System.in);

		// take input from the user
		System.out.println("정수형 데이터를 입력해주세요. ");
		int number = input.nextInt();
		
		input.nextLine(); // 개행문자 제거용 
		
		System.out.println("이름을 입력해주세요.");
		String name = input.nextLine();
		
		System.out.printf("숫자 : %d, 이름 : %s\n", number, name);
		
		input.close();   // resource 반납
		
	}

}
