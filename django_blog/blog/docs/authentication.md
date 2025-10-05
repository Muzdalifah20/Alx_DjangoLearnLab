Overview
Manages user registration, login, logout, and profile editing via Django’s built-in and custom views/forms.

Components

Registration: Custom form extending UserCreationForm with email.

Login/Logout: Django’s built-in LoginView and LogoutView.

Profile Editing: Custom view and forms updating user info and extended profile.

Security Features

All forms include CSRF tokens.

Passwords are securely hashed by Django.

User sessions are securely managed and logged out on request.

Testing Instructions
Run python manage.py test to execute test cases covering registration, login, logout, and profile updates.

User Interaction

Register: /register/

Login: /login/

Logout: /logout/

Profile view/update: /profile/
