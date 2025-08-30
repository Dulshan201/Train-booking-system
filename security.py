#!/usr/bin/env python3
"""
Security and authentication module for Train Booking System
"""

import hashlib
import secrets
import re
from datetime import datetime, timedelta
from typing import Dict, Optional, List
import json

class SecurityManager:
    """Handle security-related operations for the booking system"""
    
    def __init__(self):
        self.failed_attempts = {}
        self.blocked_ips = {}
        self.session_tokens = {}
        self.max_attempts = 5
        self.block_duration = 300  # 5 minutes
        
    def hash_password(self, password: str, salt: str = None) -> tuple:
        """Hash password with salt for secure storage"""
        if salt is None:
            salt = secrets.token_hex(16)
        
        # Use SHA-256 with salt
        password_hash = hashlib.sha256((password + salt).encode()).hexdigest()
        return password_hash, salt
    
    def verify_password(self, password: str, stored_hash: str, salt: str) -> bool:
        """Verify password against stored hash"""
        test_hash, _ = self.hash_password(password, salt)
        return test_hash == stored_hash
    
    def validate_password_strength(self, password: str) -> Dict:
        """Validate password strength and return requirements"""
        requirements = {
            "min_length": len(password) >= 8,
            "has_uppercase": bool(re.search(r'[A-Z]', password)),
            "has_lowercase": bool(re.search(r'[a-z]', password)),
            "has_digit": bool(re.search(r'\d', password)),
            "has_special": bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password)),
            "no_common_patterns": not self._has_common_patterns(password)
        }
        
        strength_score = sum(requirements.values())
        
        return {
            "is_strong": strength_score >= 5,
            "score": strength_score,
            "max_score": 6,
            "requirements": requirements,
            "suggestions": self._get_password_suggestions(requirements)
        }
    
    def generate_secure_token(self, length: int = 32) -> str:
        """Generate cryptographically secure random token"""
        return secrets.token_urlsafe(length)
    
    def create_session(self, user_id: str, duration_hours: int = 24) -> str:
        """Create secure session token"""
        token = self.generate_secure_token()
        expiry = datetime.now() + timedelta(hours=duration_hours)
        
        self.session_tokens[token] = {
            "user_id": user_id,
            "created_at": datetime.now().isoformat(),
            "expires_at": expiry.isoformat(),
            "last_accessed": datetime.now().isoformat()
        }
        
        return token
    
    def validate_session(self, token: str) -> Optional[str]:
        """Validate session token and return user_id if valid"""
        if token not in self.session_tokens:
            return None
        
        session = self.session_tokens[token]
        expiry = datetime.fromisoformat(session["expires_at"])
        
        if datetime.now() > expiry:
            del self.session_tokens[token]
            return None
        
        # Update last accessed time
        session["last_accessed"] = datetime.now().isoformat()
        return session["user_id"]
    
    def invalidate_session(self, token: str) -> bool:
        """Invalidate/logout session"""
        if token in self.session_tokens:
            del self.session_tokens[token]
            return True
        return False
    
    def track_login_attempt(self, identifier: str, success: bool) -> bool:
        """Track login attempts and implement rate limiting"""
        current_time = datetime.now()
        
        # Check if currently blocked
        if identifier in self.blocked_ips:
            block_time = datetime.fromisoformat(self.blocked_ips[identifier])
            if current_time < block_time:
                return False  # Still blocked
            else:
                del self.blocked_ips[identifier]  # Unblock
        
        # Track failed attempts
        if not success:
            if identifier not in self.failed_attempts:
                self.failed_attempts[identifier] = []
            
            self.failed_attempts[identifier].append(current_time.isoformat())
            
            # Remove old attempts (older than 1 hour)
            one_hour_ago = current_time - timedelta(hours=1)
            self.failed_attempts[identifier] = [
                attempt for attempt in self.failed_attempts[identifier]
                if datetime.fromisoformat(attempt) > one_hour_ago
            ]
            
            # Block if too many failed attempts
            if len(self.failed_attempts[identifier]) >= self.max_attempts:
                block_until = current_time + timedelta(seconds=self.block_duration)
                self.blocked_ips[identifier] = block_until.isoformat()
                return False
        else:
            # Clear failed attempts on successful login
            if identifier in self.failed_attempts:
                del self.failed_attempts[identifier]
        
        return True
    
    def sanitize_input(self, input_str: str, max_length: int = 100) -> str:
        """Sanitize user input to prevent injection attacks"""
        if not isinstance(input_str, str):
            return ""
        
        # Remove/escape dangerous characters
        sanitized = input_str.strip()[:max_length]
        
        # Remove potentially dangerous patterns
        dangerous_patterns = [
            r'<script.*?</script>',
            r'javascript:',
            r'onload=',
            r'onerror=',
            r'<iframe',
            r'</iframe>',
            r'eval\(',
            r'exec\('
        ]
        
        for pattern in dangerous_patterns:
            sanitized = re.sub(pattern, '', sanitized, flags=re.IGNORECASE)
        
        return sanitized
    
    def validate_email_security(self, email: str) -> Dict:
        """Enhanced email validation with security checks"""
        validation = {
            "is_valid": False,
            "issues": []
        }
        
        # Basic format check
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, email):
            validation["issues"].append("Invalid email format")
            return validation
        
        # Check for suspicious patterns
        suspicious_patterns = [
            r'[<>"\']',  # HTML/script injection attempts
            r'javascript:',  # JavaScript injection
            r'\.\.',  # Directory traversal
            r'@.*@',  # Multiple @ symbols
        ]
        
        for pattern in suspicious_patterns:
            if re.search(pattern, email, re.IGNORECASE):
                validation["issues"].append("Email contains suspicious characters")
                return validation
        
        # Check domain reputation (simplified)
        domain = email.split('@')[1].lower()
        suspicious_domains = [
            '10minutemail.com',
            'tempmail.org',
            'guerrillamail.com',
            # Add more temporary email domains
        ]
        
        if domain in suspicious_domains:
            validation["issues"].append("Temporary email domains not allowed")
            return validation
        
        validation["is_valid"] = True
        return validation
    
    def encrypt_sensitive_data(self, data: str, key: str = None) -> tuple:
        """Simple encryption for sensitive data (use proper encryption in production)"""
        if key is None:
            key = secrets.token_hex(16)
        
        # This is a simple XOR encryption - use proper encryption like AES in production
        encrypted = ""
        for i, char in enumerate(data):
            key_char = key[i % len(key)]
            encrypted += chr(ord(char) ^ ord(key_char))
        
        return encrypted, key
    
    def decrypt_sensitive_data(self, encrypted_data: str, key: str) -> str:
        """Decrypt sensitive data"""
        # Simple XOR decryption
        decrypted = ""
        for i, char in enumerate(encrypted_data):
            key_char = key[i % len(key)]
            decrypted += chr(ord(char) ^ ord(key_char))
        
        return decrypted
    
    def _has_common_patterns(self, password: str) -> bool:
        """Check for common weak password patterns"""
        common_patterns = [
            r'123456',
            r'password',
            r'qwerty',
            r'abc123',
            r'admin',
            r'letmein',
            r'welcome',
            r'monkey'
        ]
        
        password_lower = password.lower()
        for pattern in common_patterns:
            if pattern in password_lower:
                return True
        
        return False
    
    def _get_password_suggestions(self, requirements: Dict) -> List[str]:
        """Get password improvement suggestions"""
        suggestions = []
        
        if not requirements["min_length"]:
            suggestions.append("Use at least 8 characters")
        if not requirements["has_uppercase"]:
            suggestions.append("Include at least one uppercase letter")
        if not requirements["has_lowercase"]:
            suggestions.append("Include at least one lowercase letter")
        if not requirements["has_digit"]:
            suggestions.append("Include at least one number")
        if not requirements["has_special"]:
            suggestions.append("Include at least one special character (!@#$%^&*)")
        if not requirements["no_common_patterns"]:
            suggestions.append("Avoid common passwords and patterns")
        
        return suggestions
    
    def generate_audit_log(self, action: str, user_id: str, details: Dict = None) -> Dict:
        """Generate security audit log entry"""
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "action": action,
            "user_id": user_id,
            "ip_address": "127.0.0.1",  # In real app, get from request
            "user_agent": "TrainBookingSystem/1.0",  # In real app, get from request
            "details": details or {},
            "severity": self._get_action_severity(action)
        }
        
        return log_entry
    
    def _get_action_severity(self, action: str) -> str:
        """Determine severity level of security action"""
        high_severity = ["login_failed", "account_locked", "password_changed"]
        medium_severity = ["login_success", "logout", "session_expired"]
        
        if action in high_severity:
            return "HIGH"
        elif action in medium_severity:
            return "MEDIUM"
        else:
            return "LOW"
    
    def get_security_report(self) -> Dict:
        """Generate security status report"""
        current_time = datetime.now()
        
        # Count active sessions
        active_sessions = 0
        for token, session in self.session_tokens.items():
            expiry = datetime.fromisoformat(session["expires_at"])
            if current_time < expiry:
                active_sessions += 1
        
        return {
            "active_sessions": active_sessions,
            "blocked_ips": len(self.blocked_ips),
            "failed_attempts_tracked": len(self.failed_attempts),
            "security_level": "STANDARD",
            "recommendations": [
                "Enable two-factor authentication",
                "Implement HTTPS encryption",
                "Regular security audits",
                "Password rotation policy"
            ]
        }

