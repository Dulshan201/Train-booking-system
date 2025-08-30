# Quick Bug Fix for Quickdraw Achievement

## Issue Title: Fix menu choice validation message

## Description:
The error message for invalid menu choices could be more user-friendly and descriptive.

## Current Behavior:
When user enters invalid choice, shows: "❌ Invalid choice. Please try again."

## Expected Behavior:
Should show the valid range: "❌ Invalid choice. Please enter a number between 1-7."

## Quick Fix:
Update the error message in the main() function in main.py

## Solution:
```python
# Change this line:
print("❌ Invalid choice. Please try again.")

# To this:
print("❌ Invalid choice. Please enter a number between 1-7.")
```

---

**Instructions for Quickdraw Achievement:**
1. Copy this content and create a new issue on GitHub
2. Immediately implement the simple solution above
3. Close the issue within 5 minutes of creation
4. This is a very quick one-line fix!
