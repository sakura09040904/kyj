package lesson002;

import java.util.Stack;

public class EStackTest {

	public static void main(String[] args) {
		Stack<String> stack = new Stack<String>();
		
		stack.add("java");
		stack.add("python");
		stack.add("funny");
		
		System.out.println("origin stack : " + stack);
		
		String temp = stack.peek();
		System.out.println(temp);
		System.out.println("stack after peek() : " + stack);
		
		// search() : 값을 찾아 위치값(1 base)을 반환
		int idx = stack.search("python");
		System.out.println("idx of python  :  " + idx);
		
		
		temp = stack.pop();
		System.out.println(temp);
		System.out.println("stack after pop() : " + stack);
		
		
		idx = stack.search("python");
		System.out.println("idx of python  :  " + idx);

	}

}
