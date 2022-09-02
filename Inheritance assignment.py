class Vehicle:
    # Define attributes of parent
    fuel = "No fuel type specified"
    Color = ""
    Weight = ""

class Boat(Vehicle):
    boat_shape="v-shaped"
    motor_type="outboard"

class Airplane(Vehicle):
    wings=2
    plane_type="jet"
