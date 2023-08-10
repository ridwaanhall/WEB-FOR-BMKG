import geopy
from geopy.geocoders import Nominatim
import smtplib
from email.mime.text import MIMEText

def get_location():
    # Create a geocoder instance
    geolocator = Nominatim(user_agent="location_app")
    
    # Obtain the location coordinates
    location = geolocator.geocode("Your Location Query")
    
    return location.latitude, location.longitude

def send_email(latitude, longitude):
    # Email configuration
    sender_email = "your_email@example.com"
    receiver_email = "netika5338@kameili.com"
    subject = "Location Details"
    message = f"Latitude: {latitude}\nLongitude: {longitude}"
    
    # Create the email
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email
    
    # Send the email
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    username = "your_gmail_username"
    password = "your_gmail_password"
    
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(username, password)
        server.send_message(msg)
    
    print("Email sent successfully!")

# Get location coordinates
latitude, longitude = get_location()

# Send email with location details
send_email(latitude, longitude)
