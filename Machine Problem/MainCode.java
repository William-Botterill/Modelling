public class MainCode{
    public static void main(String[] args) {
        Machine end = new Machine(4, 50);
        Machine machine3 = new Machine(3, 50, end);
        Machine machine2 = new Machine(2, 50, machine3);
        Machine machine1 = new Machine(1, 50, machine2);
        machine1.addInventory(275);
        machine1.runInLoop();
        machine2.runInLoop();
        machine3.runInLoop();
        end.runInLoop();
    
    }
}
