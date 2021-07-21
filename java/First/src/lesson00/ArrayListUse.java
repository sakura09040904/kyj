package lesson00;

import java.util.ArrayList;

public class ArrayListUse {

	// Using Variables

	public static void main(String[] args) {
		ArrayBook book1 = new ArrayBook();
		ArrayBook book2 = new ArrayBook();
		book1.setAuthor("Joan Rolling");
		book1.setTitle("Harry Potter");
		book2.setAuthor("JRR Tolkin");
		book2.setTitle("Lord of the ring");

		book1.showInfo();
		book2.showInfo();

		// Using ArrayList		
		// ArrayList<Class> variable = new ArraList<Class>();	

		ArrayList<ArrayBook> books = new ArrayList<ArrayBook>();

		books.add(new ArrayBook("Author1","Book1"));
		books.add(new ArrayBook("Author2","Book2"));
		books.add(new ArrayBook("Author3","Book3"));
		books.add(new ArrayBook("Author4","Book4"));
		books.add(new ArrayBook("Author5","Book5"));
		books.add(new ArrayBook("Author6","Book6"));
		books.add(new ArrayBook("Author7","Book7"));
		books.add(new ArrayBook("Author9","Book9"));
		books.add(new ArrayBook("Author10","Book10"));

		// insert specific array using index
		books.add(7, new ArrayBook("Author8","Book8"));
		// remove specific array using index		
		books.remove(5);

		// for(Class variable:Array)	
		for(ArrayBook book:books) {
			book.showInfo();
		}

	}
}