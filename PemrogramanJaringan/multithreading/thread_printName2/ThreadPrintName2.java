package thread_printName2;
import java.util.logging.Level;
import java.util.logging.Logger;

public class ThreadPrintName2 implements Runnable {
    Thread thread;

    public ThreadPrintName2(String name) {
        thread = new Thread(this, name);
        thread.start();//menjalankan thread dengan satu kali instansiasi
    }

    @Override
    public void run() {
        String name = thread.getName();
        for(int i=0; i<10000; i++){
            System.out.print(name);
            try{
                Thread.sleep(0);
            }
            catch(InterruptedException e){
                Logger.getLogger(ThreadPrintName2.class.getName()).log(Level.SEVERE, null, e);
            }
        }
        
    }

}
