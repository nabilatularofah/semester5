package nabil;

import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;

/**
 * UDP Echo Server
 * Server using UDP protocol
 */
public class UDPEchoServer {
    private static final int PORT = 123;
    private static DatagramSocket dgramSocket;
    private static DatagramPacket inPacket, outPacket;
    private static byte[] buffer;

    public static void main(String[] args) {
        System.out.println("Opening Port" + PORT + "...\n" );
        try{
            dgramSocket = new DatagramSocket(PORT);
        }
        catch (Exception e){
            System.out.println("Unable to attach to port !");
            System.exit(1);
        }
        run();
    }
    private static void run(){
        try{
            String messageIn, messageOut;
            int numMessage = 0;
            do{
                buffer = new byte[256];
                inPacket = new DatagramPacket(buffer, buffer.length);
                dgramSocket.receive(inPacket);
                InetAddress clieInetAddress = inPacket.getAddress();
                int clientPort = inPacket.getPort();
                messageIn = new String(inPacket.getData(), 0, inPacket.getLength());
                System.out.println("Message Received");
                numMessage++;
                messageOut = ("Message " + numMessage + ":" + messageIn);
                outPacket = new DatagramPacket(messageOut.getBytes(), messageOut.length(), clieInetAddress, clientPort);
                dgramSocket.send(outPacket);
            }
            while (true);
        }
        catch (Exception e){
            e.printStackTrace();
        }
        finally{
            System.out.println("\n Closing Connection...");
            dgramSocket.close();
        }
    }
}
