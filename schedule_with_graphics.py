import time
from datetime import datetime, timedelta
import turtle
import threading

# Define the schedule
schedule = [
    ("10:00 AM", "Study Session 1"),
    ("12:00 PM", "Break"),
    ("12:15 PM", "Study Session 2"),
    ("2:15 PM", "Lunch Break"),
    ("2:45 PM", "Study Session 3"),
    ("4:15 PM", "Break"),
    ("4:30 PM", "Study Session 4"),
    ("6:00 PM", "Break"),
    ("6:30 PM", "Study Session 5"),
    ("7:30 PM", "Dinner"),
    ("8:00 PM", "Exercise"),
    ("8:30 PM", "Break"),
    ("9:00 PM", "Yoga Class"),
    ("9:45 PM", "Wind Down"),
    ("10:00 PM", "Sleep")
]

def get_time_delta(time_str):
    now = datetime.now()
    target_time = datetime.strptime(time_str, "%I:%M %p").replace(year=now.year, month=now.month, day=now.day)
    if target_time < now:
        target_time += timedelta(days=1)
    return (target_time - now).total_seconds()

def draw_text(t, text):
    t.clear()
    t.write(text, align="center", font=("Arial", 18, "bold"))

def run_schedule():
    turtle.setup(width=800, height=600)
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(0, 0)

    screen = turtle.Screen()
    screen.bgcolor("lightblue")
    screen.title("Daily Schedule")

    for time_str, activity in schedule:
        if stop_event.is_set():
            break
        time_to_wait = get_time_delta(time_str)
        draw_text(t, f"Next activity: {activity} at {time_str}")
        print(f"Next activity: {activity} at {time_str}")
        print(f"Waiting for {time_to_wait} seconds...")
        stop_event.wait(time_to_wait)
        if stop_event.is_set():
            break
        draw_text(t, f"Time for {activity}!")
        print(f"Time for {activity}!")
        if "Study" in activity:
            duration = 2 * 60 * 60  # 2 hours
        elif "Break" in activity:
            duration = 15 * 60  # 15 minutes
        elif "Lunch" in activity:
            duration = 30 * 60  # 30 minutes
        elif "Dinner" in activity:
            duration = 30 * 60  # 30 minutes
        elif "Exercise" in activity:
            duration = 30 * 60  # 30 minutes
        elif "Yoga" in activity:
            duration = 45 * 60  # 45 minutes
        elif "Wind Down" in activity:
            duration = 15 * 60  # 15 minutes
        else:
            duration = 0
        stop_event.wait(duration)
        if stop_event.is_set():
            break
        draw_text(t, f"{activity} is over. Moving to the next activity...\n")
        print(f"{activity} is over. Moving to the next activity...\n")
        time.sleep(3)  # Short pause between activities

def stop_program():
    stop_event.set()
    turtle.bye()
    print("Program stopped.")

if __name__ == "__main__":
    stop_event = threading.Event()
    schedule_thread = threading.Thread(target=run_schedule)
    schedule_thread.start()

    screen = turtle.Screen()
    screen.listen()
    screen.onkey(stop_program, "q")
    screen.mainloop()
