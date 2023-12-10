public class Machine {
    private int machineId;
    private int capacity;
    private int currentLoad;

    // Constructor
    public Machine(int machineId, int capacity) {
        this.machineId = machineId;
        this.capacity = capacity;
        this.currentLoad = 0;
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

    public static void main(String[] args) {
        // Example usage
        Machine machine1 = new Machine(1, 100); // Machine with ID 1 and capacity 100
        machine1.start();
        machine1.processMaterials(50);
        machine1.processMaterials(75); // This will exceed the capacity
        machine1.stop();

        Machine machine2 = new Machine(2, 200); // Another machine with ID 2 and capacity 200
        machine2.start();
        machine2.processMaterials(150);
        machine2.stop();
    }
}
