package com.example.simplememo;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

// DB Connection class
public class DBUtil {
	// Basic information variable for DB connection
	static final String JDBCDRV = "com.mysql.cj.jdbc.Driver"; // JDBC Driver Name
	// localhost: portnumber, javadb: schema name
	static final String URL = "jdbc:mysql://localhost:3306/javadb?serverTimezone=UTC";
	static final String DBUSER = "java";
	static final String DBPWD = "1234";
	
	// DB connection variable
	static Connection dbconn = null;
	
	public static void DBConnect() {
		try {
			Class.forName(JDBCDRV); // JDBC DRV Load
			System.out.println("[Complete] JDBC DRV is loeded");
			dbconn = DriverManager.getConnection(URL, DBUSER, DBPWD); // JDBC Connect
		} 
		catch (ClassNotFoundException e){
			e.printStackTrace();
			System.out.println("[Error] JDBC DRV is not loeded");
		}
		catch (SQLException e){
			e.printStackTrace();
			System.out.println("[Error] URL/USER/PWD is not corrected");
		}
		System.out.println("[Complete] JDBC DRV is connected");
	}// end of DB Cnt
	
	public static void DBClose() {
		
	}// end of DB Close
	
}
