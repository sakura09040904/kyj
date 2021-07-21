package lesson01;

import java.util.ArrayList;

// 생성된 멤버들의 정보를 받아 Array로 만들어 관리하는 클래스
public class ManageMember {
	
	private ArrayList<Member> memberArray;

	public ManageMember() {
		memberArray = new ArrayList<Member>();
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
