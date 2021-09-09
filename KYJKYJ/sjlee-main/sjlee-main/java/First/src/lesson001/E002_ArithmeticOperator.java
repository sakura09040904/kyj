package lesson001;

public class E002_ArithmeticOperator {

	public static void main(String[] args) {

	    // declare variables
	    int a = 12, b = 5;

	    // addition operator
	    System.out.println("a + b = " + (a + b));

	    // subtraction operator
	    System.out.println("a - b = " + (a - b));

	    // multiplication operator
	    System.out.println("a * b = " + (a * b));

	    // division operator
	    System.out.println("a / b = " + (a / b));

	    // modulo operator
	    System.out.println("a % b = " + (a % b));
	    
	    
	    System.out.println("=======================");
	    
	    System.out.println(9 / 2);    // 정수와 정수연산의 결과는 정수
	    System.out.println(9.0 / 2);  // 실수와 정수연산의 결과는 실수
	    System.out.println(9 / 2.0);  // 
	    System.out.println(9.0 / 2.0);// 실수끼리 연산결과는 실수
	}

}
