import tkinter as tk
import subprocess


def mark_attendance():
    # Call the attendance.py file using subprocess
    subprocess.Popen(["python", "DeepFace.py"])

# Create the main application window
root = tk.Tk()
root.title("Attendance System")

# Create a button for marking attendance
mark_button = tk.Button(root, text="Mark Attendance", command=mark_attendance)
mark_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
