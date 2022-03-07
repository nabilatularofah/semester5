package nabil;

import java.net.InetAddress;
import java.util.Scanner;

/**
 * IPtoName program untuk mendapatkan nama komputer dari alamat IP
 */

public class IPtoName {
    public static void main(String[] args){
        //membuat object scanner unutk input dari keyboard
        Scanner input = new Scanner(System.in);

        //meminta input ip address dari keyboard
        System.out.println("Input IP Address lokal ataupun komputer di jaringan");
        System.out.println("IP Address : ");
        String host = input.next(); //hasil input keyboadr dimasukkan ke var host
        input.close();

        InetAddress address = null; // membuat object InetAddress
        try{
            address = InetAddress.getByName(host); // mendapatkan nama komputer
        }
        catch(Exception e){
            System.out.println("invalid IP");
            System.exit(0);
        }
        System.out.println(address.getHostName()); // cetak nama komputer
    }   
}
