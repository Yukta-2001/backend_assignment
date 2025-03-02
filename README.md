# Backend Assignment - Django Web Application

## **Overview**
This project is a backend application built with **Django and Django Channels** that integrates:
- **Google OAuth 2.0 API** for user authentication.
- **Google Drive API** for file uploads and retrieval.
- **WebSockets** for real-time user chat.

---

## **Features**
✅ **Google Authentication**
- Users can log in via Google OAuth 2.0.
- Returns authentication data upon successful login.

✅ **Google Drive Integration**
- Upload files to Google Drive.
- Fetch and download files from Google Drive.

✅ **WebSocket-based Real-Time Chat**
- Enables real-time messaging between two users.

---

## **Installation & Setup**
### **1. Clone the Repository**
```bash
git clone https://github.com/yourusername/backend_assignment.git

cd backend_assignment
```
## 2. Create a Virtual Environment
```
python -m venv myenv
source myenv/bin/activate   # MacOS/Linux
myenv\Scripts\activate      # Windows
```
## 3. Install Dependencies
```
pip install -r requirements.txt
```
## 4. Set Up Environment Variables
Create a .env file in the project root and add:
```
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
GOOGLE_REDIRECT_URI=http://127.0.0.1:8000/auth/callback/
SECRET_KEY=your_django_secret_key
DEBUG=True
```
## 5. Apply Migrations
```
python manage.py migrate
```
## 6. Run the Development Server
```
python manage.py runserver
The server will start at http://127.0.0.1:8000/.
```

# API Endpoints

This document outlines the available API endpoints for the application.

| Feature                | Method      | Endpoint         | Description                                     |
|------------------------|-------------|------------------|-------------------------------------------------|
| Google OAuth Login     | GET         | `/auth/login/`    | Initiates Google Authentication                 |
| Google OAuth Callback  | GET         | `/auth/callback/` | Handles Google OAuth response                   |
| Upload File            | POST        | `/drive/upload/`  | Uploads a file to Google Drive                  |
| List Files             | GET         | `/drive/list/`    | Fetches list of files from Google Drive         |
| WebSocket Chat         | WebSocket   | `/ws/chat/`       | Enables real-time chat                          |

# 🐳 Docker Setup
## 1️⃣ Build & Run with Docker
```
docker build -t django-backend .
docker run -p 8000:8000 django-backend
```
## 2️⃣ Using Docker Compose

 Run the application with PostgreSQL using Docker Compose:
```
docker-compose up --build
```
## Testing with Postman

A Postman collection (`postman_collection.json`) is provided for easy testing of the API.

To test the API:

      1. Import the `postman_collection.json` file into Postman.
      2. Set the `{{base_url}}` variable to `http://127.0.0.1:8000` for local testing.

## Deployment

This project can be deployed to various platforms, including Heroku, Render, and Railway.

### Render Deployment

To deploy to Render:

1. Push the code to a GitHub repository.
2. Create a new web service on Render, linking it to your GitHub repository.
3. Configure the necessary environment variables in the Render dashboard.
4. Deploy the project.
# Testing with Postman
```
Import the Postman Collection
Open Postman.
Click Import → Select postman_collection.json.
Set {{base_url}} as http://127.0.0.1:8000.
```
## Deployment
You can deploy this project on Heroku, Render, or Railway.

Deploy to Render
Push the code to GitHub.
Create a new Render project.
Set environment variables in the dashboard.
Deploy the project.
Technologies Used
Django & Django REST Framework
Django Channels (for WebSockets)
Google OAuth 2.0 & Google Drive API
PostgreSQL (or SQLite for local testing)
WebSockets for real-time communication

