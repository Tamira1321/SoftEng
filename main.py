from my_functions import build_person, build_experiment

def main():
    first_name = input("firstname: ")
    last_name = input("lastname: ")
    sex = input("sex (male/female): ").lower()
    age = int(input("Alter: "))

    person = build_person(first_name, last_name, sex, age)

    experiment_name = input("Experiment-name: ")
    date = input("date (DD-MM-YYYY): ")
    supervisor = input("supervisor: ")

    experiment = build_experiment(experiment_name, date, supervisor, person)

    print("\nsupject:", person)
    print("experiment:", experiment)

if __name__ == "__main__":
    main()
    