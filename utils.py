from datetime import datetime


def get_valid_date(prompt):
    while True:
        value = input(prompt).strip()

        try:
            parsed_date = datetime.strptime(value, "%Y-%m-%d").date()
            return parsed_date.isoformat()
        except ValueError:
            print("Invalid date. Please use YYYY-MM-DD format.")


def get_valid_percentage(prompt):
    while True:
        try:
            percentage = int(input(prompt))

            if 0 <= percentage <= 100:
                return percentage

            print("Progress must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")


def get_valid_id(prompt):
    while True:
        try:
            goal_id = int(input(prompt))

            if goal_id > 0:
                return goal_id

            print("ID must be greater than zero.")

        except ValueError:
            print("Please enter a valid numeric ID.")
