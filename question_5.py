# Task 1
activities = ["Running", "Swimming", "Weights", "Biking"]
duration = ["5", "10", "15", "20"]
exercise_time = 0
running_time = 0
swimming_time = 0
weights_time = 0
biking_time = 0

def log_activities_and_duration():
    global exercise_time
    while True:
        print("\nWorkout Management System")
        print(f"1. {activities[0]}")
        print(f"2. {activities[1]}")
        print(f"3. {activities[2]}")
        print(f"4. {activities[3]}")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            global running_time
            print(f"1. {duration[0]}")
            print(f"2. {duration[1]}")
            print(f"3. {duration[2]}")
            print(f"4. {duration[3]}")
            print("5. Exit")
            time = input("How long did you run for? ")
            if time == "1":
                exercise_time += 5
                running_time += 5
            elif time == "2":
                exercise_time += 10
                running_time += 10
            elif time == "3":
                exercise_time += 15
                running_time += 15
            elif time == "4":
                exercise_time += 20
                running_time += 20
            elif time == "5":
                break
        elif choice == "2":
            global swimming_time
            print(f"1. {duration[0]}")
            print(f"2. {duration[1]}")
            print(f"3. {duration[2]}")
            print(f"4. {duration[3]}")
            print("5. Exit")
            time = input("How long did you swim for? ")
            if time == "1":
                exercise_time += 5
                swimming_time += 5
            elif time == "2":
                exercise_time += 10
                swimming_time += 10
            elif time == "3":
                exercise_time += 15
                swimming_time += 15
            elif time == "4":
                exercise_time += 20
                swimming_time += 20
            elif time == "5":
                break
        elif choice == "3":
            global weights_time
            print(f"1. {duration[0]}")
            print(f"2. {duration[1]}")
            print(f"3. {duration[2]}")
            print(f"4. {duration[3]}")
            print("5. Exit")
            time = input("How long did you lift weights for? ")
            if time == "1":
                exercise_time += 5
                weights_time += 5
            elif time == "2":
                exercise_time += 10
                weights_time += 10
            elif time == "3":
                exercise_time += 15
                weights_time += 15
            elif time == "4":
                exercise_time += 20
                weights_time += 20
            elif time == "5":
                break
        elif choice == "4":
            global biking_time
            print(f"1. {duration[0]}")
            print(f"2. {duration[1]}")
            print(f"3. {duration[2]}")
            print(f"4. {duration[3]}")
            print("5. Exit")
            time = input("How long did you run for? ")
            if time == "1":
                exercise_time += 5
                biking_time += 5
            elif time == "2":
                exercise_time += 10
                biking_time += 10
            elif time == "3":
                exercise_time += 15
                biking_time += 15
            elif time == "4":
                exercise_time += 20
                biking_time += 20
            elif time == "5":
                break
        elif choice == "5":
            print(f"You exercised for {exercise_time} minutes")
            break

# Task 2

def calories_burned():
    total_burned = (running_time * 3.5) + (swimming_time * 4) + (weights_time * 4.5) + (biking_time * 5.2)
    print(f"You burned {total_burned} calories!")

# Task 3

log_activities_and_duration()



def summary():
    print(f"You ran for {running_time} minutes")
    print(f"You swam for {swimming_time} minutes")
    print(f"You lifted weights for {weights_time} minutes")
    print(f"You biked for {biking_time} minutes")

summary()
calories_burned()
