package lesson002;

public class Member {
	private int memberId; // 회원아이디
	private String memberName; // 회원이름

	// 생성자constructor
	public Member(int memberId, String memberName) {
		this.memberId = memberId;
		this.memberName = memberName;
	}

	// getters & setters
	public int getMemberId() {
		return memberId;
	}

	public void setMemberId(int memberId) {
		this.memberId = memberId;
	}

	public String getMemberName() {
		return memberName;
	}

	public void setMemberName(String memberName) {
		this.memberName = memberName;
	}

	@Override
	public String toString() {
		// TODO Auto-generated method stub
		return memberName + " 회원님의 아이디는 " + memberId + "입니다.";
	}
	
	

}// end of class
