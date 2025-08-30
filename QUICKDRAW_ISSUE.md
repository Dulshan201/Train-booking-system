# Quick Issue for Quickdraw Achievement

## Issue Title: Add system status check feature

## Description:
We need a simple system status check feature that shows if the booking system is running correctly.

## Implementation:
- [ ] Add a status check method to the BookingSystem class
- [ ] Display system information (number of trains, bookings, etc.)
- [ ] Add this to the main menu

## Expected Behavior:
When user selects "System Status" from the menu, show:
- Total trains loaded
- Total bookings made
- System uptime
- Memory usage

## Solution:
This can be implemented quickly by adding a `show_system_status()` method to the main.py file.

---

**Instructions for Quickdraw Achievement:**
1. Copy this content and create a new issue on GitHub
2. Immediately implement the simple solution below
3. Close the issue within 5 minutes of creation

**Quick Solution to implement:**
```python
def show_system_status(self):
    print("\n=== SYSTEM STATUS ===")
    print(f"Total Trains: {len(self.trains)}")
    print(f"Total Bookings: {len(self.bookings)}")
    print(f"System: Online")
    print("=====================")
```
