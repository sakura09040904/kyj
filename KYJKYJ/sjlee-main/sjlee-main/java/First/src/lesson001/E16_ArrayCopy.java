package lesson001;

import java.util.Arrays;

public class E16_ArrayCopy {

	public static void main(String[] args) {
		
		int [] numbers = {1, 2, 3, 4, 5, 6};
		
		// 방법 1. shalow copy : 얕은 복사
		int [] positiveNumbers = numbers;    // copying arrays

		for (int number: positiveNumbers) {
			System.out.print(number + ", ");
		}
		System.out.println();
		System.out.println("numbers : " + numbers);
		System.out.println("positiveNumbers : " + positiveNumbers);
		
		// 방법 2. deep copy : 깊은 복사
		int [] source = {1, 2, 3, 4, 5, 6};
        int [] destination = new int[6];

        // iterate and copy elements from source to destination
        for (int i = 0; i < source.length; ++i) {
            destination[i] = source[i];
        }
        System.out.println("source.....");
        System.out.println(source);
        System.out.println(Arrays.toString(source));
        
        System.out.println("destination.....");
        System.out.println(destination);
        System.out.println(Arrays.toString(destination));
        
        destination[0] = 1000;
        System.out.println("변경후 두 배열값 비교...");
        System.out.println(Arrays.toString(source));
        System.out.println(Arrays.toString(destination));
        
        
        // 방법 3. arraycopy() 사용
        int[] n1 = {2, 3, 12, 4, 12, -2};
        int[] n3 = new int[5];

        // Creating n2 array of having length of n1 array
        int[] n2 = new int[n1.length];
      
        // copying entire n1 array to n2
        System.arraycopy(n1, 0, n2, 0, n1.length);
        System.out.println("n2 = " + Arrays.toString(n2));  
      
        // copying elements from index 2 on n1 array
        // copying element to index 1 of n3 array
        // 2 elements will be copied
        System.arraycopy(n1, 2, n3, 1, 2);
        System.out.println("n3 = " + Arrays.toString(n3));  
        
	}// end of main

}//end of class
