package lesson001;

public class E008_ifelseif {

	public static void main(String[] args) {
		// 세개 이상의 선택을 비교해야할 때
		int score = 75;
		
		if(score >= 90 ) {
			System.out.println("A");
		}else if (score >= 80) {
			System.out.println("B");
		}else if(score >= 70) {
			System.out.println("C");
		}else if(score >= 60) {
			System.out.println("D");
		}else {
			System.out.println("F");
		}
		
		System.out.println("프로그램 종료...");

	}

}
