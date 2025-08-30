#!/usr/bin/env python3
"""
Test suite for Train Booking System
"""

import unittest
import json
import os
import tempfile
from datetime import datetime
from main import Train, Passenger, Booking, TrainBookingSystem

class TestTrainBookingSystem(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        # Create a temporary file for testing
        self.test_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json')
        self.test_file.close()
        self.system = TrainBookingSystem(self.test_file.name)
    
    def tearDown(self):
        """Clean up after each test method."""
        # Remove the temporary file
        if os.path.exists(self.test_file.name):
            os.unlink(self.test_file.name)
    
    def test_train_creation(self):
        """Test Train class creation and methods."""
        train = Train("T001", "Express", "NYC", "Boston", "08:00", "12:00", 100, 50.0)
        self.assertEqual(train.train_id, "T001")
        self.assertEqual(train.name, "Express")
        self.assertEqual(train.available_seats, 100)
        self.assertEqual(train.price, 50.0)
    
    def test_passenger_creation(self):
        """Test Passenger class creation."""
        passenger = Passenger("John Doe", 30, "M", "1234567890", "john@example.com")
        self.assertEqual(passenger.name, "John Doe")
        self.assertEqual(passenger.age, 30)
        self.assertIsNotNone(passenger.passenger_id)
    
    def test_search_trains(self):
        """Test train search functionality."""
        trains = self.system.search_trains("New York", "Boston")
        self.assertTrue(len(trains) > 0)
        
        # Test case insensitive search
        trains_lower = self.system.search_trains("new york", "boston")
        self.assertEqual(len(trains), len(trains_lower))
    
    def test_book_ticket(self):
        """Test ticket booking functionality."""
        passenger = Passenger("Alice Smith", 25, "F", "9876543210", "alice@example.com")
        
        # Get a train to book
        trains = self.system.search_trains("New York", "Boston")
        self.assertTrue(len(trains) > 0)
        
        train = trains[0]
        initial_seats = train.available_seats
        
        booking = self.system.book_ticket(train.train_id, passenger, "2025-09-01")
        
        self.assertIsNotNone(booking)
        self.assertEqual(booking.train_id, train.train_id)
        self.assertEqual(booking.passenger.name, "Alice Smith")
        self.assertEqual(train.available_seats, initial_seats - 1)
    
    def test_cancel_booking(self):
        """Test booking cancellation."""
        passenger = Passenger("Bob Johnson", 35, "M", "5555555555", "bob@example.com")
        
        trains = self.system.search_trains("New York", "Boston")
        train = trains[0]
        initial_seats = train.available_seats
        
        # Book a ticket
        booking = self.system.book_ticket(train.train_id, passenger, "2025-09-01")
        self.assertIsNotNone(booking)
        
        # Cancel the booking
        success = self.system.cancel_booking(booking.booking_id)
        self.assertTrue(success)
        self.assertEqual(train.available_seats, initial_seats)
        
        # Check booking status
        cancelled_booking = self.system.get_booking(booking.booking_id)
        self.assertEqual(cancelled_booking.status, "Cancelled")
    
    def test_get_passenger_bookings(self):
        """Test retrieving passenger bookings by email."""
        passenger = Passenger("Carol Davis", 28, "F", "7777777777", "carol@example.com")
        
        trains = self.system.search_trains("New York", "Boston")
        train = trains[0]
        
        # Book multiple tickets
        booking1 = self.system.book_ticket(train.train_id, passenger, "2025-09-01")
        booking2 = self.system.book_ticket(train.train_id, passenger, "2025-09-02")
        
        bookings = self.system.get_passenger_bookings("carol@example.com")
        self.assertEqual(len(bookings), 2)
    
    def test_data_persistence(self):
        """Test saving and loading data."""
        passenger = Passenger("Dave Wilson", 40, "M", "8888888888", "dave@example.com")
        
        trains = self.system.search_trains("New York", "Boston")
        train = trains[0]
        
        booking = self.system.book_ticket(train.train_id, passenger, "2025-09-01")
        
        # Create a new system instance with the same data file
        new_system = TrainBookingSystem(self.test_file.name)
        
        # Check if booking exists in new system
        retrieved_booking = new_system.get_booking(booking.booking_id)
        self.assertIsNotNone(retrieved_booking)
        self.assertEqual(retrieved_booking.passenger.name, "Dave Wilson")
    
    def test_invalid_booking(self):
        """Test booking with invalid train ID."""
        passenger = Passenger("Invalid User", 25, "M", "0000000000", "invalid@example.com")
        
        booking = self.system.book_ticket("INVALID", passenger, "2025-09-01")
        self.assertIsNone(booking)
    
    def test_booking_full_train(self):
        """Test booking when no seats available."""
        # Create a train with only 1 seat
        full_train = Train("FULL", "Full Train", "A", "B", "10:00", "11:00", 1, 10.0)
        self.system.trains["FULL"] = full_train
        
        passenger1 = Passenger("First", 25, "M", "1111111111", "first@example.com")
        passenger2 = Passenger("Second", 30, "F", "2222222222", "second@example.com")
        
        # Book the only seat
        booking1 = self.system.book_ticket("FULL", passenger1, "2025-09-01")
        self.assertIsNotNone(booking1)
        
        # Try to book when full
        booking2 = self.system.book_ticket("FULL", passenger2, "2025-09-01")
        self.assertIsNone(booking2)

def run_tests():
    """Run all tests."""
    unittest.main()

if __name__ == "__main__":
    run_tests()
