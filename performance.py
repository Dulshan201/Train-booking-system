#!/usr/bin/env python3
"""
Performance monitoring and optimization tools for Train Booking System
"""

import time
import psutil
import os
from datetime import datetime
from typing import Dict, List
import json

class PerformanceMonitor:
    """Monitor system performance and resource usage"""
    
    def __init__(self):
        self.start_time = time.time()
        self.operation_logs = []
        
    def log_operation(self, operation_name: str, duration: float, memory_used: float = None):
        """Log operation performance metrics"""
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "operation": operation_name,
            "duration_ms": round(duration * 1000, 2),
            "memory_mb": round(memory_used or psutil.Process().memory_info().rss / 1024 / 1024, 2)
        }
        self.operation_logs.append(log_entry)
        
    def get_system_stats(self) -> Dict:
        """Get current system statistics"""
        process = psutil.Process()
        return {
            "cpu_percent": psutil.cpu_percent(interval=1),
            "memory_percent": psutil.virtual_memory().percent,
            "process_memory_mb": round(process.memory_info().rss / 1024 / 1024, 2),
            "disk_usage_percent": psutil.disk_usage('/').percent if os.name != 'nt' else psutil.disk_usage('C:\\').percent,
            "uptime_seconds": round(time.time() - self.start_time, 2)
        }
        
    def generate_performance_report(self) -> Dict:
        """Generate comprehensive performance report"""
        if not self.operation_logs:
            return {"message": "No operations logged yet"}
            
        durations = [log["duration_ms"] for log in self.operation_logs]
        memory_usage = [log["memory_mb"] for log in self.operation_logs]
        
        return {
            "total_operations": len(self.operation_logs),
            "average_duration_ms": round(sum(durations) / len(durations), 2),
            "max_duration_ms": max(durations),
            "min_duration_ms": min(durations),
            "average_memory_mb": round(sum(memory_usage) / len(memory_usage), 2),
            "peak_memory_mb": max(memory_usage),
            "operations_per_second": round(len(self.operation_logs) / (time.time() - self.start_time), 2),
            "system_stats": self.get_system_stats()
        }
        
    def export_logs(self, filename: str = None) -> str:
        """Export performance logs to JSON file"""
        if filename is None:
            filename = f"performance_logs_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            
        report_data = {
            "generated_at": datetime.now().isoformat(),
            "performance_summary": self.generate_performance_report(),
            "detailed_logs": self.operation_logs
        }
        
        with open(filename, 'w') as f:
            json.dump(report_data, f, indent=2)
            
        return filename

class DatabaseOptimizer:
    """Optimize data storage and retrieval operations"""
    
    @staticmethod
    def optimize_json_storage(data: Dict) -> Dict:
        """Optimize JSON data structure for better performance"""
        optimized = {}
        
        # Create indexes for faster lookups
        if "trains" in data:
            optimized["trains"] = data["trains"]
            optimized["train_index"] = {
                "by_source": {},
                "by_destination": {},
                "by_route": {}
            }
            
            for train_id, train_data in data["trains"].items():
                source = train_data.get("source", "").lower()
                destination = train_data.get("destination", "").lower()
                route = f"{source}-{destination}"
                
                # Build indexes
                if source not in optimized["train_index"]["by_source"]:
                    optimized["train_index"]["by_source"][source] = []
                optimized["train_index"]["by_source"][source].append(train_id)
                
                if destination not in optimized["train_index"]["by_destination"]:
                    optimized["train_index"]["by_destination"][destination] = []
                optimized["train_index"]["by_destination"][destination].append(train_id)
                
                if route not in optimized["train_index"]["by_route"]:
                    optimized["train_index"]["by_route"][route] = []
                optimized["train_index"]["by_route"][route].append(train_id)
        
        if "bookings" in data:
            optimized["bookings"] = data["bookings"]
            optimized["booking_index"] = {
                "by_email": {},
                "by_train": {},
                "by_date": {}
            }
            
            for booking_id, booking_data in data["bookings"].items():
                email = booking_data.get("passenger", {}).get("email", "").lower()
                train_id = booking_data.get("train_id", "")
                date = booking_data.get("journey_date", "")
                
                # Build booking indexes
                if email and email not in optimized["booking_index"]["by_email"]:
                    optimized["booking_index"]["by_email"][email] = []
                if email:
                    optimized["booking_index"]["by_email"][email].append(booking_id)
                
                if train_id not in optimized["booking_index"]["by_train"]:
                    optimized["booking_index"]["by_train"][train_id] = []
                optimized["booking_index"]["by_train"][train_id].append(booking_id)
                
                if date not in optimized["booking_index"]["by_date"]:
                    optimized["booking_index"]["by_date"][date] = []
                optimized["booking_index"]["by_date"][date].append(booking_id)
        
        return optimized
    
    @staticmethod
    def compress_data(data: Dict) -> Dict:
        """Compress data by removing redundant information"""
        compressed = {}
        
        # Compress train data
        if "trains" in data:
            compressed["trains"] = {}
            for train_id, train_data in data["trains"].items():
                compressed["trains"][train_id] = {
                    "n": train_data.get("name", ""),  # name
                    "s": train_data.get("source", ""),  # source
                    "d": train_data.get("destination", ""),  # destination
                    "dt": train_data.get("departure_time", ""),  # departure_time
                    "at": train_data.get("arrival_time", ""),  # arrival_time
                    "ts": train_data.get("total_seats", 0),  # total_seats
                    "as": train_data.get("available_seats", 0),  # available_seats
                    "p": train_data.get("price", 0.0),  # price
                    "b": train_data.get("bookings", [])  # bookings
                }
        
        return compressed

