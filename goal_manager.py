from datetime import date

from storage import load_goals, save_goals


def add_goal(title, description, target_date):
    goals = load_goals()

    goal_id = max(
        [goal["id"] for goal in goals],
        default=0
    ) + 1

    goal = {
        "id": goal_id,
        "title": title,
        "description": description,
        "target_date": target_date,
        "progress": 0,
        "status": "Pending",
        "created_date": date.today().isoformat()
    }

    goals.append(goal)
    save_goals(goals)

    print("\nGoal added successfully!")


def view_goals():
    goals = load_goals()

    if not goals:
        print("\nNo goals found.")
        return

    print("\n" + "-" * 100)
    print(
        f"{'ID':<5} {'Title':<25} {'Target Date':<15} "
        f"{'Progress':<12} {'Status':<15}"
    )
    print("-" * 100)

    for goal in goals:
        print(
            f"{goal['id']:<5} "
            f"{goal['title'][:24]:<25} "
            f"{goal['target_date']:<15} "
            f"{goal['progress']}%".ljust(12) +
            f"{goal['status']:<15}"
        )

    print("-" * 100)


def search_goals(keyword):
    goals = load_goals()
    keyword = keyword.lower()

    results = [
        goal for goal in goals
        if keyword in goal["title"].lower()
        or keyword in goal["description"].lower()
    ]

    if not results:
        print("\nNo matching goals found.")
        return

    print("\nSearch Results:")

    for goal in results:
        print(
            f"\nID: {goal['id']}"
            f"\nTitle: {goal['title']}"
            f"\nDescription: {goal['description']}"
            f"\nTarget Date: {goal['target_date']}"
            f"\nProgress: {goal['progress']}%"
            f"\nStatus: {goal['status']}"
        )


def update_goal_progress(goal_id, progress):
    goals = load_goals()

    for goal in goals:
        if goal["id"] == goal_id:
            goal["progress"] = progress

            if progress == 100:
                goal["status"] = "Completed"
            elif progress == 0:
                goal["status"] = "Pending"
            else:
                goal["status"] = "In Progress"

            save_goals(goals)
            print("\nGoal progress updated successfully!")
            return

    print("\nGoal ID not found.")


def mark_goal_completed(goal_id):
    goals = load_goals()

    for goal in goals:
        if goal["id"] == goal_id:
            goal["progress"] = 100
            goal["status"] = "Completed"

            save_goals(goals)
            print("\nGoal marked as completed!")
            return

    print("\nGoal ID not found.")


def delete_goal(goal_id):
    goals = load_goals()

    updated_goals = [
        goal for goal in goals
        if goal["id"] != goal_id
    ]

    if len(updated_goals) == len(goals):
        print("\nGoal ID not found.")
        return

    save_goals(updated_goals)
    print("\nGoal deleted successfully.")


def show_statistics():
    goals = load_goals()

    if not goals:
        print("\nNo goals available for statistics.")
        return

    total_goals = len(goals)
    completed_goals = sum(
        1 for goal in goals
        if goal["status"] == "Completed"
    )
    pending_goals = sum(
        1 for goal in goals
        if goal["status"] == "Pending"
    )
    in_progress_goals = sum(
        1 for goal in goals
        if goal["status"] == "In Progress"
    )

    average_progress = sum(
        goal["progress"] for goal in goals
    ) / total_goals

    print("\n========== GOAL STATISTICS ==========")
    print(f"Total Goals: {total_goals}")
    print(f"Completed Goals: {completed_goals}")
    print(f"Pending Goals: {pending_goals}")
    print(f"In Progress Goals: {in_progress_goals}")
    print(f"Average Progress: {average_progress:.2f}%")
    print("=====================================")
