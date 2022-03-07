package com.nabil.jdbcsocket;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.ResultSet;
import java.sql.Statement;

public class App {
    private static final String URL =  "jdbc:mysql://localhost:3306/dbase?user=root&password=''";

    private static void printResult(ResultSet rs) throws SQLException {
        System.out.println("== Data Pegawai");
        while (rs.next()) {
            int nip = rs.getInt(1);
            String nama = rs.getString(2);
            String kelamin = rs.getString(3);
            String jabatan = rs.getString(4);
            System.out.println("NIP          : " + nip);
            System.out.println("Nama         : " + nama);
            System.out.println("Kelamin      : " + kelamin);
            System.out.println("Jabatan      : " + jabatan);
            System.out.println();
        }
        System.out.println("================================");
    }

    public static void main(String[] args) throws Exception {
        System.out.println("Connecting....");
        try(
            Connection conn = DriverManager.getConnection(URL);
            Statement stmt = conn.createStatement();
        ){
            System.out.println("Creating table...");
            stmt.execute("DROP TABLE IF EXISTS pegawai");
            stmt.execute("CREATE TABLE pegawai(nip INTEGER(20) PRIMARY KEY NOT NULL, nama(50) NOT NULL,kelamin(10) NOT NULL,jabatan(20) NOT NULL);");

            System.out.println("Inserting data...");
            int updateResult = stmt.executeUpdate(
                "INSERT TO pegawai VALUES" +
                "('197210011993111003', 'Emanuel', 'Laki-laki', 'Kelapa Dinas'), " +
                "('196802271999031004', 'Vivia Beatrix', 'Perempuan', Sekretaris'), " +
                "('196909041998031004', 'Yoseph Faot', 'Laki-laki', 'Bendahara')"
            );

            if (updateResult !=3){
                throw new Exception("Unable to insert data");
            }

            ResultSet rs = stmt.executeQuery("SELECT * FROM pegawai");
            printResult(rs);
            
            System.out.println("Updating 2nd data...");
            updateResult = stmt.executeUpdate("UPDATE pegawai SET nama='Chandra D', jabatan='Humas' WHERE nip='1966071219990031012'");

            if (updateResult !=1){
                throw new Exception("Unable to update 2nd data");
            }

            rs = stmt.executeQuery("SELECT * FROM pegawai");
            printResult(rs);

            System.out.println("Done.");
            }
            catch (Exception ex){
                System.out.println("Error");
                System.out.println(ex.toString());
        }
    }
}
