package lesson002;

import java.util.HashSet;

public class HashSetTest {

	public static void main(String[] args) {
		// Set 인터페이스를 이해하고 활용할 수 있다.
		HashSet<String> hashSet = new HashSet<String>();
		
		hashSet.add(new String("임정순"));
		hashSet.add("박현정");
		hashSet.add("박현정");
		hashSet.add("박현정");
		hashSet.add("박현정");
		hashSet.add("박현정");
		hashSet.add("박현정");
		hashSet.add("박현정");
		hashSet.add("박현정");
		hashSet.add("박현정");
		System.out.println(hashSet);
		

	}

}
