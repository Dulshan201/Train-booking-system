#!/usr/bin/env python3
"""
Utility functions for Train Booking System
Contains helper functions and common operations
"""

import json
import uuid
from datetime import datetime, timedelta
from typing import List, Dict, Optional

def generate_booking_id() -> str:
    """Generate a unique booking ID"""
    return str(uuid.uuid4())

def generate_passenger_id() -> str:
    """Generate a unique passenger ID"""
    return str(uuid.uuid4())

def format_currency(amount: float, currency: str = "$") -> str:
    """Format currency with proper symbol and decimal places"""
    return f"{currency}{amount:.2f}"

def validate_email(email: str) -> bool:
    """Basic email validation"""
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_phone(phone: str) -> bool:
    """Basic phone number validation"""
    import re
    # Remove all non-digit characters
    digits_only = re.sub(r'\D', '', phone)
    # Check if it has 10-15 digits
    return 10 <= len(digits_only) <= 15

def validate_age(age: int) -> bool:
    """Validate passenger age"""
    return 1 <= age <= 120

def format_date(date_str: str) -> str:
    """Format date string for display"""
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return date_obj.strftime("%B %d, %Y")
    except ValueError:
        return date_str

def format_time(time_str: str) -> str:
    """Format time string for display"""
    try:
        time_obj = datetime.strptime(time_str, "%H:%M")
        return time_obj.strftime("%I:%M %p")
    except ValueError:
        return time_str

def calculate_journey_duration(departure: str, arrival: str) -> str:
    """Calculate journey duration between departure and arrival times"""
    try:
        # Handle next day arrivals (marked with +1)
        if arrival.endswith('+1'):
            arrival_clean = arrival[:-2]
            dep_time = datetime.strptime(departure, "%H:%M")
            arr_time = datetime.strptime(arrival_clean, "%H:%M")
            # Add 24 hours for next day
            arr_time += timedelta(days=1)
        else:
            dep_time = datetime.strptime(departure, "%H:%M")
            arr_time = datetime.strptime(arrival, "%H:%M")
        
        duration = arr_time - dep_time
        hours = duration.seconds // 3600
        minutes = (duration.seconds % 3600) // 60
        
        if duration.days > 0:
            hours += duration.days * 24
        
        if hours > 0 and minutes > 0:
            return f"{hours}h {minutes}m"
        elif hours > 0:
            return f"{hours}h"
        else:
            return f"{minutes}m"
    except ValueError:
        return "Unknown"

def sanitize_input(input_str: str) -> str:
    """Sanitize user input by removing dangerous characters"""
    if not input_str:
        return ""
    
    # Remove potentially dangerous characters
    dangerous_chars = ['<', '>', '"', "'", '&', '\n', '\r', '\t']
    cleaned = input_str
    for char in dangerous_chars:
        cleaned = cleaned.replace(char, '')
    
    return cleaned.strip()

def format_passenger_name(name: str) -> str:
    """Format passenger name to title case"""
    return sanitize_input(name).title()

def generate_ticket_number() -> str:
    """Generate a formatted ticket number"""
    timestamp = datetime.now().strftime("%Y%m%d%H%M")
    random_part = str(uuid.uuid4())[:8].upper()
    return f"TKT-{timestamp}-{random_part}"

def backup_data(source_file: str, backup_suffix: str = "backup") -> bool:
    """Create a backup of the data file"""
    try:
        import shutil
        backup_file = f"{source_file}.{backup_suffix}"
        shutil.copy2(source_file, backup_file)
        return True
    except Exception as e:
        print(f"Backup failed: {e}")
        return False

def restore_data(backup_file: str, target_file: str) -> bool:
    """Restore data from backup file"""
    try:
        import shutil
        shutil.copy2(backup_file, target_file)
        return True
    except Exception as e:
        print(f"Restore failed: {e}")
        return False

def calculate_seat_utilization(total_seats: int, available_seats: int) -> float:
    """Calculate seat utilization percentage"""
    if total_seats <= 0:
        return 0.0
    occupied_seats = total_seats - available_seats
    return (occupied_seats / total_seats) * 100

def get_next_available_train_id(existing_ids: List[str]) -> str:
    """Generate next available train ID"""
    base = "T"
    counter = 1
    while f"{base}{counter:03d}" in existing_ids:
        counter += 1
    return f"{base}{counter:03d}"

def format_booking_summary(booking_data: Dict) -> str:
    """Format booking data into a readable summary"""
    summary = f"""
📋 BOOKING SUMMARY
==================
Booking ID: {booking_data.get('booking_id', 'N/A')}
Passenger: {booking_data.get('passenger_name', 'N/A')}
Train: {booking_data.get('train_name', 'N/A')} ({booking_data.get('train_id', 'N/A')})
Route: {booking_data.get('source', 'N/A')} → {booking_data.get('destination', 'N/A')}
Journey Date: {format_date(booking_data.get('journey_date', ''))}
Departure: {format_time(booking_data.get('departure_time', ''))}
Arrival: {format_time(booking_data.get('arrival_time', ''))}
Price: {format_currency(booking_data.get('price', 0))}
Status: {booking_data.get('status', 'Unknown')}
==================
"""
    return summary

class DataValidator:
    """Data validation utility class"""
    
    @staticmethod
    def validate_train_data(train_data: Dict) -> List[str]:
        """Validate train data and return list of errors"""
        errors = []
        
        required_fields = ['train_id', 'name', 'source', 'destination', 
                          'departure_time', 'arrival_time', 'total_seats', 'price']
        
        for field in required_fields:
            if field not in train_data or not train_data[field]:
                errors.append(f"Missing required field: {field}")
        
        if 'total_seats' in train_data:
            if not isinstance(train_data['total_seats'], int) or train_data['total_seats'] <= 0:
                errors.append("Total seats must be a positive integer")
        
        if 'price' in train_data:
            if not isinstance(train_data['price'], (int, float)) or train_data['price'] <= 0:
                errors.append("Price must be a positive number")
        
        return errors
    
    @staticmethod
    def validate_passenger_data(passenger_data: Dict) -> List[str]:
        """Validate passenger data and return list of errors"""
        errors = []
        
        required_fields = ['name', 'age', 'gender', 'phone', 'email']
        
        for field in required_fields:
            if field not in passenger_data or not passenger_data[field]:
                errors.append(f"Missing required field: {field}")
        
        if 'age' in passenger_data:
            if not validate_age(passenger_data['age']):
                errors.append("Age must be between 1 and 120")
        
        if 'email' in passenger_data:
            if not validate_email(passenger_data['email']):
                errors.append("Invalid email format")
        
        if 'phone' in passenger_data:
            if not validate_phone(passenger_data['phone']):
                errors.append("Invalid phone number format")
        
        return errors

def log_system_event(event: str, details: Dict = None) -> None:
    """Log system events for debugging and monitoring"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {event}"
    
    if details:
        log_entry += f" - Details: {json.dumps(details, default=str)}"
    
    # In a production system, this would write to a proper log file
    print(f"LOG: {log_entry}")

# Constants for the utility module
SUPPORTED_CURRENCIES = ["$", "€", "£", "¥", "₹"]
MAX_PASSENGER_NAME_LENGTH = 100
MAX_TRAIN_NAME_LENGTH = 50
MAX_STATION_NAME_LENGTH = 50
