package lesson002;

public class BStudent extends BPerson {
	String studentId;
	
	public BStudent(String studentId) {
		this.studentId = studentId;
		this.name = "무명씨";
		this.address = "주소불명";
	}
	
	public BStudent(String name, String address, String studentId) {
		this.studentId = studentId;
		this.name = name;
		this.address = address;
	}
	
	public void learn(String subject) {
		System.out.println(name + "은(는) " + subject + "을(를) 공부합니다.");
	}
	
	@Override
	public void showinfo() {
		System.out.println(studentId + ", " + name + ": " + address);
	}
	
	
}
