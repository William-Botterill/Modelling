import java.util.Random;

public class Machine {
    private int machineId;
    private int capacity;
    private int currentLoad;
    private int inventory;
    private int processTime;
    private int processVariance;
    private boolean free;
    private Machine NextMachine;

    // Constructor
    public Machine(int machineId, int capacity, Machine Next) {
        this.machineId = machineId;
        this.capacity = capacity;
        this.currentLoad = 0;
        this.inventory = 0;
        this.processTime = 5000; //(in milliseconds)
        this.processVariance = 1000; //(in milliseconds)
        this.free = true;
        this.NextMachine = Next;
    }
    
    public Machine(int machineId, int capacity) {
        this.machineId = machineId;
        this.capacity = capacity;
        this.currentLoad = 0;
        this.inventory = 0;
        this.processTime = 5000; //(in milliseconds)
        this.processVariance = 1000; //(in milliseconds)
        this.free = true;
        //this.NextMachine = Next;
    }

    // Getter for machineId
    public int getMachineId() {
        return machineId;
    }

    // Getter for capacity
    public int getCapacity() {
        return capacity;
    }

    // Getter for currentLoad
    public int getCurrentLoad() {
        return currentLoad;
    }

    //Getter for inventory
    public int getInventory(){
        return inventory;
    }

    //Getter for inventory
    public int getProcessTime(){
        return processTime;
    }

    //Getter for inventory
    public int getProcessVariance(){
        return processVariance;
    }

    public void addInventory(int mat){
        this.inventory += mat;
    } 

    // Start the machine
    public void startMachine(int load) {
        System.out.println("Machine " + machineId + " started.");
        processMaterials(load);
    }

    // Stop the machine
    public void stop() {
        System.out.println("Machine " + machineId + " stopped.");
        //runIfInventoryAvailable();
    }

    public int getRandomProcessVariance() {
        Random random = new Random();
        return (random.nextInt(2*processVariance) -processVariance);
    }
    // Process materials
    public void processMaterials(int materials) {
        free = false;
        System.out.println("Machine " + machineId + " is processing " + materials);
        int fullProcessTime = processTime + getRandomProcessVariance();
        try {
            Thread.sleep(fullProcessTime);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        free = true;
        System.out.println("Full Process Time: " + fullProcessTime);
        System.out.println("Processed materials totalling: " + materials);
        stop();
    }

    public void loadMaterials(int materials, int machineId) {
        int load;
        if (free){
            if (capacity < materials) {
                load = capacity;
            }
            else {
                load = materials;
            }
            inventory -= load;
            startMachine(load);
        }
        else{
            System.out.println("Machine is not current free");
        }
    }

    public void runIfInventoryAvailable() {
        if (inventory > 0 && free) {
            //start();
            loadMaterials(inventory, 1);
            
            System.out.println("Inventory: " + inventory);
        } else {
            System.out.println("Machine " + machineId + " cannot run. Inventory is empty.");
        }
        try {
            Thread.sleep(1000);
        } catch (Exception e) {
            // TODO: handle exception
        }
        runIfInventoryAvailable();
    }

    public void runInLoop() {
        Thread thread = new Thread(() -> {
            while (true) {
                runIfInventoryAvailable();
                try {
                    // Sleep for a specific duration before checking again
                    Thread.sleep(1000); // Adjust the sleep duration as needed (in milliseconds)
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        });

        // Start the thread
        thread.start();
    }

    public static void main(String[] args) {
        
    }
}
