package lesson01;

public class BStudent extends BPerson {
	String studentId;
	
		
	public BStudent() {
	}

	public BStudent(String studentId) {
		this.studentId = studentId;
		this.name = "Null";
		this.address = "Null";
	}
	
	public BStudent(String name, String address, String studentId) {
		this.studentId = studentId;
		this.name = name;
		this.address = address;
	}

	public void learn(String subject) {
		System.out.println("이름: "+name+", 주소: "+address+", 수업과목: "+subject);
	}

	@Override
	public void showInfo() {
		System.out.println("Name: "+name+", Address: "+address);
	}
	

}
