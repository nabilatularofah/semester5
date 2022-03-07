package threadJoint_printName;

public class ThreadJoinPrintName implements Runnable {
    Thread thread;

    public ThreadJoinPrintName(String name){
        thread = new Thread(this, name);
        thread.start();
    }

    @Override
    public void run() {
        String name = thread.getName();
        for(int i=0; i<20; i++){
            System.out.println(name);
            try{
                Thread.sleep(1000);
            }
            catch(InterruptedException e){
                e.printStackTrace();
            }
        }
        
    }

}
