package lesson01;

// 인터페이스(DPerson을) implement(구현) (클래스 상속과 같음)
// 여러개의 인터페이스를 implement 할 수 있음. (상속은 한개만 가능)

public class DStudent implements DPerson {

	@Override
	public void sleep() {
		System.out.println("Sleeping");
	}

	@Override
	public void eat() {
		System.out.println("Eating");
	}

}
