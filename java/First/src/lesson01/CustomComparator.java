package lesson01;

import java.util.Comparator;
import java.util.PriorityQueue;


class Main{
	public static void main(String[] args) {
		PriorityQueue<Integer> myque = new PriorityQueue<Integer>(new CustomComparator());
		myque.add(4);
		myque.add(2);
		myque.add(1);
		myque.add(3);
		 System.out.print("PriorityQueue: " + myque);
	}
}


public class CustomComparator implements Comparator<Integer> {

	@Override
	public int compare(Integer number1, Integer number2) {
        int value =  number1.compareTo(number2);
        // elements are sorted in reverse order
        if (value > 0) {
            return -1;
        }
        else if (value < 0) {
            return 1;
        }
        else {
            return 0;
        }
	}
}
