package lesson01;

public class BStudentTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		BStudent stu1 = new BStudent("kim1", "청주시", "1001");
		BStudent stu2 = new BStudent("1002");
		BStudent stu3 = new BStudent();
		
		stu1.showInfo();
		stu1.learn("java");
		stu2.showInfo();
		stu3.showInfo();
	}

}
