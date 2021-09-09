package lesson001;

public class E011_forStmt {

	public static void main(String[] args) {
		int sum = 0;
	    int n = 1000;

	    // for loop  (초기식 i=1; 테스트식 i <= n; i를 1씩 증가하며)
	    for (int i = 1; i <= n; ++i) {
	      // body inside for loop
	      sum += i;     // sum = sum + i
	    }
	       
	    System.out.println("Sum = " + sum);
	}

}
