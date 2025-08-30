#!/usr/bin/env python3
"""
Configuration file for Train Booking System
Contains all configurable settings and constants
"""

# System Configuration
DEFAULT_DATA_FILE = "train_data.json"
BACKUP_DATA_FILE = "train_data_backup.json"

# Display Configuration
MAX_DISPLAY_WIDTH = 100
SEPARATOR_CHAR = "="
BOOKING_CONFIRMATION_WIDTH = 50

# Business Rules
MIN_PASSENGER_AGE = 1
MAX_PASSENGER_AGE = 120
MIN_BOOKING_ADVANCE_DAYS = 0
MAX_BOOKING_ADVANCE_DAYS = 365

# Train Configuration
DEFAULT_TRAIN_CAPACITY = 100
MIN_TRAIN_CAPACITY = 10
MAX_TRAIN_CAPACITY = 500

# Pricing Configuration
MIN_TICKET_PRICE = 1.0
MAX_TICKET_PRICE = 1000.0
CURRENCY_SYMBOL = "$"

# Date and Time Formats
DATE_FORMAT = "%Y-%m-%d"
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
TIME_FORMAT = "%H:%M"

# Error Messages
ERROR_MESSAGES = {
    "INVALID_TRAIN_ID": "❌ Invalid Train ID. Please check and try again.",
    "NO_SEATS_AVAILABLE": "❌ No seats available on this train.",
    "BOOKING_NOT_FOUND": "❌ Booking not found.",
    "INVALID_DATE_FORMAT": "❌ Invalid date format. Please use YYYY-MM-DD.",
    "INVALID_AGE": f"❌ Age must be between {MIN_PASSENGER_AGE} and {MAX_PASSENGER_AGE}.",
    "EMPTY_FIELD": "❌ This field cannot be empty.",
    "INVALID_EMAIL": "❌ Please enter a valid email address."
}

# Success Messages
SUCCESS_MESSAGES = {
    "BOOKING_CONFIRMED": "✅ Booking confirmed successfully!",
    "BOOKING_CANCELLED": "✅ Booking cancelled successfully!",
    "DATA_SAVED": "✅ Data saved successfully!",
    "SYSTEM_INITIALIZED": "✅ System initialized successfully!"
}

# Menu Options
MAIN_MENU = {
    "1": "Search Trains",
    "2": "Book Ticket",
    "3": "Cancel Booking",
    "4": "View Booking",
    "5": "View My Bookings",
    "6": "Exit"
}

# System Emojis
EMOJIS = {
    "TRAIN": "🚂",
    "SEARCH": "🔍",
    "TICKET": "🎫",
    "CANCEL": "❌",
    "VIEW": "📋",
    "BOOKINGS": "📚",
    "SUCCESS": "✅",
    "ERROR": "❌",
    "WARNING": "⚠️",
    "INFO": "ℹ️",
    "USER": "👤"
}

# Development Settings
DEBUG_MODE = False
ENABLE_LOGGING = True
LOG_LEVEL = "INFO"

# Future Features (Placeholders)
ENABLE_EMAIL_NOTIFICATIONS = False
ENABLE_SMS_NOTIFICATIONS = False
ENABLE_PAYMENT_PROCESSING = False
ENABLE_SEAT_SELECTION = False
