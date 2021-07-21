package lesson01;

import java.util.HashMap;
import java.util.Iterator;

public class ManageMemberH {
	
	private HashMap<Integer, Member> hashMap;
	
	public ManageMemberH() {
		hashMap = new HashMap<Integer,Member>();
	}
	
	public void addMember(Member member) {
		hashMap.put(member.getId(), member);
	}
	
	public boolean removeMember(int id) {
		if(hashMap.containsKey(id)) {
			hashMap.remove(id);
			return true;
		}
		System.out.print(id+"is not exsist");
		return false;
	}

	public void showAll() {
		Iterator<Integer> ir = hashMap.keySet().iterator();
		while (ir.hasNext()) {
			int key = ir.next();
			Member member = hashMap.get(key);
			System.out.println(member);
		} System.out.println();
	}

}
