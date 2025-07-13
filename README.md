# Event Management API
A simple event management API built using FastAPI.

## Core features include:
- **User Management**
- **Event Management**
- **Speaker Management**
- **Registration Management**
- **Simple Validation**
- **Modular Structure**
- **HTTP Status Codes**

Follow these steps to set up and run the Event Management API:
### 1. Prerequisites
Ensure that at least Python 3.9+ is installed on your system.

### 2. Create a Virtual Environment (Recommended)
Always use a virtual environment to manage dependencies:
python -m venv venv

### 3. Activate the Virtual Environment
On Windows:
venv\Scripts\activate

On macOS/Linux:
source venv/bin/activate

### 4. Install Dependencies
Install the required dependencies using pip:
pip install "fastapi[standard]"

### 5. Run the Application
Navigate to the root directory of the project(where main.py is located) and run the application using Uvicorn:
uvicorn main:app --reload
The --reload flag will automatically restart the server when code changes.

### 6. Access the API Documentation
Once the server is running, you can access the interactive API documentation(Swagger UI) at http://127.0.0.1:8000/docs.









