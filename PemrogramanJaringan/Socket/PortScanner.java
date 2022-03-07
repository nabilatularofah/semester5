package nabil;

import java.net.InetAddress;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.Scanner;

/**
 * melacak port-
 * port yang terbuka (tersedia) pada suatu IP server tertentu
 * 
 */
public class PortScanner {
    public static void main(String[] args) throws UnknownHostException{
        //membuat object scanner untuk input dari keyboard
        Scanner input = new Scanner(System.in);

        System.out.print("IP Address target : ");
        String host = input.next(); //meminta niput ip address target

        System.out.println("Scan port from : ");
        int portStarted = input.nextInt(); //meminta input port awal
        System.out.println("until port num : ");
        int portEnded = input.nextInt(); //meminta input port akhir

        input.close();

        InetAddress inetAddress = InetAddress.getByName(host);
        System.out.println("inetAddress : " + inetAddress);
        String hostName = inetAddress.getHostName();
        System.out.println("hostName : " + hostName);

        for (int port = portStarted; port <= portEnded; port++) {
            try{
                Socket socket =new Socket(hostName, port); //scan ip address & port
                String text = hostName + " is listening on port " + port;
                System.out.println(text);
                socket.close();
            }
            catch (Exception e) {
                //TODO: handle exception
            }
        }
    }
}
