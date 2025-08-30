#!/usr/bin/env python3
"""
Advanced booking analytics and reporting features
"""

from datetime import datetime, timedelta
from typing import Dict, List, Tuple
import json
from collections import defaultdict

class BookingAnalytics:
    """Advanced analytics for booking data"""
    
    def __init__(self, booking_system):
        self.system = booking_system
    
    def generate_daily_report(self, date: str = None) -> Dict:
        """Generate daily booking report"""
        if date is None:
            date = datetime.now().strftime("%Y-%m-%d")
        
        daily_bookings = [
            booking for booking in self.system.bookings.values()
            if booking.booking_date.startswith(date)
        ]
        
        total_revenue = sum(
            self.system.trains[booking.train_id].price 
            for booking in daily_bookings 
            if booking.status == "Confirmed"
        )
        
        return {
            "date": date,
            "total_bookings": len(daily_bookings),
            "confirmed_bookings": len([b for b in daily_bookings if b.status == "Confirmed"]),
            "cancelled_bookings": len([b for b in daily_bookings if b.status == "Cancelled"]),
            "total_revenue": total_revenue,
            "popular_routes": self._get_popular_routes(daily_bookings)
        }
    
    def generate_weekly_report(self) -> Dict:
        """Generate weekly booking statistics"""
        end_date = datetime.now()
        start_date = end_date - timedelta(days=7)
        
        weekly_bookings = [
            booking for booking in self.system.bookings.values()
            if start_date <= datetime.strptime(booking.booking_date.split()[0], "%Y-%m-%d") <= end_date
        ]
        
        return {
            "week_ending": end_date.strftime("%Y-%m-%d"),
            "total_bookings": len(weekly_bookings),
            "daily_breakdown": self._get_daily_breakdown(weekly_bookings),
            "train_utilization": self._calculate_train_utilization(),
            "revenue_trend": self._calculate_revenue_trend(weekly_bookings)
        }
    
    def get_passenger_insights(self) -> Dict:
        """Analyze passenger booking patterns"""
        passenger_data = defaultdict(list)
        
        for booking in self.system.bookings.values():
            passenger_data[booking.passenger.email].append(booking)
        
        insights = {
            "total_unique_passengers": len(passenger_data),
            "repeat_customers": len([p for p in passenger_data.values() if len(p) > 1]),
            "average_bookings_per_passenger": sum(len(bookings) for bookings in passenger_data.values()) / len(passenger_data) if passenger_data else 0,
            "most_frequent_passenger": self._get_most_frequent_passenger(passenger_data)
        }
        
        return insights
    
    def get_route_performance(self) -> List[Dict]:
        """Analyze performance of different routes"""
        route_stats = defaultdict(lambda: {"bookings": 0, "revenue": 0, "cancellations": 0})
        
        for booking in self.system.bookings.values():
            train = self.system.trains[booking.train_id]
            route = f"{train.source} → {train.destination}"
            
            route_stats[route]["bookings"] += 1
            if booking.status == "Confirmed":
                route_stats[route]["revenue"] += train.price
            else:
                route_stats[route]["cancellations"] += 1
        
        return [
            {
                "route": route,
                "total_bookings": stats["bookings"],
                "revenue": stats["revenue"],
                "cancellation_rate": (stats["cancellations"] / stats["bookings"] * 100) if stats["bookings"] > 0 else 0
            }
            for route, stats in route_stats.items()
        ]
    
    def predict_peak_times(self) -> Dict:
        """Predict peak booking times based on historical data"""
        hour_bookings = defaultdict(int)
        day_bookings = defaultdict(int)
        
        for booking in self.system.bookings.values():
            booking_time = datetime.strptime(booking.booking_date, "%Y-%m-%d %H:%M:%S")
            hour_bookings[booking_time.hour] += 1
            day_bookings[booking_time.strftime("%A")] += 1
        
        peak_hour = max(hour_bookings.items(), key=lambda x: x[1]) if hour_bookings else (0, 0)
        peak_day = max(day_bookings.items(), key=lambda x: x[1]) if day_bookings else ("Unknown", 0)
        
        return {
            "peak_hour": f"{peak_hour[0]}:00",
            "peak_hour_bookings": peak_hour[1],
            "peak_day": peak_day[0],
            "peak_day_bookings": peak_day[1],
            "hourly_distribution": dict(hour_bookings),
            "daily_distribution": dict(day_bookings)
        }
    
    def _get_popular_routes(self, bookings: List) -> List[Tuple[str, int]]:
        """Get most popular routes from bookings"""
        route_count = defaultdict(int)
        
        for booking in bookings:
            train = self.system.trains[booking.train_id]
            route = f"{train.source} → {train.destination}"
            route_count[route] += 1
        
        return sorted(route_count.items(), key=lambda x: x[1], reverse=True)[:5]
    
    def _get_daily_breakdown(self, bookings: List) -> Dict:
        """Get daily breakdown of bookings"""
        daily_count = defaultdict(int)
        
        for booking in bookings:
            date = booking.booking_date.split()[0]
            daily_count[date] += 1
        
        return dict(daily_count)
    
    def _calculate_train_utilization(self) -> Dict:
        """Calculate utilization rate for each train"""
        utilization = {}
        
        for train_id, train in self.system.trains.items():
            if train.total_seats > 0:
                occupied = train.total_seats - train.available_seats
                utilization[train_id] = {
                    "name": train.name,
                    "utilization_rate": (occupied / train.total_seats) * 100,
                    "occupied_seats": occupied,
                    "total_seats": train.total_seats
                }
        
        return utilization
    
    def _calculate_revenue_trend(self, bookings: List) -> List[Dict]:
        """Calculate revenue trend over time"""
        daily_revenue = defaultdict(float)
        
        for booking in bookings:
            if booking.status == "Confirmed":
                date = booking.booking_date.split()[0]
                train = self.system.trains[booking.train_id]
                daily_revenue[date] += train.price
        
        return [
            {"date": date, "revenue": revenue}
            for date, revenue in sorted(daily_revenue.items())
        ]
    
    def _get_most_frequent_passenger(self, passenger_data: Dict) -> Dict:
        """Find the most frequent passenger"""
        if not passenger_data:
            return {"email": "None", "bookings": 0}
        
        most_frequent = max(passenger_data.items(), key=lambda x: len(x[1]))
        return {
            "email": most_frequent[0],
            "bookings": len(most_frequent[1]),
            "name": most_frequent[1][0].passenger.name if most_frequent[1] else "Unknown"
        }
    
    def export_analytics_report(self, filename: str = None) -> str:
        """Export comprehensive analytics report"""
        if filename is None:
            filename = f"booking_analytics_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        report = {
            "generated_at": datetime.now().isoformat(),
            "daily_report": self.generate_daily_report(),
            "weekly_report": self.generate_weekly_report(),
            "passenger_insights": self.get_passenger_insights(),
            "route_performance": self.get_route_performance(),
            "peak_times": self.predict_peak_times()
        }
        
        with open(filename, 'w') as f:
            json.dump(report, f, indent=2, default=str)
        
        return filename

