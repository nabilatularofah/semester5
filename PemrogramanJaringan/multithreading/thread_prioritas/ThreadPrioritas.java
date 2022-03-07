package thread_prioritas;

public class ThreadPrioritas extends Thread {
    private int hitungmundur = 5;
    private volatile double d = 0;

    public ThreadPrioritas(int prioritas){
        setPriority(prioritas);start();
    }
@Override
public void run(){
    while(true){
        for(int i=0; i <10000000; i++){
            d = + (Math.PI + Math.E) / (double)i;
        }
        System.out.println(this.toString() + ":" + hitungmundur + "-->" + d);
        if(--hitungmundur == 0){
            return;
        }
    }
}
}
