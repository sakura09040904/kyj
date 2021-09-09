package lesson001;

public class E009_switchCase {

	public static void main(String[] args) {
		// jobnumber 에 따라 입력, 조회, 수정, 삭제, 종료를 선택하려 할 때
		int jobnumber = 1;
		switch( jobnumber ) {
		case 1:
			System.out.println("입력작업을 수행합니다...");
			break;
		case 2:
			System.out.println("조회작업을 수행합니다...");
			break;
		case 3:
			System.out.println("수정작업을 수행합니다...");
			break;
		case 4:
			System.out.println("삭제작업을 수행합니다...");
			break;
		case 5:
			break;
		default:
			System.out.println("잘못된 선택입니다.");
			break;
		}// end of switch
		
		System.out.println("----------------");
		
		
		int number = 10;

	    // checks if number is greater than 0
	    if (number > 0) {
	      System.out.println("The number is positive.");
	    }
	    
	    // execute this block
	    // if number is not greater than 0
	    else {
	      System.out.println("The number is not positive.");
	    }

	    System.out.println("Statement outside if...else block");

	}// end of main

}// end of class
