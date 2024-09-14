# WhatsApp Clone - Mumbai University Project

This project is a simple **WhatsApp Clone** built using **Django** and **SQLite** for educational purposes. It provides users the ability to register, log in, send messages, and participate in real-time chat conversations.

## Features

- **User Registration and Login**: Users can create an account and log in to the platform.
- **Chat Functionality**: Users can send and receive messages, participate in 1-on-1 chats.
- **Message History**: Users can view the history of messages in each chat.
- **User-Friendly Interface**: A clean and simple interface for users to interact with the platform.

## Project Structure

- `WhatsAppClone/`: Main project folder.
- `chat/`: Contains the app logic for chats and messages.
- `templates/`: HTML templates for rendering user interface (login, registration, chat).
- `static/`: CSS files for styling the user interface.
- `db.sqlite3`: SQLite database file for storing user data and chat history.

## Requirements

- **Python 3.x**
- **Django 3.x or later**

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/WhatsAppClone.git
   cd WhatsAppClone

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`

3. **Install Dependencies**: Install Django and other necessary dependencies:
   ```bash
   pip install django

4. **Run Migrations**: Apply the migrations to create the database schema:
   ```bash
   python manage.py migrate

5. **Run the Development Server**: Start the Django development server:
   ```bash
   python manage.py runserver

6. **Access the Application**: Open your browser and go to `http://127.0.0.1:8000/` to access the WhatsApp clone.

##How to Use
- **Register**: Create a new account by filling in the registration form.
- **Login**: Use your registered username and password to log in.
- **Chats**: View a list of your active chats. You can click on a chat to view and send messages.
- **Send Messages**: Send new messages in the chat interface.

##Customization
You can customize the project by:

- Adding more chat features like group chat.
- Enhancing the chat interface with AJAX for real-time message updates.
- Extending the user profile to include more details.
