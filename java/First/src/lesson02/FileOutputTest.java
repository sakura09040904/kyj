package lesson02;

import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;

public class FileOutputTest {

	public static void main(String[] args) {
		try {
			FileWriter fw = new FileWriter("C:/Users/user9/Desktop/output2.txt");
			fw.write('A');
			char buf[] = {'B','C','D','E'};
			fw.write(buf);
			fw.write("안녕하세요");
			fw.write(buf, 1, 2);
			fw.write("65");
			System.out.println("진행중...");
			fw.close();
		} 
		catch (FileNotFoundException e) {   
			e.printStackTrace();
			System.out.println("File is not found");
		}
		catch (IOException e) {
			e.printStackTrace();
			System.out.println("Onput Error");
		}
		
		System.out.println("Program is ended");
		

	}

}
