package lesson00;

public class ArrayBook {
	private String author;
	private String title;
	static int num=0;
	private int bookNum;

	public ArrayBook() {
		this.num++;
		this.bookNum = num;
	}

	public ArrayBook(String author, String title) {
		this.author = author;
		this.title = title;
		this.num++;
	}

	public String getAuthor() {
		return author;
	}
	public void setAuthor(String author) {
		this.author = author;
	}

	public String getTitle() {
		return title;
	}

	public void setTitle(String title) {
		this.title = title;
	}

	public void showInfo() {
		System.out.printf("Book Number: %d\nAuthor: %s\nTitle:%s\n\n", this.bookNum, this.author, this.title);
	}

}
