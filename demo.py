#!/usr/bin/env python3
"""
Demo script for Train Booking System
This script demonstrates the key features of the booking system
"""

from main import TrainBookingSystem, Passenger
import time

def print_separator(title=""):
    """Print a decorative separator with optional title"""
    if title:
        print(f"\n{'='*20} {title} {'='*20}")
    else:
        print("="*60)

def demo_train_booking_system():
    """Demonstrate the train booking system features"""
    print("🚂 TRAIN BOOKING SYSTEM DEMO 🚂")
    print_separator()
    
    # Initialize the system
    system = TrainBookingSystem("demo_data.json")
    print("✅ System initialized with sample trains")
    
    # Demo 1: Search for trains
    print_separator("SEARCHING FOR TRAINS")
    print("🔍 Searching for trains from New York to Boston...")
    trains = system.search_trains("New York", "Boston")
    system.display_trains(trains)
    
    # Demo 2: Book a ticket
    print_separator("BOOKING A TICKET")
    if trains:
        train = trains[0]
        print(f"📋 Booking ticket for train {train.train_id} - {train.name}")
        
        # Create a demo passenger
        passenger = Passenger(
            name="John Demo",
            age=30,
            gender="M",
            phone="555-0123",
            email="john.demo@example.com"
        )
        
        booking = system.book_ticket(train.train_id, passenger, "2025-09-15")
        
        if booking:
            print("✅ Booking successful!")
            system.display_booking_details(booking)
            demo_booking_id = booking.booking_id
        else:
            print("❌ Booking failed!")
            return
    
    # Demo 3: Search for another route
    print_separator("SEARCHING ANOTHER ROUTE")
    print("🔍 Searching for trains from Boston to Washington...")
    trains2 = system.search_trains("Boston", "Washington")
    system.display_trains(trains2)
    
    # Demo 4: Book another ticket for the same passenger
    if trains2:
        train2 = trains2[0]
        print(f"\n📋 Booking another ticket for the same passenger...")
        
        booking2 = system.book_ticket(train2.train_id, passenger, "2025-09-16")
        
        if booking2:
            print("✅ Second booking successful!")
            system.display_booking_details(booking2)
    
    # Demo 5: View all bookings for a passenger
    print_separator("PASSENGER BOOKING HISTORY")
    print(f"📚 Viewing all bookings for {passenger.email}...")
    passenger_bookings = system.get_passenger_bookings(passenger.email)
    
    print(f"Found {len(passenger_bookings)} bookings:")
    for booking in passenger_bookings:
        system.display_booking_details(booking)
    
    # Demo 6: Cancel a booking
    print_separator("CANCELLING A BOOKING")
    if 'demo_booking_id' in locals():
        print(f"❌ Cancelling booking {demo_booking_id[:8]}...")
        
        if system.cancel_booking(demo_booking_id):
            print("✅ Booking cancelled successfully!")
            
            # Show updated booking status
            cancelled_booking = system.get_booking(demo_booking_id)
            if cancelled_booking:
                print(f"📋 Updated booking status: {cancelled_booking.status}")
        else:
            print("❌ Failed to cancel booking!")
    
    # Demo 7: Show system statistics
    print_separator("SYSTEM STATISTICS")
    total_trains = len(system.trains)
    total_bookings = len(system.bookings)
    active_bookings = len([b for b in system.bookings.values() if b.status == "Confirmed"])
    
    print(f"📊 Total trains in system: {total_trains}")
    print(f"📊 Total bookings made: {total_bookings}")
    print(f"📊 Active bookings: {active_bookings}")
    print(f"📊 Cancelled bookings: {total_bookings - active_bookings}")
    
    # Show train utilization
    print("\n🚂 Train Utilization:")
    for train in system.trains.values():
        utilization = ((train.total_seats - train.available_seats) / train.total_seats) * 100
        print(f"   {train.train_id} - {train.name}: {utilization:.1f}% occupied")
    
    print_separator("DEMO COMPLETED")
    print("🎉 Demo completed successfully!")
    print("💡 Try running 'python main.py' for the interactive version!")
    print("🧪 Run 'python test_booking_system.py' to execute tests!")

if __name__ == "__main__":
    demo_train_booking_system()