class RevenueOptimizer:
    """Optimize revenue through dynamic pricing and recommendations"""
    
    def __init__(self, booking_system):
        self.system = booking_system
    
    def suggest_price_adjustments(self) -> Dict:
        """Suggest price adjustments based on demand"""
        suggestions = {}
        
        for train_id, train in self.system.trains.items():
            utilization_rate = ((train.total_seats - train.available_seats) / train.total_seats) * 100
            
            if utilization_rate > 80:
                suggestion = "Increase price by 10-15%"
                reason = "High demand"
            elif utilization_rate < 30:
                suggestion = "Decrease price by 5-10%"
                reason = "Low demand"
            else:
                suggestion = "Maintain current price"
                reason = "Balanced demand"
            
            suggestions[train_id] = {
                "current_price": train.price,
                "utilization_rate": utilization_rate,
                "suggestion": suggestion,
                "reason": reason
            }
        
        return suggestions
    
    def calculate_optimal_capacity(self) -> Dict:
        """Calculate optimal capacity for each route"""
        # This is a simplified calculation
        route_demand = defaultdict(int)
        
        for booking in self.system.bookings.values():
            train = self.system.trains[booking.train_id]
            route = f"{train.source}-{train.destination}"
            route_demand[route] += 1
        
        recommendations = {}
        for train_id, train in self.system.trains.items():
            route = f"{train.source}-{train.destination}"
            demand = route_demand.get(route, 0)
            
            recommendations[train_id] = {
                "current_capacity": train.total_seats,
                "demand_score": demand,
                "recommended_capacity": max(50, min(200, demand * 10)),  # Simple formula
                "efficiency_score": (demand / train.total_seats) * 100 if train.total_seats > 0 else 0
            }
        
        return recommendations
