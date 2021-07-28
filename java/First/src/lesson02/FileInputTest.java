package lesson02;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class FileInputTest {

	public static void main(String[] args) {
		FileInputStream fis=null;

		try {
			fis = new FileInputStream("C:/Users/user9/Desktop/input.txt");
			System.out.println(fis.read());
			System.out.println(fis.read());
			System.out.println(fis.read());
		} 

		//IOExcption에 포함되기 때문에 먼저 catch.
		catch (FileNotFoundException e) {   
			e.printStackTrace();
			System.out.println("File is not found");
		}
		//file read error check
		catch (IOException efile) {
			efile.printStackTrace();
			System.out.println("파일 입출력 처리 오류");
		}System.out.println("Program1 is ended");
		System.out.println("----------------------------------------------------------");
		
		
		try {
			FileReader fr = new FileReader("C:/Users/user9/Desktop/input2.txt");
			int i;
			while((i=fr.read()) != -1){
				System.out.print((char)i);
			}System.out.println();
		}
		catch (FileNotFoundException e) {   
			e.printStackTrace();
			System.out.println("File is not found");
		}
		catch (IOException e) {
			e.printStackTrace();
		}System.out.println("Program2 is ended");

	}

}
