package lesson01;

import java.util.Iterator;
import java.util.TreeSet;

public class ETreeSetTest {

	public static void main(String[] args) {

		// Add
		TreeSet<Integer> numbers = new TreeSet<>();

		numbers.add(4);
		numbers.add(2);
		numbers.add(8);
		numbers.add(6);
		System.out.println("TreeSet: "+numbers);

		TreeSet<Integer> number = new TreeSet<>();
		number.add(1);
		number.add(7);
		number.add(3);
		number.add(5);

		// Add All (Union(합집합))
		number.addAll(numbers);
		System.out.println("New TreeSet(Union): "+number);

		// Iterator
		System.out.print("Using Iterator: ");
		Iterator<Integer> ir = number.iterator();
		while(ir.hasNext()) {
			System.out.print(ir.next());
			System.out.print(", ");
		}
		System.out.println();
		System.out.println("---------------------------------------------");

		// remove(), removeAll()
		System.out.println("5 is removed? "+number.remove(5));
		System.out.println("all is removed? "+numbers.removeAll(numbers));
		System.out.println("---------------------------------------------");

		// first(), last()
		System.out.println("First Number: "+number.first());
		System.out.println("Last Number: "+number.last());
		System.out.println("---------------------------------------------");

		// higher, lower, ceiling, floor, headset, tailset
		System.out.println("higher than 5: "+number.higher(5));
		System.out.println("lower than 5: "+number.lower(5));
		System.out.println("lower than 5: "+number.lower(5));
		System.out.println("ceiling 5: "+number.ceiling(5));
		System.out.println("floor 5: "+number.floor(5));
		System.out.println("headset without: "+number.headSet(6));
		System.out.println("headset with: "+number.headSet(6, true));
		System.out.println("headset without: "+number.tailSet(6));
		System.out.println("headset with: "+number.tailSet(6, false));
		System.out.println("---------------------------------------------");

		//subSet(e1, 이상(T/F), e2, 이하(T/F))
		System.out.println("subset without boolean: "+number.subSet(2, 6));
		System.out.println("subdset with boolean: "+number.subSet(2, false, 6, true));

		// Intersection (교집합)
		numbers.add(4);
		numbers.add(2);
		numbers.add(8);
		numbers.add(6);
		numbers.retainAll(number);
		System.out.println("Intersection of two set: "+numbers);
		// Difference (차집합)
		number.removeAll(numbers);
		System.out.println("Difference of two set: "+number);
		// Subset (부분집합)
		numbers.removeAll(numbers);
		numbers.add(1);
		numbers.add(3);
		System.out.println("Is subset?: "+number.containsAll(numbers));
		System.out.println("---------------------------------------------");

	}

}
