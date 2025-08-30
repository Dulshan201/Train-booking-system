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

## Advanced Configuration

### Customizing Train Data
You can modify the default train data by editing the `initialize_sample_trains()` method in `main.py`:

```python
# Add your custom trains
Train("T006", "Your Train Name", "Source City", "Destination City", 
      "HH:MM", "HH:MM", seat_count, price)
```

### Data Storage Location
By default, the system stores data in `train_data.json`. To use a custom location:

```python
# Initialize with custom data file
system = TrainBookingSystem("custom_data.json")
```

### Environment Variables
Set these optional environment variables for enhanced functionality:
- `TRAIN_DATA_PATH`: Custom path for data storage
- `DEBUG_MODE`: Enable debug logging (true/false)

## Deployment Options

### Local Development
```bash
# Standard development setup
python main.py
```

### Production Deployment
```bash
# For production environments, consider:
# 1. Using a proper database instead of JSON
# 2. Adding authentication and authorization
# 3. Implementing logging and monitoring
# 4. Adding input validation and sanitization
```

### Docker Deployment (Future Enhancement)
```dockerfile
# Dockerfile example for containerization
FROM python:3.9-slim
WORKDIR /app
COPY . .
CMD ["python", "main.py"]
```

## Performance Considerations

### Large Scale Usage
- Current JSON storage suitable for < 10,000 bookings
- For larger scale, consider migrating to:
  - SQLite for medium scale (10K-100K records)
  - PostgreSQL/MySQL for enterprise scale (100K+ records)

### Memory Optimization
- System loads all data into memory on startup
- For large datasets, consider implementing lazy loading
- Use pagination for search results with large train networks

## Security Notes

### Data Protection
- Currently stores data in plain text JSON
- For production use, implement:
  - Data encryption at rest
  - Secure passenger information handling
  - Input validation and sanitization
  - Rate limiting for API calls

### Future Security Enhancements
- User authentication system
- Role-based access control
- Audit logging for all transactions
- HTTPS/TLS encryption for web deployment

## API Documentation

### Core Classes and Methods

#### TrainBookingSystem Class
```python
# Main system initialization
system = TrainBookingSystem(data_file="train_data.json")

# Search for trains
trains = system.search_trains("Source", "Destination")

# Book a ticket
booking = system.book_ticket(train_id, passenger, journey_date)

# Cancel booking
success = system.cancel_booking(booking_id)

# Get booking details
booking = system.get_booking(booking_id)
```

#### Train Class
```python
# Create a new train
train = Train(train_id, name, source, destination, 
              departure_time, arrival_time, total_seats, price)
```

#### Passenger Class
```python
# Create passenger information
passenger = Passenger(name, age, gender, phone, email)
```

## Testing Guide

### Running Tests
```bash
# Run all tests
python test_booking_system.py

# Run with verbose output
python -m unittest test_booking_system -v

# Run specific test
python -m unittest test_booking_system.TestTrainBookingSystem.test_book_ticket
```

### Test Coverage
- ✅ Train creation and management
- ✅ Passenger information handling
- ✅ Booking process validation
- ✅ Cancellation functionality
- ✅ Data persistence and loading
- ✅ Search functionality
- ✅ Error handling scenarios

## FAQ (Frequently Asked Questions)

### Q: Can I add more trains to the system?
A: Yes! You can modify the `initialize_sample_trains()` method in `main.py` or add trains through the system interface.

### Q: How do I backup my booking data?
A: Simply copy the `train_data.json` file to a safe location. This contains all your trains and bookings.

### Q: Can multiple people use the system simultaneously?
A: Currently, the system is designed for single-user access. For multi-user scenarios, consider implementing a database backend.

### Q: How do I reset the system to default state?
A: Delete the `train_data.json` file. The system will automatically recreate it with sample data on next startup.

### Q: What happens if I lose a booking ID?
A: You can search for bookings using the passenger's email address through the "View My Bookings" option.

## Version History

### v1.0.0 (Current)
- Initial release with core booking functionality
- Command-line interface
- JSON-based data storage
- Complete test suite
- Comprehensive documentation

### Planned Features (v2.0.0)
- Web-based user interface
- Database integration (SQLite/PostgreSQL)
- Email notifications
- Payment processing integration
- Multi-language support
- Mobile app compatibility
