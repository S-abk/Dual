import time
from tkinter import Tk, Label, Button

# Splash screen function
def show_splash_screen(root, time_in_seconds):
  splash_label = Label(root, text="Program Starting...", font=("Arial", 20))
  splash_label.pack()
  root.update()
  time.sleep(time_in_seconds)
  splash_label.destroy()
  root.destroy()

# Timer function with user input for minutes
def start_timer():
  root = Tk()
  root.withdraw()  # Hide the main window

  # Get user input for minutes
  minutes = int(input("Enter the number of minutes: "))
  seconds = minutes * 60

  show_splash_screen(Tk(), 2)  # Show splash screen for 2 seconds

  # Timer loop
  while seconds > 0:
    remaining_minutes = int(seconds / 60)
    remaining_seconds = seconds % 60
    print(f"Time remaining: {remaining_minutes} minutes {remaining_seconds} seconds")
    time.sleep(1)
    seconds -= 1

  print("Timer finished!")

if __name__ == "__main__":
  start_timer()
