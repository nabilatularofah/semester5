package nabil;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.InetAddress;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Scanner;

/**
 * SimpleEchoServer aplikasi berbasis SocketServer dan Socket
 */
public class SimpleEchoServer{
    private static ServerSocket servSock;
    public static void main(String[] args){
        //membuat objek scanner untuk input dari keyboard
        Scanner input = new Scanner(System.in);
        System.out.print("Input Port Server diinginkan: ");
        int PORT = input.nextInt();
        input.close();
        try{
            servSock = new ServerSocket(PORT);
            InetAddress host = InetAddress.getLocalHost();
            System.out.println("SimpleEchoServer is not at " + host + "with port " + PORT);
            while(true){
                Socket incoming = servSock.accept();
                BufferedReader in = new BufferedReader(new InputStreamReader(incoming.getInputStream()));
                PrintWriter out = new PrintWriter(incoming.getOutputStream(), true);
                out.println("Hello This is from the java SimpleEchoServer");
                out.println("Enter BYE to exit");
                out.flush();
                while(true){
                    String str = in.readLine();
                    /*if(str==null){
                        break; //client closed connection if not enter anything
                    }*/
                    out.println("Echo: " + str);
                    out.flush();
                    if (str.trim().equals("BYE")){
                        break; //client wants to closed connection
                    }
                }
                in.close();
                out.close();
                incoming.close();
            }
        }
        catch (Exception e){
            System.out.println("Unable to attach to port or problem disconnect");
            System.exit(1);
        }
    }
}