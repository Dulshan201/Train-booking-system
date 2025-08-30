#!/usr/bin/env python3
"""
Web-based Train Booking System
A beautiful, modern web interface for the train booking system with worldwide cities
"""

from flask import Flask, render_template, request, jsonify, redirect, url_for, flash, session
from datetime import datetime, timedelta
import json
import os
import uuid
import secrets
from main import TrainBookingSystem, Train, Passenger, Booking
from cities import WORLD_CITIES, CITY_REGIONS

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# Initialize the booking system
booking_system = TrainBookingSystem()

@app.route('/')
def index():
    """Home page with search functionality"""
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search_trains():
    """Search for trains based on source and destination"""
    source = request.form.get('source', '').strip()
    destination = request.form.get('destination', '').strip()
    
    if not source or not destination:
        flash('Please enter both source and destination', 'error')
        return redirect(url_for('index'))
    
    trains = booking_system.search_trains(source, destination)
    return render_template('search_results.html', trains=trains, source=source, destination=destination)

@app.route('/book/<train_id>')
def book_form(train_id):
    """Show booking form for selected train"""
    train = booking_system.trains.get(train_id)
    if not train:
        flash('Train not found', 'error')
        return redirect(url_for('index'))
    
    return render_template('booking_form.html', train=train)

@app.route('/book', methods=['POST'])
def book_ticket():
    """Process ticket booking"""
    try:
        train_id = request.form.get('train_id')
        name = request.form.get('name', '').strip()
        age_str = request.form.get('age', '0')
        gender = request.form.get('gender', '').strip()
        phone = request.form.get('phone', '').strip()
        email = request.form.get('email', '').strip()
        journey_date = request.form.get('journey_date', '').strip()
        
        # Debug logging
        print(f"Booking attempt - Train ID: {train_id}, Name: {name}, Age: {age_str}")
        
        # Validation
        if not train_id:
            flash('Train ID is missing', 'error')
            return redirect(url_for('index'))
            
        if not name:
            flash('Please enter your full name', 'error')
            return redirect(url_for('book_form', train_id=train_id))
            
        try:
            age = int(age_str)
            if age < 1 or age > 120:
                flash('Please enter a valid age between 1 and 120', 'error')
                return redirect(url_for('book_form', train_id=train_id))
        except ValueError:
            flash('Please enter a valid age', 'error')
            return redirect(url_for('book_form', train_id=train_id))
            
        if not gender:
            flash('Please select your gender', 'error')
            return redirect(url_for('book_form', train_id=train_id))
            
        if not phone:
            flash('Please enter your phone number', 'error')
            return redirect(url_for('book_form', train_id=train_id))
            
        if not email:
            flash('Please enter your email address', 'error')
            return redirect(url_for('book_form', train_id=train_id))
            
        if not journey_date:
            flash('Please select your journey date', 'error')
            return redirect(url_for('book_form', train_id=train_id))
        
        # Check if train exists
        if train_id not in booking_system.trains:
            flash('Selected train not found', 'error')
            return redirect(url_for('index'))
        
        # Create passenger and book ticket
        passenger = Passenger(name, age, gender, phone, email)
        booking = booking_system.book_ticket(train_id, passenger, journey_date)
        
        if booking:
            session['last_booking'] = booking.booking_id
            flash('Booking successful!', 'success')
            return redirect(url_for('booking_confirmation', booking_id=booking.booking_id))
        else:
            flash('Booking failed. No seats available on this train.', 'error')
            return redirect(url_for('book_form', train_id=train_id))
            
    except Exception as e:
        print(f"Booking error: {str(e)}")
        flash(f'An error occurred during booking: {str(e)}', 'error')
        return redirect(url_for('index'))

@app.route('/booking/<booking_id>')
def booking_confirmation(booking_id):
    """Show booking confirmation"""
    booking = booking_system.get_booking(booking_id)
    if not booking:
        flash('Booking not found', 'error')
        return redirect(url_for('index'))
    
    train = booking_system.trains[booking.train_id]
    return render_template('booking_confirmation.html', booking=booking, train=train)

@app.route('/my-bookings')
def my_bookings():
    """Show form to view user's bookings"""
    return render_template('my_bookings.html')

@app.route('/my-bookings', methods=['POST'])
def view_bookings():
    """View all bookings for an email"""
    email = request.form.get('email', '').strip()
    if not email:
        flash('Please enter your email address', 'error')
        return redirect(url_for('my_bookings'))
    
    bookings = booking_system.get_passenger_bookings(email)
    return render_template('bookings_list.html', bookings=bookings, email=email, booking_system=booking_system)

@app.route('/cancel/<booking_id>')
def cancel_booking(booking_id):
    """Cancel a booking"""
    if booking_system.cancel_booking(booking_id):
        flash('Booking cancelled successfully', 'success')
    else:
        flash('Booking not found or already cancelled', 'error')
    
    return redirect(url_for('index'))

@app.route('/system-status')
def system_status():
    """Show system status page"""
    # Get system statistics
    total_trains = len(booking_system.trains)
    total_bookings = len(booking_system.bookings)
    confirmed_bookings = sum(1 for b in booking_system.bookings.values() if b.status == "Confirmed")
    cancelled_bookings = sum(1 for b in booking_system.bookings.values() if b.status == "Cancelled")
    total_seats = sum(train.available_seats for train in booking_system.trains.values())
    
    stats = {
        'total_trains': total_trains,
        'total_bookings': total_bookings,
        'confirmed_bookings': confirmed_bookings,
        'cancelled_bookings': cancelled_bookings,
        'total_seats': total_seats,
        'version': '1.0.0'
    }
    
    return render_template('system_status.html', stats=stats)

@app.route('/api/trains')
def api_trains():
    """API endpoint for train data"""
    trains_data = []
    for train in booking_system.trains.values():
        trains_data.append({
            'train_id': train.train_id,
            'name': train.name,
            'source': train.source,
            'destination': train.destination,
            'departure_time': train.departure_time,
            'arrival_time': train.arrival_time,
            'available_seats': train.available_seats,
            'price': train.price
        })
    return jsonify(trains_data)

@app.route('/api/cities')
def get_cities():
    """API endpoint to get all available cities"""
    return jsonify(WORLD_CITIES)

@app.route('/api/cities/search')
def search_cities():
    """API endpoint to search cities for autocomplete"""
    query = request.args.get('q', '').lower()
    if len(query) < 2:
        return jsonify([])
    
    matching_cities = [city for city in WORLD_CITIES if query in city.lower()]
    # Limit to 10 results for better performance
    return jsonify(matching_cities[:10])

@app.route('/api/regions')
def get_regions():
    """API endpoint to get cities grouped by regions"""
    return jsonify(CITY_REGIONS)

@app.errorhandler(404)
def not_found(error):
    """404 error handler"""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    """500 error handler"""
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
