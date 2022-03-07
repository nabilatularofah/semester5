package threadJoint_printName;

public class main {
    public static void main(String[] args) {
        System.out.println("Threads will be running");

        ThreadJoinPrintName pnt1 = new ThreadJoinPrintName("A");
        ThreadJoinPrintName pnt2 = new ThreadJoinPrintName("B");
        ThreadJoinPrintName pnt3 = new ThreadJoinPrintName("C");
        ThreadJoinPrintName pnt4 = new ThreadJoinPrintName("D");

        try{
            pnt1.thread.join();
            pnt2.thread.join();
            pnt3.thread.join();
            pnt4.thread.join();
        }
        catch(InterruptedException e){
            e.printStackTrace();
        }
        System.out.println("Threads killed.");
    }
}
