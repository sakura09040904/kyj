package lesson01;

// 추상클래스 CPerson으로부터 상속받아 클래스 생성.
// 추상클래스는 객체 생성 불가.

public class CStudent extends CPerson {

	String id;
	
	public CStudent(String id) {
		this.id = id;
		
	}

// 상속받은 추상클래스내의 추상메서드 override 필요
	@Override
	public void showInfo() {
		
		System.out.println("Student ID: "+id);
		// TODO Auto-generated method stub
	}

}
