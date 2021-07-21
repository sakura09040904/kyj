package lesson01;

import java.util.LinkedList;

public class LinkedListTest {

	public static void main(String[] args) {
		LinkedList<String> myList = new LinkedList<String>();
 
		myList.add("A");
		myList.add("B");
		myList.add("C");
		
		System.out.println(myList);
		
		myList.add(1, "D");
		System.out.println(myList);
		
		myList.addFirst("0");
		System.out.println(myList);
		
		//removeLast(); 마지막 값을 제거하고 해당 값을 반환
		System.out.println(myList.removeLast()); 
		System.out.println(myList);
		
	}

}
