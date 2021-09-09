package lesson002;

public class MemberHashMapTest {

	public static void main(String[] args) {
		MemberHashMap memberHashMap = new MemberHashMap();
		
		Member member1 = new Member(1001, "홍길동1");
		Member member2 = new Member(1002, "홍길동2");
		Member member3 = new Member(1003, "홍길동3");
		Member member4 = new Member(1004, "홍길동4");
		
		memberHashMap.addMember(member1);
		memberHashMap.addMember(member2);
		memberHashMap.addMember(member3);
		memberHashMap.addMember(member4);
		
		System.out.println("--- 4개 데이터 추가 후 전체 출력");
		memberHashMap.showAllMember();
		
		System.out.println("--- 1개 데이터 삭제 후 전체 출력");
		memberHashMap.removeMember(1003);
		memberHashMap.showAllMember();

	}

}
