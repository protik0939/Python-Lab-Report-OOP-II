# Scenario: A delivery company uses different modes of transportation for various packages, such
# as Truck, Ship, and Plane. Each transport type has a different way of calculating the delivery
# cost, which includes parameters like weight and distance.
# -----------------------------
# Question:
# Define a base class Transport with a method calculate_cost(weight, distance). Create three
# derived classes Truck, Ship, and Plane, each implementing calculate_cost() differently based on
# the transport mode. Demonstrate polymorphism by writing a function that calculates delivery
# costs for each mode of transportation using a single list of transport objects.
#---------------------------
#Answer:
#---------------------------



# Base class
class Transport:
    def calculate_cost(self, weight, distance):
        """Abstract method to calculate delivery cost."""
        raise NotImplementedError("Subclasses must implement this method")

# Derived class for Truck
class Truck(Transport):
    def calculate_cost(self, weight, distance):
        return (weight * 5) + (distance * 2)

# Derived class for Ship
class Ship(Transport):
    def calculate_cost(self, weight, distance):
        return (weight * 3) + (distance * 1.5)

# Derived class for Plane
class Plane(Transport):
    def calculate_cost(self, weight, distance):
        return (weight * 10) + (distance * 5)

# Function to demonstrate polymorphism
def calculate_delivery_costs(transports, weight, distance):
    for transport in transports:
        print(f"{transport.__class__.__name__} Delivery Cost: ${transport.calculate_cost(weight, distance):.2f}")

# Test data
truck = Truck()
ship = Ship()
plane = Plane()

# List of transport objects
transport_modes = [truck, ship, plane]

# Demonstrate polymorphism
print("Calculating delivery costs for weight=100kg and distance=200km:")
calculate_delivery_costs(transport_modes, weight=100, distance=200)
