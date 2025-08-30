"""
Installation and Setup Guide for Train Booking System
"""

# Quick Start Guide

## Prerequisites
- Python 3.6 or higher installed on your system
- Git installed (for version control)

## Installation Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Dulshan201/Train-booking-system.git
   cd Train-booking-system
   ```

2. **Run the system:**
   ```bash
   # Interactive mode
   python main.py
   
   # Demo mode
   python demo.py
   
   # Run tests
   python test_booking_system.py
   ```

## System Features Overview

### Core Functionality
- ✅ Train search by source and destination
- ✅ Ticket booking with passenger details
- ✅ Booking cancellation and management
- ✅ Passenger booking history
- ✅ Data persistence with JSON storage

### Technical Features
- ✅ Object-oriented design
- ✅ Comprehensive error handling
- ✅ Unit test coverage
- ✅ UUID-based unique identifiers
- ✅ Real-time seat availability tracking

### Sample Data Included
The system comes with 5 pre-configured train routes:
- New York ↔ Boston (Express Mail)
- Boston → Washington (City Connect)
- Washington → Philadelphia (Metro Link)
- Philadelphia → New York (Coast Runner)
- New York → Chicago (Night Express)

## Usage Examples

### Searching for Trains
```
Source: New York
Destination: Boston
Result: Shows available trains with schedules and pricing
```

### Booking a Ticket
```
1. Search for trains
2. Select train by ID
3. Enter passenger details
4. Get booking confirmation with unique ID
```

### Managing Bookings
```
- View booking: Use booking ID
- Cancel booking: Use booking ID
- View all bookings: Use email address
```

## Troubleshooting

### Common Issues
1. **Import Error**: Ensure you're using Python 3.6+
2. **File Permission Error**: Run with appropriate permissions
3. **JSON Error**: Delete train_data.json to reset to defaults

### Support
- GitHub Issues: https://github.com/Dulshan201/Train-booking-system/issues
- Documentation: README.md in repository

## Contributing
See README.md for contribution guidelines and development setup.
