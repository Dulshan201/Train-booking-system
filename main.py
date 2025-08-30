#!/usr/bin/env python3
"""
Train Booking System
A comprehensive train ticket booking and management system
"""

from datetime import datetime, timedelta
import json
import os
from typing import Dict, List, Optional
import uuid

class Train:
    def __init__(self, train_id: str, name: str, source: str, destination: str, 
                 departure_time: str, arrival_time: str, total_seats: int, price: float):
        self.train_id = train_id
        self.name = name
        self.source = source
        self.destination = destination
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.total_seats = total_seats
        self.available_seats = total_seats
        self.price = price
        self.bookings = []

    def to_dict(self):
        return {
            'train_id': self.train_id,
            'name': self.name,
            'source': self.source,
            'destination': self.destination,
            'departure_time': self.departure_time,
            'arrival_time': self.arrival_time,
            'total_seats': self.total_seats,
            'available_seats': self.available_seats,
            'price': self.price,
            'bookings': self.bookings
        }

    @classmethod
    def from_dict(cls, data):
        train = cls(
            data['train_id'], data['name'], data['source'], data['destination'],
            data['departure_time'], data['arrival_time'], data['total_seats'], data['price']
        )
        train.available_seats = data['available_seats']
        train.bookings = data['bookings']
        return train

class Passenger:
    def __init__(self, name: str, age: int, gender: str, phone: str, email: str):
        self.passenger_id = str(uuid.uuid4())
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone
        self.email = email

    def to_dict(self):
        return {
            'passenger_id': self.passenger_id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            'phone': self.phone,
            'email': self.email
        }

    @classmethod
    def from_dict(cls, data):
        passenger = cls(data['name'], data['age'], data['gender'], data['phone'], data['email'])
        passenger.passenger_id = data['passenger_id']
        return passenger

class Booking:
    def __init__(self, train_id: str, passenger: Passenger, booking_date: str, journey_date: str):
        self.booking_id = str(uuid.uuid4())
        self.train_id = train_id
        self.passenger = passenger
        self.booking_date = booking_date
        self.journey_date = journey_date
        self.status = "Confirmed"

    def to_dict(self):
        return {
            'booking_id': self.booking_id,
            'train_id': self.train_id,
            'passenger': self.passenger.to_dict(),
            'booking_date': self.booking_date,
            'journey_date': self.journey_date,
            'status': self.status
        }

    @classmethod
    def from_dict(cls, data):
        booking = cls(
            data['train_id'], 
            Passenger.from_dict(data['passenger']), 
            data['booking_date'], 
            data['journey_date']
        )
        booking.booking_id = data['booking_id']
        booking.status = data['status']
        return booking

