"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45


# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    semester_cost = annual_cost / SEMESTERS_PER_YEAR
    return semester_cost


def cost_per_month(annual_cost):
    month_cost = annual_cost / MONTHS_PER_YEAR
    return month_cost


def cost_per_day(annual_cost):
    day_cost = annual_cost / (CLASS_DAYS_PER_SEMESTER * SEMESTERS_PER_YEAR)
    return day_cost


def cost_per_credit(annual_cost, credits):
    credit_cost = ((annual_cost/SEMESTERS_PER_YEAR) / credits)
    return credit_cost


def cost_per_class(annual_cost, credits):
    cost_class = ((annual_cost/SEMESTERS_PER_YEAR) / credits) * CS1430_CREDITS / CS1430_MEETINGS_PER_SEMESTER
    return cost_class

def cost_per_minute(annual_cost, credits):
    cost_minute = ((((annual_cost/SEMESTERS_PER_YEAR) / credits) * CS1430_CREDITS )/ CS1430_MEETINGS_PER_SEMESTER) / 50
    return cost_minute
# ---- PROGRAM ----

def main():
    year_cost = float(input("Enter the total cost for one year: "))
    credits = float(input("Enter the number of credits for this semester: "))

    while True:
        # Show your menu here.
        print("Menu:")
        print("1. Calculate cost per semester")
        print("2. Calculate cost per month")
        print("3. Calculate cost per day")
        print("4. Calculate cost per credit")
        print("5. Calculate cost per class")
        print("6. Calculate cost per minute of class time")
        print("Q. Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            print(f"Cost per semester: ${cost_per_semester(year_cost):.2f}")
        elif choice == "2":
            print(f"Cost per month: ${cost_per_month(year_cost):.2f}")
        elif choice == "3":
            print(f"Cost per day: ${cost_per_day(year_cost):.2f}")
        elif choice == "4":
            print(f"Cost per credit: ${cost_per_credit(year_cost, credits):.2f}")
        elif choice == "5":
            print(f"Cost per class: ${cost_per_class(year_cost, credits):.2f}")
        elif choice == "6":
            print(f"Cost per minute of class time: ${cost_per_minute(year_cost, credits):.2f}")
        elif choice == "Q":
            break



# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
