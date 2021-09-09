package lesson002;

import java.util.LinkedList;

public class LinkedListTest {

	public static void main(String[] args) {
		// LinkedList의 이해와 활용
		// String타입의 LinkedList 생성
		LinkedList<String> myList = new LinkedList<String>();
		
		myList.add("A");
		myList.add("B");
		myList.add("C");
		System.out.println("--- A,B,C 추가 후 전체 출력");
		System.out.println(myList);
		
		myList.add(1, "D"); // 인덱스 1 위치에 D추가
		System.out.println("--- D 추가 후 전체 출력");
		System.out.println(myList);
		
		myList.addFirst("0");
		System.out.println("--- 맨 앞에 0 추가 후 전체 출력");
		System.out.println(myList);
		
		myList.removeLast();
		System.out.println("--- 맨 뒤의 요소 삭제 후 전체 출력");
		System.out.println(myList);
		
	}// end of main
}// end of class