package lesson002;

import java.util.LinkedList;
import java.util.List;

public class A02_LinkedList {

	public static void main(String[] args) {
		// LinkedList class를 이용하여 list 생성하기 
        List<Integer> numbers = new LinkedList<>();

        // 리스트에 엘리먼트 추가하기
        numbers.add(1);
        numbers.add(2);
        numbers.add(3);
        System.out.println("List: " + numbers);

        // 리스트의 엘리먼트 액세스
        int number = numbers.get(2); //인덱스2의 값은 3
        System.out.println("Accessed Element: " + number);

        // Using the indexOf() method
        int index = numbers.indexOf(2);  // 값 2의 인덱스는 1
        System.out.println("Position of 2 is " + index);

        // Remove element from the list
        int removedNumber = numbers.remove(1);  // 1번 인덱스의 값 삭제
        System.out.println("Removed Element: " + removedNumber);

	}

}
