package lesson01;

public class BPerson {

	String name;
	String address;

	public void BPerson(String name, String address) {
		this.name = name;
		this.address = address;
	}
	
	public void showInfo() {
		System.out.println("이름: "+name+", 주소: "+address);
	}
}
