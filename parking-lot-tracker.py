class ParkingSpace:
    def __init__(self, levels, spots_per_level):
        self.levels = {
            level: {spot: None for spot in range(1, spots_per_level + 1)}
            for level in levels
        }

    def assign_parking_space(self, vehicle_number):
        for level, spots in self.levels.items():
            for spot, occupied_by in spots.items():
                if occupied_by is None:
                    self.levels[level][spot] = vehicle_number
                    return {"level": level, "spot": spot}
                elif occupied_by == vehicle_number:
                    return {"level": level, "spot": spot}

        return None

    def retrieve_parking_spot(self, vehicle_number):
        for level, spots in self.levels.items():
            if vehicle_number in spots.values():
                spot = list(spots.values()).index(vehicle_number) + 1
                return {"level": level, "spot": spot}
        return None


class ParkingLotTracker:
    def __init__(self, levels, spots_per_level):
        self.parking_lot = ParkingSpace(levels, spots_per_level)

    def run(self):
        while True:
            print("1. Assign Parking Space")
            print("2. Retrieve Parking Spot")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                vehicle_number = input("Enter vehicle number: ")
                result = self.parking_lot.assign_parking_space(vehicle_number)
                if result:
                    print(f"Parking Space assigned: {result}")
                else:
                    print("Parking lot is full.")
            elif choice == "2":
                vehicle_number = input("Enter vehicle number: ")
                result = self.parking_lot.retrieve_parking_spot(vehicle_number)
                if result:
                    print(f"Parked at: {result}")
                else:
                    print(f"{vehicle_number} not found in the parking lot.")
            elif choice == "3":
                break
            else:
                print("Invalid choice.")


if __name__ == "__main__":
    levels = ["A", "B"]
    spots_per_level = 20

    parking_app = ParkingLotTracker(levels, spots_per_level)
    parking_app.run()