class AccessControl:
    """Manage user permissions and access control"""
    
    def __init__(self):
        self.user_roles = {}
        self.role_permissions = {
            "admin": ["all"],
            "operator": ["view_bookings", "create_booking", "cancel_booking"],
            "viewer": ["view_bookings"],
            "customer": ["view_own_bookings", "create_booking", "cancel_own_booking"]
        }
    
    def assign_role(self, user_id: str, role: str) -> bool:
        """Assign role to user"""
        if role in self.role_permissions:
            self.user_roles[user_id] = role
            return True
        return False
    
    def check_permission(self, user_id: str, permission: str) -> bool:
        """Check if user has specific permission"""
        if user_id not in self.user_roles:
            return False
        
        user_role = self.user_roles[user_id]
        role_perms = self.role_permissions.get(user_role, [])
        
        return "all" in role_perms or permission in role_perms
    
    def get_user_permissions(self, user_id: str) -> List[str]:
        """Get all permissions for a user"""
        if user_id not in self.user_roles:
            return []
        
        user_role = self.user_roles[user_id]
        return self.role_permissions.get(user_role, [])

if __name__ == "__main__":
    # Example usage
    security = SecurityManager()
    
    # Test password validation
    password = "MySecurePass123!"
    validation = security.validate_password_strength(password)
    print("Password Validation:", json.dumps(validation, indent=2))
    
    # Test session management
    token = security.create_session("user123")
    print(f"Session Token: {token}")
    
    # Test security report
    report = security.get_security_report()
    print("Security Report:", json.dumps(report, indent=2))
