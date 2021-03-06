package nabil;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.InetAddress;
import java.net.Socket;
import java.net.UnknownHostException;

/**
 * TCP Echo Client Aplikasi ini berpasangan dengan TCPEchoServer
 */

public class TCPEchoClient {
    //private static String strHostl
    private static InetAddress host;
    private static final int PORT = 1234;

    public static void main(String[] args){
        try{
            host = InetAddress.getLocalHost();
            // strHost = args[0];
            // host = InetAddress.getByName(strHost);
        }
        catch (UnknownHostException e){
            System.out.println("Host ID Not Found");
            System.exit(1);
        }
        run();
    }

    private static void run() {
        Socket link = null;
        try{
            link = new Socket(host, PORT);
            BufferedReader in = new BufferedReader(new InputStreamReader(link.getInputStream()));
            PrintWriter out = new PrintWriter(link.getOutputStream(), true);
            BufferedReader userEntry = new BufferedReader(new InputStreamReader(System.in));

            String message, response;
            do {
                System.out.print("Enter message : ");
                message = userEntry.readLine();
                out.println(message);
                response = in.readLine();
                System.out.println("SERVER " + response);
            }
            while (!message.equals("close"));
        } catch (IOException e) {
            e.printStackTrace();
        }
        finally{
            try{
                System.out.println("closing connection");
                link.close();
            }
            catch (IOException e){
                System.out.println("Unable to disconnect!");
                System.exit(1);
            }
        }
    }  
}