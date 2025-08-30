# 🚂 Train Booking System

A comprehensive train ticket booking and management system built with Python. This system allows users to search for trains, book tickets, manage bookings, and view their travel history.

## ✨ Features

- 🔍 **Train Search**: Search for trains between different stations
- 🎫 **Ticket Booking**: Book train tickets with passenger details
- ❌ **Booking Cancellation**: Cancel existing bookings
- 📋 **Booking Management**: View booking details and history
- 💾 **Data Persistence**: All data is saved to JSON files
- 🏗️ **Object-Oriented Design**: Clean, modular code structure

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher
- No additional dependencies required (uses only standard library)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Dulshan201/Train-booking-system.git
cd Train-booking-system
```

2. Run the application:
```bash
python main.py
```

## 🎮 How to Use

### Main Menu Options

1. **Search Trains**: Find available trains between stations
2. **Book Ticket**: Reserve a seat on your chosen train
3. **Cancel Booking**: Cancel an existing reservation
4. **View Booking**: Check details of a specific booking
5. **View My Bookings**: See all your bookings by email
6. **Exit**: Close the application

### Sample Usage

#### Searching for Trains
- Enter source and destination stations
- View available trains with schedules and prices

#### Booking a Ticket
- Search for trains on your route
- Select a train by entering its Train ID
- Fill in passenger details:
  - Name
  - Age
  - Gender
  - Phone number
  - Email address
  - Journey date
- Receive booking confirmation with unique Booking ID

#### Managing Bookings
- Use your Booking ID to view or cancel reservations
- Use your email to see all your bookings

## 🏗️ System Architecture

### Classes

- **Train**: Represents a train with route, schedule, and seat information
- **Passenger**: Stores passenger information
- **Booking**: Links passengers to trains with booking details
- **TrainBookingSystem**: Main system class that manages all operations

### Data Storage

- All data is stored in `train_data.json`
- Automatic data persistence after each operation
- Sample trains are automatically created on first run

## 📊 Sample Data

The system comes pre-loaded with sample trains:

| Train ID | Name | Route | Departure | Arrival | Seats | Price |
|----------|------|-------|-----------|---------|-------|-------|
| T001 | Express Mail | New York → Boston | 08:00 | 12:00 | 100 | $50.00 |
| T002 | City Connect | Boston → Washington | 14:00 | 18:30 | 80 | $65.00 |
| T003 | Metro Link | Washington → Philadelphia | 10:30 | 13:15 | 120 | $45.00 |
| T004 | Coast Runner | Philadelphia → New York | 16:00 | 19:45 | 90 | $55.00 |
| T005 | Night Express | New York → Chicago | 22:00 | 08:00+1 | 150 | $120.00 |

## 🔧 Features in Detail

### Smart Search
- Case-insensitive station name matching
- Real-time seat availability checking
- Comprehensive train information display

### Secure Booking
- Unique booking IDs using UUID
- Automatic seat count management
- Timestamp tracking for all bookings

### Data Integrity
- JSON-based data persistence
- Error handling for data corruption
- Automatic backup and recovery

## 📁 Project Structure

```
train-booking-system/
│
├── main.py              # Main application file
├── train_data.json      # Data storage (auto-generated)
├── README.md           # Project documentation
├── requirements.txt    # Python dependencies
└── .gitignore         # Git ignore file
```

## 🛠️ Technical Details

- **Language**: Python 3.6+
- **Data Format**: JSON
- **Architecture**: Object-Oriented Programming
- **Storage**: File-based (JSON)
- **Dependencies**: Standard Library Only

## 🔮 Future Enhancements

- 🌐 Web-based interface
- 💳 Payment gateway integration
- 📱 Mobile app support
- 🎯 Seat selection feature
- 📧 Email notifications
- 📊 Analytics dashboard
- 🗄️ Database integration
- 🔐 User authentication system

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👥 Authors

- **Dulshan201** - *Initial work* - [GitHub](https://github.com/Dulshan201)
- **TheAkila** - *Contributor* - [GitHub](https://github.com/TheAkila)

## 📞 Support

If you have any questions or need help with the system, please:

1. Check the documentation above
2. Look through existing [issues](https://github.com/Dulshan201/Train-booking-system/issues)
3. Create a new issue if your question isn't answered

## 🎯 Version History

- **v1.0.0** - Initial release with core booking functionality
  - Train search and booking
  - Passenger management
  - Data persistence
  - Command-line interface

---

**Happy Traveling! 🚂✨**

Made with ❤️ by [Dulshan201](https://github.com/Dulshan201) and [TheAkila](https://github.com/TheAkila)
