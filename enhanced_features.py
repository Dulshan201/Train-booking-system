#!/usr/bin/env python3
"""
Advanced Train Booking System Features
Enhanced functionality for better user experience
"""

from main import TrainBookingSystem, Train, Passenger, Booking
from utils import format_currency, calculate_journey_duration, validate_email
from datetime import datetime, timedelta
import json

class EnhancedTrainBookingSystem(TrainBookingSystem):
    """Enhanced version of the train booking system with additional features"""
    
    def __init__(self, data_file: str = "train_data.json"):
        super().__init__(data_file)
        self.loyalty_points = {}  # Store loyalty points for passengers
        self.discounts = {
            "STUDENT": 0.15,
            "SENIOR": 0.20,
            "MILITARY": 0.25,
            "FREQUENT": 0.10
        }
    
    def search_trains_advanced(self, source: str, destination: str, 
                             date: str = None, max_price: float = None,
                             departure_after: str = None) -> list:
        """Advanced train search with filters"""
        results = self.search_trains(source, destination, date)
        
        # Filter by maximum price
        if max_price is not None:
            results = [train for train in results if train.price <= max_price]
        
        # Filter by departure time
        if departure_after is not None:
            try:
                min_time = datetime.strptime(departure_after, "%H:%M").time()
                filtered_results = []
                for train in results:
                    train_time = datetime.strptime(train.departure_time, "%H:%M").time()
                    if train_time >= min_time:
                        filtered_results.append(train)
                results = filtered_results
            except ValueError:
                pass  # Invalid time format, ignore filter
        
        return results
    
    def calculate_loyalty_points(self, price: float) -> int:
        """Calculate loyalty points based on ticket price"""
        return int(price * 10)  # 10 points per dollar
    
    def apply_discount(self, price: float, discount_code: str = None) -> float:
        """Apply discount to ticket price"""
        if discount_code and discount_code.upper() in self.discounts:
            discount_rate = self.discounts[discount_code.upper()]
            return price * (1 - discount_rate)
        return price
    
    def book_ticket_enhanced(self, train_id: str, passenger: Passenger, 
                           journey_date: str, discount_code: str = None) -> Booking:
        """Enhanced booking with discounts and loyalty points"""
        if train_id not in self.trains:
            return None
        
        train = self.trains[train_id]
        if train.available_seats <= 0:
            return None
        
        # Calculate discounted price
        original_price = train.price
        discounted_price = self.apply_discount(original_price, discount_code)
        
        # Create booking with original booking method
        booking = self.book_ticket(train_id, passenger, journey_date)
        
        if booking:
            # Add loyalty points
            points_earned = self.calculate_loyalty_points(discounted_price)
            if passenger.email not in self.loyalty_points:
                self.loyalty_points[passenger.email] = 0
            self.loyalty_points[passenger.email] += points_earned
            
            # Store discount information in booking (extend booking object)
            booking.original_price = original_price
            booking.discounted_price = discounted_price
            booking.discount_code = discount_code
            booking.points_earned = points_earned
            
            self.save_data()
        
        return booking
    
    def get_loyalty_points(self, email: str) -> int:
        """Get loyalty points for a passenger"""
        return self.loyalty_points.get(email, 0)
    
    def redeem_loyalty_points(self, email: str, points: int) -> bool:
        """Redeem loyalty points (100 points = $10 discount)"""
        current_points = self.get_loyalty_points(email)
        if current_points >= points:
            self.loyalty_points[email] -= points
            return True
        return False
    
    def get_popular_routes(self, limit: int = 5) -> list:
        """Get most popular routes based on bookings"""
        route_counts = {}
        
        for booking in self.bookings.values():
            if booking.status == "Confirmed":
                train = self.trains[booking.train_id]
                route = f"{train.source} → {train.destination}"
                route_counts[route] = route_counts.get(route, 0) + 1
        
        # Sort by popularity
        popular_routes = sorted(route_counts.items(), key=lambda x: x[1], reverse=True)
        return popular_routes[:limit]
    
    def get_revenue_report(self) -> dict:
        """Generate revenue report"""
        total_revenue = 0
        bookings_count = 0
        cancelled_count = 0
        
        for booking in self.bookings.values():
            if booking.status == "Confirmed":
                train = self.trains[booking.train_id]
                total_revenue += train.price
                bookings_count += 1
            elif booking.status == "Cancelled":
                cancelled_count += 1
        
        return {
            "total_revenue": total_revenue,
            "confirmed_bookings": bookings_count,
            "cancelled_bookings": cancelled_count,
            "average_ticket_price": total_revenue / bookings_count if bookings_count > 0 else 0
        }
    
    def suggest_alternative_routes(self, source: str, destination: str) -> list:
        """Suggest alternative routes with connections"""
        alternatives = []
        
        # Find trains from source to any intermediate station
        intermediate_trains = []
        for train in self.trains.values():
            if train.source.lower() == source.lower() and train.available_seats > 0:
                intermediate_trains.append(train)
        
        # Find trains from intermediate stations to destination
        for intermediate_train in intermediate_trains:
            intermediate_station = intermediate_train.destination
            connecting_trains = []
            
            for train in self.trains.values():
                if (train.source.lower() == intermediate_station.lower() and 
                    train.destination.lower() == destination.lower() and 
                    train.available_seats > 0):
                    connecting_trains.append(train)
            
            for connecting_train in connecting_trains:
                # Check if connection time is reasonable (at least 30 minutes)
                try:
                    arrival_time = datetime.strptime(intermediate_train.arrival_time, "%H:%M")
                    departure_time = datetime.strptime(connecting_train.departure_time, "%H:%M")
                    
                    # Handle next day scenarios
                    if connecting_train.departure_time < intermediate_train.arrival_time:
                        departure_time += timedelta(days=1)
                    
                    connection_time = departure_time - arrival_time
                    
                    if connection_time.total_seconds() >= 1800:  # 30 minutes minimum
                        total_price = intermediate_train.price + connecting_train.price
                        total_duration = calculate_journey_duration(
                            intermediate_train.departure_time, 
                            connecting_train.arrival_time
                        )
                        
                        alternatives.append({
                            "route": f"{source} → {intermediate_station} → {destination}",
                            "trains": [intermediate_train.train_id, connecting_train.train_id],
                            "total_price": total_price,
                            "total_duration": total_duration,
                            "connection_time": str(connection_time)
                        })
                except ValueError:
                    continue  # Skip if time parsing fails
        
        return alternatives
    
    def display_enhanced_booking_details(self, booking: Booking):
        """Display enhanced booking details with discounts and points"""
        self.display_booking_details(booking)
        
        # Show additional information if available
        if hasattr(booking, 'discount_code') and booking.discount_code:
            print(f"Discount Applied: {booking.discount_code}")
            print(f"Original Price: {format_currency(booking.original_price)}")
            print(f"Discounted Price: {format_currency(booking.discounted_price)}")
            savings = booking.original_price - booking.discounted_price
            print(f"You Saved: {format_currency(savings)}")
        
        if hasattr(booking, 'points_earned'):
            print(f"Loyalty Points Earned: {booking.points_earned}")
        
        # Show current loyalty points
        current_points = self.get_loyalty_points(booking.passenger.email)
        print(f"Total Loyalty Points: {current_points}")
    
    def export_bookings_to_csv(self, filename: str = "bookings_export.csv") -> bool:
        """Export all bookings to CSV file"""
        try:
            import csv
            
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['booking_id', 'passenger_name', 'passenger_email', 
                            'train_id', 'train_name', 'source', 'destination',
                            'departure_time', 'arrival_time', 'journey_date', 
                            'booking_date', 'price', 'status']
                
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                
                for booking in self.bookings.values():
                    train = self.trains[booking.train_id]
                    writer.writerow({
                        'booking_id': booking.booking_id,
                        'passenger_name': booking.passenger.name,
                        'passenger_email': booking.passenger.email,
                        'train_id': train.train_id,
                        'train_name': train.name,
                        'source': train.source,
                        'destination': train.destination,
                        'departure_time': train.departure_time,
                        'arrival_time': train.arrival_time,
                        'journey_date': booking.journey_date,
                        'booking_date': booking.booking_date,
                        'price': train.price,
                        'status': booking.status
                    })
            
            return True
        except Exception as e:
            print(f"Export failed: {e}")
            return False

