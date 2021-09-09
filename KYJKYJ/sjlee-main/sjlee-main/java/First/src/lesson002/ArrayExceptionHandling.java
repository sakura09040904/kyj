package lesson002;

import java.sql.SQLException;

public class ArrayExceptionHandling {

	public static void main(String[] args) {
		// try catch 구문을 이용한 예외처리
		
		int[] arr = new int[5];
		
		try {
			for(int i = 0; i <= 5 ; i++) {
				arr[i] = i;
				System.out.println(arr[i]);
			}
		} catch (ArrayIndexOutOfBoundsException e) {
			// TODO: handle exception
			System.out.println("인덱스가 범위를 벗어났습니다.");
			e.printStackTrace();
		} //end of catch(Exception e)
				
		System.out.println("프로그램 종료");

	}//end of main

}//end of class
