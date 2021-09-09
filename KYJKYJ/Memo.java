package com.example.simplememo;

import java.awt.Font;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Timestamp;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTable;
import javax.swing.JTextField;
import javax.swing.SwingConstants;
import javax.swing.border.EmptyBorder;
import javax.swing.table.DefaultTableModel;

public class Memo extends JFrame {

	private JPanel contentPane;
	private JTextField txtWriter;
	private JTextField txtRegistdate;
	private JTextField txtTitle;
	private JTextField txtContents;
	private JTable tblMemolist;

	private DefaultTableModel model; // Table modeling variable 

	/**
	 * Launch the application.
	 */

	/**
	 * Create the frame.
	 */
	public Memo(String username) {
		addWindowListener(new WindowAdapter() {
			@Override
			
			//Memo Frame is Opened
			public void windowOpened(WindowEvent e) {
				LoadTbl();
			}
		});
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 501, 389);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);

		JButton btnNewButton = new JButton("Exit");
		btnNewButton.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				DBUtil.DBClose();
				dispose();
				System.out.println("Program is ended");
				System.exit(0);
			}
		});
		btnNewButton.setBounds(376, 317, 97, 23);
		contentPane.add(btnNewButton);

		JLabel lblNewLabel = new JLabel("Simple Memo");
		lblNewLabel.setHorizontalAlignment(SwingConstants.CENTER);
		lblNewLabel.setFont(new Font("Arial", Font.PLAIN, 15));
		lblNewLabel.setBounds(142, 10, 148, 23);
		contentPane.add(lblNewLabel);

		JLabel lblNewLabel_1 = new JLabel("Writer");
		lblNewLabel_1.setBounds(12, 50, 57, 15);
		contentPane.add(lblNewLabel_1);

		JLabel lblNewLabel_2 = new JLabel("Date");
		lblNewLabel_2.setBounds(12, 75, 57, 15);
		contentPane.add(lblNewLabel_2);

		JLabel lblNewLabel_3 = new JLabel("Title");
		lblNewLabel_3.setBounds(12, 100, 57, 15);
		contentPane.add(lblNewLabel_3);

		JLabel lblNewLabel_4 = new JLabel("Contents");
		lblNewLabel_4.setBounds(12, 125, 57, 15);
		contentPane.add(lblNewLabel_4);

		txtWriter = new JTextField();
		txtWriter.setBounds(67, 47, 100, 21);
		contentPane.add(txtWriter);
		txtWriter.setColumns(10);

		txtRegistdate = new JTextField();
		txtRegistdate.setBounds(67, 72, 100, 21);
		contentPane.add(txtRegistdate);
		txtRegistdate.setColumns(10);

		txtTitle = new JTextField();
		txtTitle.setBounds(67, 97, 100, 21);
		contentPane.add(txtTitle);
		txtTitle.setColumns(10);

		txtContents = new JTextField();
		txtContents.setBounds(67, 122, 100, 21);
		contentPane.add(txtContents);
		txtContents.setColumns(10);

		JScrollPane scrollPane = new JScrollPane();
		scrollPane.setBounds(214, 43, 239, 264);
		contentPane.add(scrollPane);

		tblMemolist = new JTable();
		tblMemolist.addMouseListener(new MouseAdapter() {
			
			@Override
			// mouse click!
			public void mouseClicked(MouseEvent e) {
				int row = tblMemolist.getSelectedRow();
				int id = Integer.parseInt(tblMemolist.getModel().getValueAt(row, 0).toString());
				setTextField(id);
				
			}
		});
		scrollPane.setViewportView(tblMemolist);

		JButton btnReset = new JButton("Reset");
		btnReset.addActionListener(new ActionListener() {
			
			// Reset Button Click!
			public void actionPerformed(ActionEvent e) {
				txtTitle.setText("");
				txtWriter.setText("");
				txtRegistdate.setText("");
				txtContents.setText("");
			}
		});
		btnReset.setVerticalAlignment(SwingConstants.BOTTOM);
		btnReset.setBounds(12, 171, 97, 23);
		contentPane.add(btnReset);

		JButton btnSave = new JButton("Save");
		btnSave.addActionListener(new ActionListener() {
			
			// Save Button Click!
			public void actionPerformed(ActionEvent e) {
				String query = "INSERT INTO memo(writer, title, registdate, contents)" + "VALUES(?,?,?,?)";
				
				String writer = username; // data from Log-in Class When calling Memo class.
				// or txtWriter.getText();
				String title = txtTitle.getText();
				String registdate = txtRegistdate.getText();
				String contents = txtContents.getText();
				
				try {
					PreparedStatement pstmt = DBUtil.dbconn.prepareStatement(query);
					pstmt.setString(1,writer);
					pstmt.setString(2,title);
					pstmt.setString(3,registdate);
					pstmt.setString(4,contents);
					
					pstmt.execute(); // not query (not Load)
					
					LoadTbl();
					
				}catch(SQLException einsert) {
					System.out.println("[ERROR!]Data Save(Insert) error.");
					einsert.printStackTrace();
					
				}
			} // end of action perform.
		});
		btnSave.setBounds(12, 199, 97, 23);
		contentPane.add(btnSave);

		JButton btnUpdate = new JButton("Correct");
		btnUpdate.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
			}
		});
		btnUpdate.setBounds(12, 228, 97, 23);
		contentPane.add(btnUpdate);

		JButton btnDelete = new JButton("Delete");
		btnDelete.setBounds(12, 256, 97, 23);
		contentPane.add(btnDelete);
	} // end of memo constructor

	// memo method

	private void LoadTbl() {
		// Table Modeling (Column listing)
		DefaultTableModel model = new DefaultTableModel();
		model.addColumn("Number(ID)");
		model.addColumn("Witer");
		model.addColumn("Title");
		model.addColumn("RegistDatg");
		model.addColumn("Contents");

		// Query Execute (from 'memo' table of 'javadb' schema in DB)
		String query = "SELECT * FROM memo";

		try {
			PreparedStatement pstmt = DBUtil.dbconn.prepareStatement(query);
			ResultSet rs = pstmt.executeQuery();
			
		// Data Load and Make a Row in JFrame(memo) table(LoadTbl)	
			while(rs.next()) {
				model.addRow(new Object[] { // Data load from memo Table in DB(with Date type), Make a Row Data in LoadTbl 
						rs.getInt(1),
						rs.getString(2),
						rs.getString(3),
						rs.getDate(4),
						rs.getString(5)
				});
			} // end of while
			rs.close();
			pstmt.close();
			
			tblMemolist.setModel(model); // Make a tblMemolist using 'model'
			tblMemolist.setAutoResizeMode(0);
			tblMemolist.getColumnModel().getColumn(0).setPreferredWidth(20);
			tblMemolist.getColumnModel().getColumn(1).setPreferredWidth(50);
			tblMemolist.getColumnModel().getColumn(2).setPreferredWidth(80);
			tblMemolist.getColumnModel().getColumn(3).setPreferredWidth(80);
			tblMemolist.getColumnModel().getColumn(4).setPreferredWidth(300);

			JOptionPane.showMessageDialog(null, "Memo is loaded.");

		} catch(SQLException eload) {
			System.out.println("[ERROR!]Table Loading error.");
		}


	} // end of LoadTbl
	
	private void setTextField(int id) {
		String query = "SELECT * FROM memo WHERE id=?";
		try {
			PreparedStatement pstmt = DBUtil.dbconn.prepareStatement(query);
			pstmt.setInt(1,id);
			ResultSet rs = pstmt.executeQuery();
			while(rs.next()) {
				txtWriter.setText(rs.getString(2));
				txtTitle.setText(rs.getString(3));
				
				// Date Expression
				Timestamp date = rs.getTimestamp(4);
				java.text.SimpleDateFormat formatter =
						//new java.text.SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
						new java.text.SimpleDateFormat("yyyy-MM-dd");
				txtRegistdate.setText(formatter.format(date));
				
				txtContents.setText(rs.getString(5));
			}
			
		} catch(SQLException eset) {
			System.out.println("[ERROR!]Data ");
		}
	}



} // end of class
