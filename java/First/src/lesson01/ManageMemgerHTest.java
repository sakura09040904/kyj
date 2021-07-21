package lesson01;

public class ManageMemgerHTest {

	public static void main(String[] args) {
		ManageMemberH memberHash = new ManageMemberH();
		
		Member member1 = new Member(1001, "kim1");
		Member member2 = new Member(1002, "kim2");
		Member member3 = new Member(1003, "kim3");
		Member member4 = new Member(1004, "kim4");
		
		memberHash.addMember(member1);
		memberHash.addMember(member2);
		memberHash.addMember(member3);
		memberHash.addMember(member4);
		
		memberHash.showAll();
		memberHash.removeMember(1002);
		memberHash.showAll();

	}

}
