package lesson02;
import java.util.ArrayList;

import lesson01.Member;

public class MemberArrayList {
	 // 김연지

	private ArrayList<Member> memberArray = new ArrayList<Member>();
	
	public MemberArrayList() {
		this.memberArray = memberArray;
	}

	public MemberArrayList(ArrayList<Member> memberArray) {
		this.memberArray = memberArray;
	}
	
	public void addMember(Member member) {
		memberArray.add(member);
	}
	
	public boolean removeMember(int id) {
		for(int i=0; i<memberArray.size(); i++) {
			Member member = memberArray.get(i);
			int tmp = member.getId();
			if(tmp == id) {
				memberArray.remove(i);
				return true;
			}
		}
		System.out.print(id+"is not exsist");
		return false;
	}
	
	public void showAllMember() {
		for(Member member : memberArray) {
			System.out.println(member);
		}System.out.println("-------------------------------------------");
	}
	
}