class TrainBookingSystem:
    def __init__(self, data_file: str = "train_data.json"):
        self.data_file = data_file
        self.trains = {}
        self.bookings = {}
        self.load_data()
        self.initialize_sample_trains()

    def load_data(self):
        """Load data from JSON file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    self.trains = {tid: Train.from_dict(tdata) for tid, tdata in data.get('trains', {}).items()}
                    self.bookings = {bid: Booking.from_dict(bdata) for bid, bdata in data.get('bookings', {}).items()}
            except (json.JSONDecodeError, KeyError) as e:
                print(f"Error loading data: {e}. Starting with empty data.")
                self.trains = {}
                self.bookings = {}

    def save_data(self):
        """Save data to JSON file"""
        data = {
            'trains': {tid: train.to_dict() for tid, train in self.trains.items()},
            'bookings': {bid: booking.to_dict() for bid, booking in self.bookings.items()}
        }
        with open(self.data_file, 'w') as f:
            json.dump(data, f, indent=2)

    def initialize_sample_trains(self):
        """Initialize with sample train data if no trains exist"""
        if not self.trains:
            sample_trains = [
                Train("T001", "Express Mail", "New York", "Boston", "08:00", "12:00", 100, 50.0),
                Train("T002", "City Connect", "Boston", "Washington", "14:00", "18:30", 80, 65.0),
                Train("T003", "Metro Link", "Washington", "Philadelphia", "10:30", "13:15", 120, 45.0),
                Train("T004", "Coast Runner", "Philadelphia", "New York", "16:00", "19:45", 90, 55.0),
                Train("T005", "Night Express", "New York", "Chicago", "22:00", "08:00+1", 150, 120.0)
            ]
            
            for train in sample_trains:
                self.trains[train.train_id] = train
            self.save_data()

    def search_trains(self, source: str, destination: str, date: str = None) -> List[Train]:
        """Search for trains between source and destination"""
        results = []
        for train in self.trains.values():
            if (train.source.lower() == source.lower() and 
                train.destination.lower() == destination.lower() and 
                train.available_seats > 0):
                results.append(train)
        return results

    def book_ticket(self, train_id: str, passenger: Passenger, journey_date: str) -> Optional[Booking]:
        """Book a ticket for a passenger"""
        if train_id not in self.trains:
            return None
        
        train = self.trains[train_id]
        if train.available_seats <= 0:
            return None

        booking = Booking(train_id, passenger, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), journey_date)
        self.bookings[booking.booking_id] = booking
        train.available_seats -= 1
        train.bookings.append(booking.booking_id)
        
        self.save_data()
        return booking

    def cancel_booking(self, booking_id: str) -> bool:
        """Cancel a booking"""
        if booking_id not in self.bookings:
            return False
        
        booking = self.bookings[booking_id]
        train = self.trains[booking.train_id]
        
        booking.status = "Cancelled"
        train.available_seats += 1
        train.bookings.remove(booking_id)
        
        self.save_data()
        return True

    def get_booking(self, booking_id: str) -> Optional[Booking]:
        """Get booking details by booking ID"""
        return self.bookings.get(booking_id)

    def get_passenger_bookings(self, email: str) -> List[Booking]:
        """Get all bookings for a passenger by email"""
        return [booking for booking in self.bookings.values() 
                if booking.passenger.email == email and booking.status == "Confirmed"]

    def display_trains(self, trains: List[Train]):
        """Display train information in a formatted way"""
        if not trains:
            print("No trains found matching your criteria.")
            return
        
        print("\n" + "="*100)
        print(f"{'Train ID':<10} {'Name':<15} {'Source':<12} {'Destination':<12} {'Departure':<10} {'Arrival':<10} {'Seats':<8} {'Price':<8}")
        print("="*100)
        
        for train in trains:
            print(f"{train.train_id:<10} {train.name:<15} {train.source:<12} {train.destination:<12} "
                  f"{train.departure_time:<10} {train.arrival_time:<10} {train.available_seats:<8} ${train.price:<7.2f}")

    def display_booking_details(self, booking: Booking):
        """Display booking details"""
        train = self.trains[booking.train_id]
        print("\n" + "="*50)
        print("BOOKING CONFIRMATION")
        print("="*50)
        print(f"Booking ID: {booking.booking_id}")
        print(f"Train: {train.name} ({train.train_id})")
        print(f"Route: {train.source} → {train.destination}")
        print(f"Departure: {train.departure_time}")
        print(f"Arrival: {train.arrival_time}")
        print(f"Passenger: {booking.passenger.name}")
        print(f"Journey Date: {booking.journey_date}")
        print(f"Booking Date: {booking.booking_date}")
        print(f"Status: {booking.status}")
        print(f"Price: ${train.price:.2f}")
        print("="*50)

def main():
    """Main function to run the train booking system"""
    system = TrainBookingSystem()
    
    while True:
        print("\n" + "="*50)
        print("🚂 TRAIN BOOKING SYSTEM 🚂")
        print("="*50)
        print("1. Search Trains")
        print("2. Book Ticket")
        print("3. Cancel Booking")
        print("4. View Booking")
        print("5. View My Bookings")
        print("6. Exit")
        print("="*50)
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            print("\n🔍 SEARCH TRAINS")
            source = input("Enter source station: ").strip()
            destination = input("Enter destination station: ").strip()
            
            trains = system.search_trains(source, destination)
            system.display_trains(trains)
            
        elif choice == '2':
            print("\n🎫 BOOK TICKET")
            source = input("Enter source station: ").strip()
            destination = input("Enter destination station: ").strip()
            
            trains = system.search_trains(source, destination)
            if not trains:
                print("No trains available for this route.")
                continue
            
            system.display_trains(trains)
            train_id = input("\nEnter Train ID to book: ").strip().upper()
            
            if train_id not in [train.train_id for train in trains]:
                print("Invalid Train ID.")
                continue
            
            print("\n👤 PASSENGER DETAILS")
            name = input("Enter passenger name: ").strip()
            age = int(input("Enter age: "))
            gender = input("Enter gender (M/F/Other): ").strip()
            phone = input("Enter phone number: ").strip()
            email = input("Enter email: ").strip()
            journey_date = input("Enter journey date (YYYY-MM-DD): ").strip()
            
            passenger = Passenger(name, age, gender, phone, email)
            booking = system.book_ticket(train_id, passenger, journey_date)
            
            if booking:
                print("\n✅ Booking Successful!")
                system.display_booking_details(booking)
            else:
                print("❌ Booking failed. No seats available.")
                
        elif choice == '3':
            print("\n❌ CANCEL BOOKING")
            booking_id = input("Enter Booking ID: ").strip()
            
            if system.cancel_booking(booking_id):
                print("✅ Booking cancelled successfully!")
            else:
                print("❌ Booking not found or already cancelled.")
                
        elif choice == '4':
            print("\n📋 VIEW BOOKING")
            booking_id = input("Enter Booking ID: ").strip()
            
            booking = system.get_booking(booking_id)
            if booking:
                system.display_booking_details(booking)
            else:
                print("❌ Booking not found.")
                
        elif choice == '5':
            print("\n📚 MY BOOKINGS")
            email = input("Enter your email: ").strip()
            
            bookings = system.get_passenger_bookings(email)
            if bookings:
                for booking in bookings:
                    system.display_booking_details(booking)
            else:
                print("No bookings found for this email.")
                
        elif choice == '6':
            print("Thank you for using Train Booking System! 🚂")
            break
            
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
