package lesson002;

public class BPerson {
	String name;
	String address;

	// 이름과 주소를 패러미터로 받는 생성자
	public void BPerson(String name, String address) {
		this.name = name;
		this.address = address;
	}
	
	public void showinfo() {
		System.out.println(name + " : " + address);
	}
}//end of class
