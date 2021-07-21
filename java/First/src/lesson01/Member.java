package lesson01;

// 멤버를 생성하여 정보를 저장하는 클래스
public class Member {
	
	private int id;
	private String name;
	
	//constructor
	public Member() {}

	public Member(int id, String name) {
		this.id = id;
		this.name = name;
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	//회원정보 출력을 위한 toString() override.
	// print(Member member)에서 실행
	@Override
	public String toString() {
		return name+"님의 ID는 "+id+"입니다.";
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}
	
}
