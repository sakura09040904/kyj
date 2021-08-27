package lesson02;

import lesson01.ManageMember;
import lesson01.Member;

public class MemberArrayListTest {

	public static void main(String[] args) {
		// 김연지
		ManageMember arrayMember = new ManageMember();

		Member mem1 = new Member(1001,"kim1");
		Member mem2 = new Member(1002,"kim2");
		Member mem3 = new Member(1003,"kim3");
		Member mem4 = new Member(1004,"kim4");
		Member mem5 = new Member(1005,"kim5");

		arrayMember.addMember(mem1);
		arrayMember.addMember(mem2);
		arrayMember.addMember(mem3);
		arrayMember.addMember(mem4);
		arrayMember.addMember(mem5);

		arrayMember.showAllMember();

		arrayMember.removeMember(mem3.getId());

		arrayMember.showAllMember();


	}

}
