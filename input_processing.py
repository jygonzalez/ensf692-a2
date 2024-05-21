# input_processing.py
# YAEL GONZALEZ, ENSF 692 P24
# A terminal-based program for processing computer vision changes detected by a car.

class Sensor:
    """
    Sensor class to track the status of traffic light, pedestrian, and vehicle.
    """

    def __init__(self, traffic_light="green", pedestrian="no", vehicle="no"):
        """
        Initializes the sensor with default values for traffic_light, pedestrian, and vehicle.
        """
        self.traffic_light = traffic_light
        self.pedestrian = pedestrian
        self.vehicle = vehicle        

    def update_status(self, traffic_light=None, pedestrian=None, vehicle=None):
        """
        Updates the sensor status based on the provided parameters.
        Only updates parameters that are not None and are valid.
        """
        # Each status is set to None by default. If a status value is passed (i.e., different than None),
        # then the status will be validated through the tuple. If the status is valid, then the instance
        # variable for the sensor will get updated. If the status is invalid, a message will be printed.
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


def print_message(sensor):
    """
    Prints an action message and the current status of the sensor.
    """
    # STOP message if there is either a red light, a pedestrian or a vehicle. For other messages the light 
    # only must be checked, because if pedestrian or vehicle it falls under the STOP message category. 
    if sensor.traffic_light == "red" or sensor.pedestrian == "yes" or sensor.vehicle == "yes":
        print("\nSTOP\n")
    elif sensor.traffic_light == "yellow":
        print("\nCaution\n")
    else:
        print("\nProceed\n")
    print(f"Light = {sensor.traffic_light} , Pedestrian = {sensor.pedestrian} , Vehicle = {sensor.vehicle} .\n")


def main():
    """
    Main function to run the Car Vision Detector Processing Program.
    """
    # Step 1. Greet the user and instantiate the Sensor object
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")
    sensor = Sensor()

    while True:
        # Step 2. Ask the user for changes in the vision input and store in "selection" variable   
        print("Are changes are detected in the vision input?")     
        selection = input("Select 1 for light, 2 for pedestrian, 3 for vehicle, or 0 to end the program: ")
        
        # Step 3. Validate the selection.
        try:
            if selection not in ('0', '1', '2', '3'): # Use a tuple to validate selection
                raise ValueError("You must select either 1, 2, 3 or 0.") # Raise exception if invalid
        except ValueError as err:
            print(err, "\n") # Handle exception and display message 
            continue # Restart the program at this stage

        # Step 4. Process user's selection from the options
        if (selection is "0"): # First, quit the program if user selected '0'
            break     
        
        # Store the identified change in the "change" variable
        change = input("What change has been identified?: ")

        # Use a switch/case method to process the selection, i.e., update the sensor status. No need for a 
        # default case (selection has been validated already) 
        match(selection): 
            case "1":
                sensor.update_status(traffic_light=change)
            case "2":
                sensor.update_status(pedestrian=change)
            case "3":
                sensor.update_status(vehicle=change)
        
       # Step 5. Print the appropriate action message given the current instance variables values
        print_message(sensor)
   

if __name__ == '__main__':
    main()
