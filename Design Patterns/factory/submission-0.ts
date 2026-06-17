class Vehicle {
    getType(): string {
        throw new Error("getType method must be overridden");
    }
}

class Car extends Vehicle {
    getType(): string {
        return "Car";
    }
}

class Bike extends Vehicle {
    getType(): string {
        return "Bike";
    }
}

class Truck extends Vehicle {
    getType(): string {
        return "Truck";
    }
}

class VehicleFactory {
    createVehicle(): Vehicle {
        throw new Error("createVehicle method must be overridden");
    }
}

class CarFactory extends VehicleFactory {
    // Write your code here
    createVehicle() {
        return new Car();
    }
}

class BikeFactory extends VehicleFactory {
    // Write your code here
    createVehicle() {
        return new Bike();
    }
}

class TruckFactory extends VehicleFactory {
    // Write your code here
    createVehicle() {
        return new Truck();
    }
}
