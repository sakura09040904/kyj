package lesson01;
import java.util.ArrayList;

class MyStack {
	
	private ArrayList<String> myStack = new ArrayList<String>();
	
	public void push(String data) {
		myStack.add(data);
	}
	
	public String pop() {
		int len = myStack.size();
		if(len==0) {
			System.out.println("Stack is Empty");
			return null;
		}
		return myStack.remove(len-1);
	}
	
	public void showInfo() {
		for(String data:myStack) {
			System.out.print(data);
		}System.out.println();
	}
}

class MyQue{
	
	private ArrayList<String> myQue = new ArrayList<String>();
	
	public void push(String data) {
		myQue.add(data);
	}
	
	public String deQue() {
		int len = myQue.size();
		if(len==0) {
			System.out.println("Que is Empty");
			return null;
		}
		return myQue.remove(0);
	}
	
	public void showInfo() {
		for(String data:myQue) {
			System.out.print(data);
		}System.out.println();
	}
	
	
}

public class MyStackTest {

	public static void main(String[] args) {
		MyStack stack = new MyStack();
		
		stack.push("A");
		stack.push("B");
		stack.push("C");
		stack.push("D");
		stack.showInfo();
		
		System.out.println("1st:"+stack.pop());
		System.out.println("2nd:"+stack.pop());
		System.out.println("3rd:"+stack.pop());
		System.out.println("4th:"+stack.pop());
		stack.showInfo();
		
		MyQue myQue = new MyQue();
		myQue.push("A");
		myQue.push("B");
		myQue.push("C");
		myQue.push("D");
		myQue.showInfo();
		
		System.out.println("1st:"+myQue.deQue());
		System.out.println("2nd:"+myQue.deQue());
		System.out.println("3rd:"+myQue.deQue());
		System.out.println("4th:"+myQue.deQue());
		myQue.showInfo();
		
	}

}
