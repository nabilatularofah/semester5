package nabil;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.URL;
import java.net.URLConnection;

public class App {
    public static void main(String[] args) throws Exception {
        URL address = new URL("https://www.youtube.com");
        URLConnection conn = address.openConnection();
        BufferedReader reader = new BufferedReader(
            new InputStreamReader(conn.getInputStream())
        );

        while (true) {
            String inputLine = reader.readLine();

            if (inputLine == null){
                break;
            }

            System.out.println(inputLine);
        }
    }
}
