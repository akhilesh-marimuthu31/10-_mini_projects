# Stopwatch Application in Python using Tkinter
# This program creates a simple stopwatch with Start, Stop, and Reset functionality.
# It tracks the time in the format HH:MM:SS and allows users to interact with the GUI.

import tkinter as tk  # Importing tkinter for creating GUI elements

class Stopwatch:
    def __init__(self, root):
        # Initialize the stopwatch with the main window (root) and other UI elements
        self.root = root
        self.root.title("Stopwatch")  # Set the window title
        self.root.geometry("300x200")  # Set the window size
        
        self.is_running = False  # To check if the stopwatch is currently running
        self.counter = 0  # Keeps track of elapsed time in seconds
        
        # Label to display time in HH:MM:SS format
        self.time_label = tk.Label(root, text="00:00:00", font=("Arial", 30))
        self.time_label.pack(pady=20)  # Padding around the label for spacing

        # Start Button to start the stopwatch
        self.start_button = tk.Button(root, text="Start", command=self.start, font=("Arial", 12))
        self.start_button.pack(side=tk.LEFT, padx=20)  # Place the button on the left side

        # Stop Button to pause the stopwatch
        self.stop_button = tk.Button(root, text="Stop", command=self.stop, font=("Arial", 12))
        self.stop_button.pack(side=tk.LEFT, padx=20)  # Place the button on the left side

        # Reset Button to reset the stopwatch back to 00:00:00
        self.reset_button = tk.Button(root, text="Reset", command=self.reset, font=("Arial", 12))
        self.reset_button.pack(side=tk.LEFT, padx=20)  # Place the button on the left side

    def update_time(self):
        """Updates the time displayed every second"""
        if self.is_running:
            # Calculate minutes, seconds, and hours from the counter
            minutes, seconds = divmod(self.counter, 60)
            hours, minutes = divmod(minutes, 60)
            
            # Format the time as HH:MM:SS
            time_format = f"{hours:02}:{minutes:02}:{seconds:02}"
            
            # Update the time label with the formatted time
            self.time_label.config(text=time_format)
            
            # Increment the counter by 1 second
            self.counter += 1
            
            # Call this method again after 1000 milliseconds (1 second)
            self.root.after(1000, self.update_time)

    def start(self):
        """Start the stopwatch if it is not already running"""
        if not self.is_running:
            self.is_running = True  # Set the running flag to True
            self.update_time()  # Begin updating the time

    def stop(self):
        """Pause the stopwatch"""
        self.is_running = False  # Set the running flag to False

    def reset(self):
        """Reset the stopwatch to 00:00:00"""
        self.is_running = False  # Stop the stopwatch
        self.counter = 0  # Reset the counter to zero
        self.time_label.config(text="00:00:00")  # Reset the displayed time


# Main part of the program
if __name__ == "__main__":
    root = tk.Tk()  # Create the main window
    stopwatch = Stopwatch(root)  # Create an instance of the Stopwatch class
    root.mainloop()  # Start the Tkinter event loop
