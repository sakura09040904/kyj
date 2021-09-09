package lesson002;
/*
 * 리스트 인터페이스를 구현하는 클래스들 :
 *  ArrayList, LinkedList, Vector, Stack
 *  
 *  자주 사용하는 리스트 인터페이스 메서드
 *  add() - 리스트에 엘리먼트 추가
 *  addAll() - 임의 리스트의 모든 요소를 다른 리스트에 추가
 *  get() - 리스트의 임의 요소에 접근
 *  iterator() - returns iterator object that can be used to 
 *               sequentially access elements of lists
 *  set() - changes elements of lists
 *  remove() - removes an element from the list
 *  removeAll() - removes all the elements from the list
 *  clear() - removes all the elements from the list 
 *            (more efficient than removeAll())
 *  size() - returns the length of lists
 *  toArray() - converts a list into an array
 *  contains() - returns true if a list contains specified element
 */

import java.util.ArrayList;
import java.util.List;


public class A01_ArrayList {

	public static void main(String[] args) {
		
		// List의 구현
		List<Integer> numbers = new ArrayList<>();

		// 
		System.out.println("Init List : " + numbers);
		
		// 리스트에 값 추가하기
        numbers.add(1);
        numbers.add(2);
        numbers.add(3);
        System.out.println("List: " + numbers);

        // 인덱스를 사용하여 리스트 엘리먼트에 접근 
        int number = numbers.get(2);
        System.out.println("Accessed Element: " + number);

        // 인덱스를 사용하여 리스트의 엘리먼트 삭제
        int removedNumber = numbers.remove(1);
        System.out.println("Removed Element: " + removedNumber);

	}

}
