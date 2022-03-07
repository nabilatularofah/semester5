package thread_printName;

import java.util.logging.Level;
import java.util.logging.Logger;

public class ThreadPrintName extends Thread {
    public ThreadPrintName(String name) {
        super(name);
        start();//menjalankan thread dengan satu kali instansiasi
    }

    @Override
    public void run() {
        String name = getName();
        for(int i=0; i<20; i++){
            System.out.print(name);
            try{
                Thread.sleep(1000);
            }
            catch (InterruptedException ex){
                Logger.getLogger(ThreadPrintName.class.getName()).log(Level.SEVERE, null, ex);
                //ex.printStackTrace();
            }
        }
    }

}
