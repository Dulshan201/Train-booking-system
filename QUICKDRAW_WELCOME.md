# Super Quick Enhancement for Quickdraw Achievement

## Issue Title: Add welcome message on startup

## Description:
Add a nice welcome message when the system starts to make it more user-friendly.

## Current Behavior:
System starts directly with the menu

## Expected Behavior:
Show a welcome message before the first menu display

## Quick Fix:
Add 2 lines at the start of the main() function in main.py

## Solution:
```python
def main():
    """Main function to run the train booking system"""
    system = TrainBookingSystem()
    
    # Add these 2 lines:
    print("🎉 Welcome to the Train Booking System! 🎉")
    print("Let's help you book your perfect journey!\n")
    
    while True:
        # ... rest of the code
```

---

**Instructions for Quickdraw Achievement:**
1. Copy this content and create a new issue on GitHub
2. Immediately add the 2 welcome lines
3. Close the issue within 5 minutes of creation
4. This is literally a 2-line addition!
