public class Machine {
    private int machineId;
    private int capacity;
    private int currentLoad;
    private int inventory;
    private int processTime;
    private int processVariance;
    private boolean free;

    // Constructor
    public Machine(int machineId, int capacity) {
        this.machineId = machineId;
        this.capacity = capacity;
        this.currentLoad = 0;
        this.inventory = 0;
        this.processTime = 0;
        this.processVariance = 0;
        this.free = true;
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
    public void start() {
        System.out.println("Machine " + machineId + " started.");
    }

    // Stop the machine
    public void stop() {
        System.out.println("Machine " + machineId + " stopped.");
    }

    // Process materials
    public void processMaterials(int materials) {
        if (currentLoad + materials <= capacity) {
            currentLoad += materials;
            System.out.println("Machine " + machineId + " is processing " + materials + " materials. Current load: " + currentLoad);
        } else {
            System.out.println("Machine " + machineId + " cannot process more materials. Capacity exceeded.");
        }
    }

    public void runIfInventoryAvailable() {
        if (inventory > 0 && free) {
            start();
            processMaterials(inventory);
            stop();
            inventory = inventory - capacity;
            if (inventory < 0) {
                inventory = 0;
            }
            System.out.println("Inventory: " + inventory);
        } else {
            System.out.println("Machine " + machineId + " cannot run. Inventory is empty.");
        }
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
        Machine machine1 = new Machine(1, 50);
        machine1.addInventory(50);
        machine1.addInventory(75);
        machine1.runInLoop();

    }
}
