package com.example.simplememo;

import java.awt.EventQueue;
import java.awt.Font;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JPasswordField;
import javax.swing.JTextField;
import javax.swing.SwingConstants;
import javax.swing.border.EmptyBorder;

public class Login extends JFrame {

	private JPanel contentPane;
	private JTextField txtUsername;
	private JPasswordField txtPwd;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					if(DBUtil.dbconn == null) DBUtil.DBConnect();
					Login frame = new Login();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public Login() {
		setTitle("Login Demo");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lblNewLabel = new JLabel("Login System");
		lblNewLabel.setHorizontalAlignment(SwingConstants.CENTER);
		lblNewLabel.setFont(new Font("맑은 고딕", Font.PLAIN, 20));
		lblNewLabel.setBounds(111, 33, 212, 30);
		contentPane.add(lblNewLabel);
		
		JLabel lblNewLabel_1 = new JLabel("User Name");
		lblNewLabel_1.setFont(new Font("D2Coding", Font.PLAIN, 16));
		lblNewLabel_1.setBounds(51, 90, 99, 30);
		contentPane.add(lblNewLabel_1);
		
		JLabel lblNewLabel_1_1 = new JLabel("Password");
		lblNewLabel_1_1.setFont(new Font("D2Coding", Font.PLAIN, 16));
		lblNewLabel_1_1.setBounds(51, 145, 99, 30);
		contentPane.add(lblNewLabel_1_1);
		
		txtUsername = new JTextField();
		txtUsername.setBounds(162, 95, 203, 21);
		contentPane.add(txtUsername);
		txtUsername.setColumns(10);
		
		txtPwd = new JPasswordField();
		txtPwd.setBounds(162, 150, 203, 21);
		contentPane.add(txtPwd);
		
		JButton btnLogin = new JButton("Log-In");
		btnLogin.addActionListener(new ActionListener() {

			// Click Log-in and Start!!!
			public void actionPerformed(ActionEvent e) {
				// DB Connection Check again.
				if(DBUtil.dbconn == null) DBUtil.DBConnect();
				// input user information
				String username = txtUsername.getText();
				String userpwd = new String(txtPwd.getPassword());
				
				//SQL input
				//String query = "SELECT * FROM users WHERE username="+username+"and userpwd="+userpwd; // by statement
				String query = "SELECT * FROM users WHERE username=? and userpwd=?"; //by prepared statement
				
				try {
					PreparedStatement pstmt = DBUtil.dbconn.prepareStatement(query);
					pstmt.setString(1,  username);
					pstmt.setString(2,  userpwd);
					ResultSet rs = pstmt.executeQuery();
					if(rs.next()) { // Log-in is performed
						//System.out.println("Log-in is complete.");
						rs.close();
						pstmt.close();
						dispose(); // close present window (and resource return)
						Memo memo = new Memo(username);
						memo.setVisible(true);
						
					} else { // not performed
						System.out.println("Pleas check account or password.");
					}
					rs.close();
					pstmt.close();
					
				}catch(SQLException elogin) {
					System.out.println("Log-in Error.");
					elogin.printStackTrace();
				}
				
			}
		});
		btnLogin.setBounds(162, 204, 123, 23);
		contentPane.add(btnLogin);
	}
}