def run_enhanced_demo():
    """Demonstrate enhanced features"""
    print("🚀 ENHANCED TRAIN BOOKING SYSTEM DEMO")
    print("="*50)
    
    system = EnhancedTrainBookingSystem("enhanced_demo_data.json")
    
    # Demo advanced search
    print("\n🔍 ADVANCED SEARCH DEMO")
    print("Searching for trains under $60 departing after 10:00...")
    trains = system.search_trains_advanced("New York", "Boston", 
                                          max_price=60.0, 
                                          departure_after="10:00")
    system.display_trains(trains)
    
    # Demo discount booking
    print("\n🎫 DISCOUNT BOOKING DEMO")
    passenger = Passenger("Student User", 20, "F", "555-0199", "student@example.com")
    
    if trains:
        booking = system.book_ticket_enhanced(trains[0].train_id, passenger, 
                                            "2025-09-20", "STUDENT")
        if booking:
            print("✅ Student discount applied!")
            system.display_enhanced_booking_details(booking)
    
    # Demo popular routes
    print("\n📊 POPULAR ROUTES")
    popular = system.get_popular_routes()
    for i, (route, count) in enumerate(popular, 1):
        print(f"{i}. {route} - {count} bookings")
    
    # Demo revenue report
    print("\n💰 REVENUE REPORT")
    report = system.get_revenue_report()
    print(f"Total Revenue: {format_currency(report['total_revenue'])}")
    print(f"Confirmed Bookings: {report['confirmed_bookings']}")
    print(f"Average Ticket Price: {format_currency(report['average_ticket_price'])}")
    
    print("\n🎉 Enhanced demo completed!")

if __name__ == "__main__":
    run_enhanced_demo()
