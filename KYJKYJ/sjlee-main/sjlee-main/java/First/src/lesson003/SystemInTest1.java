package lesson003;

import java.io.IOException;

public class SystemInTest1 {

	public static void main(String[] args) {
		int i;
		
		// 입력 받기
		try {
			System.out.println("문자를 입력주세요.");
			i = System.in.read();
			System.out.println(i);
			System.out.println((char)(i-32));
		} catch (IOException e) {
			// TODO: handle exception
			e.printStackTrace();
			System.out.println("입력 오류가 발생하였습니다.");
		}// end of try catch
		
		System.out.println("프로그램 종료...");
	}//end of main
}//end of class
