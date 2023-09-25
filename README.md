# FastAPI eCommerce Application

## Overview

This FastAPI eCommerce application is a sample project designed to provide a foundation for building an eCommerce platform similar to Flipkart or Amazon. It includes APIs for managing products and orders, user information, and basic MongoDB integration.

## Features

- List all available products in the system.
- Create new orders with order details, items, and user addresses.
- Retrieve orders from the system with pagination support.
- Fetch a single order by its unique Order ID.
- Update product details, including available quantity.

## Getting Started

### Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.6 or higher
- MongoDB (Make sure MongoDB is running locally on the default port 27017, or update the MongoDB connection URI in `database/mongo.py`)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/your-ecommerce-project.git```
   
2. Install dependencies:
```bash
   cd your-ecommerce-project
   pip install -r requirements.txt
```
### Running the Application

```bash
uvicorn main:app --reload
```
The application should be accessible at `http://localhost:8000`

### API Documentation

you can access the API documentation and test the endpoints using the Swagger UI provided by FastAPI. Open your web browser and navigate to:

```bash
http://localhost:8000/docs
```

### Usage
. Use the API endpoints to create and manage products, orders, and user information.
. Update the code in the database/mongo.py file to integrate with your MongoDB database.
. Customize and extend the functionality to meet your specific requirements.

### Project Structure
The project structure follows best practices for organizing a FastAPI application:

. main.py: The main application script.
. api/: Contains API route definitions.
. models/: Includes Pydantic models for data validation.
. database/: Manages MongoDB database connections and operations.
. requirements.txt: Lists project dependencies.
. README.md: The documentation you're currently reading.

