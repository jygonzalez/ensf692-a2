# input_processing.py
# YAEL GONZALEZ, ENSF 692 P24
# A terminal-based program for processing computer vision changes detected by a car.
# You may add your own additional classes, functions, variables, etc. as long as they do not contradict the requirements (i.e. no global variables, etc.). 
# You may import any modules from the standard Python library.
# Remember to include your name and comments.

# No global variables are permitted

# You do not need to provide additional commenting above this class, just the user-defined functions within the class


#TODO: Add comments to explain logic
class Sensor:
    """
    Sensor class to track the status of traffic light, pedestrian, and vehicle.
    """

    # Must include a constructor that uses default values
    # You do not need to provide commenting above the constructor
    def __init__(self, traffic_light="green", pedestrian="no", vehicle="no"):
        """
        Initializes the sensor with default values for traffic_light, pedestrian, and vehicle.
        """
        self.traffic_light = traffic_light
        self.pedestrian = pedestrian
        self.vehicle = vehicle        

    # Replace these comments with your function commenting
    def update_status(self, traffic_light=None, pedestrian=None, vehicle=None): # You may decide how to implement the arguments for this function
        """
        Updates the sensor status based on the provided parameters.
        Only updates parameters that are not None and are valid.
        """
        if traffic_light is not None:
            if traffic_light in ("green", "yellow", "red"):
                self.traffic_light = traffic_light
            else:
                print("Invalid vision change.")

        if pedestrian is not None:
            if pedestrian in ("yes", "no"):
                self.pedestrian = pedestrian
            else:
                print("Invalid vision change.")

        if vehicle is not None:
            if vehicle in ("yes", "no"):
                self.vehicle = vehicle
            else:
                print("Invalid vision change.")

# The sensor object should be passed to this function to print the action message and current status
# Replace these comments with your function commenting
def print_message(sensor):
    """
    Prints an action message and the current status of the sensor.
    """
    if sensor.traffic_light == "red" or sensor.pedestrian == "yes" or sensor.vehicle == "yes":
        print("\nSTOP\n")
    elif sensor.traffic_light == "green":
        print("\nProceed\n")
    else:
        print("\nCaution\n")
    print(f"Light = {sensor.traffic_light} , Pedestrian = {sensor.pedestrian} , Vehicle = {sensor.vehicle} .\n")


def main():
    """
    Main function to run the Car Vision Detector Processing Program.
    """
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")
    sensor = Sensor()

    while True:   
        print("Are changes are detected in the vision input?")     
        selection = input("Select 1 for light, 2 for pedestrian, 3 for vehicle, or 0 to end the program: ")
        
        try:
            if selection not in ('0', '1', '2', '3'):
                raise ValueError("You must select either 1, 2, 3 or 0.")
        except ValueError as err:
            print(err, "\n")
            continue

        if (selection is "0"):
            break     

        change = input("What change has been identified?: ")

        match(selection):
            case "1":
                sensor.update_status(traffic_light=change)
            case "2":
                sensor.update_status(pedestrian=change)
            case "3":
                sensor.update_status(vehicle=change)
        
        print_message(sensor)
   

if __name__ == '__main__':
    main()
