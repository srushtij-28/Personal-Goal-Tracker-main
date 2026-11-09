from storage import initialize_storage
from goal_manager import (
    add_goal,
    view_goals,
    search_goals,
    update_goal_progress,
    mark_goal_completed,
    delete_goal,
    show_statistics
)
from utils import (
    get_valid_date,
    get_valid_percentage,
    get_valid_id
)


def display_menu():
    print("\n========== PERSONAL GOAL TRACKER ==========")
    print("1. Add Goal")
    print("2. View All Goals")
    print("3. Search Goals")
    print("4. Update Goal Progress")
    print("5. Mark Goal as Completed")
    print("6. Delete Goal")
    print("7. Show Statistics")
    print("8. Exit")
    print("===========================================")


def main():
    initialize_storage()

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            title = input("Enter goal title: ").strip()
            description = input("Enter goal description: ").strip()
            target_date = get_valid_date(
                "Enter target date (YYYY-MM-DD): "
            )

            if not title:
                print("Goal title cannot be empty.")
                continue

            add_goal(title, description, target_date)

        elif choice == "2":
            view_goals()

        elif choice == "3":
            keyword = input("Enter title or description keyword: ").strip()
            search_goals(keyword)

        elif choice == "4":
            goal_id = get_valid_id("Enter goal ID: ")
            progress = get_valid_percentage(
                "Enter progress percentage (0-100): "
            )

            update_goal_progress(goal_id, progress)

        elif choice == "5":
            goal_id = get_valid_id(
                "Enter goal ID to mark completed: "
            )

            mark_goal_completed(goal_id)

        elif choice == "6":
            goal_id = get_valid_id("Enter goal ID to delete: ")
            delete_goal(goal_id)

        elif choice == "7":
            show_statistics()

        elif choice == "8":
            print("Thank you for using Personal Goal Tracker!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
