package lesson00;

import java.util.Scanner;

public class SortWords {

	public static void main(String[] args) {
		
		Scanner input = new Scanner(System.in);
		System.out.print("Please input words. (distinguished by space bar)");
		String word = input.nextLine();
		String[] words = word.split(" ");
		
		String tmp = "";
		
		for(int i=0; i<(words.length-1); i++) {
			for(int j=i+1; j<words.length; j++) {
				if(words[i].compareTo(words[j]) > 0) {
					tmp = words[i];
					words[i] = words[j];
					words[j] = tmp; 
				}
			}
		}

		for(int i=0; i<words.length; i++) {
			System.out.println(words[i]);
		}

	}

}
