package lesson01;

// ctrl+space bar : 앞의 키워드를 보고 완성시켜줌
// (sysout : ctrl+space bar)
// (try: ctrl+space bar)

public class HandlingException {
	
	public static void main(String[] args) {
		
		// Array Exception Handling
		int[] arr = new int[5];
		try {
			for(int i=0; i<=5; i++) {
				arr[i] = i;
				System.out.println(i);
			}
		} catch (ArrayIndexOutOfBoundsException e) {
			System.out.println("배열의 범위를 벗어났습니다.");
			e.printStackTrace(); // 오류가 난 부분을 찾아냄
		}
		
		System.out.println("프로그램 종료");
		
		// 
		
	}
	
}