class CacheManager:
    """Manage caching for frequently accessed data"""
    
    def __init__(self, max_size: int = 100, ttl_seconds: int = 300):
        self.cache = {}
        self.access_times = {}
        self.max_size = max_size
        self.ttl_seconds = ttl_seconds
        
    def get(self, key: str):
        """Get item from cache"""
        current_time = time.time()
        
        if key in self.cache:
            # Check if item has expired
            if current_time - self.access_times[key] > self.ttl_seconds:
                del self.cache[key]
                del self.access_times[key]
                return None
            
            self.access_times[key] = current_time
            return self.cache[key]
        
        return None
    
    def set(self, key: str, value):
        """Set item in cache"""
        current_time = time.time()
        
        # Remove expired items
        self._cleanup_expired()
        
        # Remove oldest item if cache is full
        if len(self.cache) >= self.max_size:
            oldest_key = min(self.access_times.keys(), key=lambda k: self.access_times[k])
            del self.cache[oldest_key]
            del self.access_times[oldest_key]
        
        self.cache[key] = value
        self.access_times[key] = current_time
    
    def _cleanup_expired(self):
        """Remove expired items from cache"""
        current_time = time.time()
        expired_keys = [
            key for key, access_time in self.access_times.items()
            if current_time - access_time > self.ttl_seconds
        ]
        
        for key in expired_keys:
            del self.cache[key]
            del self.access_times[key]
    
    def clear(self):
        """Clear all cache"""
        self.cache.clear()
        self.access_times.clear()
    
    def get_stats(self) -> Dict:
        """Get cache statistics"""
        self._cleanup_expired()
        return {
            "size": len(self.cache),
            "max_size": self.max_size,
            "utilization_percent": round((len(self.cache) / self.max_size) * 100, 2),
            "ttl_seconds": self.ttl_seconds
        }

def benchmark_operations(booking_system, num_operations: int = 1000) -> Dict:
    """Benchmark various system operations"""
    monitor = PerformanceMonitor()
    results = {}
    
    # Benchmark train search
    start_time = time.time()
    for _ in range(num_operations):
        booking_system.search_trains("New York", "Boston")
    search_duration = time.time() - start_time
    monitor.log_operation("train_search", search_duration / num_operations)
    results["search_avg_ms"] = round((search_duration / num_operations) * 1000, 2)
    
    # Benchmark data loading
    start_time = time.time()
    for _ in range(100):  # Fewer iterations for data loading
        booking_system.load_data()
    load_duration = time.time() - start_time
    monitor.log_operation("data_loading", load_duration / 100)
    results["load_avg_ms"] = round((load_duration / 100) * 1000, 2)
    
    # Benchmark data saving
    start_time = time.time()
    for _ in range(100):
        booking_system.save_data()
    save_duration = time.time() - start_time
    monitor.log_operation("data_saving", save_duration / 100)
    results["save_avg_ms"] = round((save_duration / 100) * 1000, 2)
    
    results["system_stats"] = monitor.get_system_stats()
    results["performance_report"] = monitor.generate_performance_report()
    
    return results

if __name__ == "__main__":
    # Example usage
    monitor = PerformanceMonitor()
    
    # Simulate some operations
    start = time.time()
    time.sleep(0.1)  # Simulate operation
    monitor.log_operation("sample_operation", time.time() - start)
    
    print("Performance Report:")
    print(json.dumps(monitor.generate_performance_report(), indent=2))
