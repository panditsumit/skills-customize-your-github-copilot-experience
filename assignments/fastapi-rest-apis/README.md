# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build fast, modern REST APIs using the FastAPI framework. You'll create a backend service that handles HTTP requests, manages data, and returns responses following REST principles and best practices.

## 📝 Tasks

### 🛠️ Create a Basic TODO API

#### Description
Build a REST API for managing a simple to-do list. Create endpoints that allow users to create, read, update, and delete TODO items. Implement proper HTTP methods (GET, POST, PUT, DELETE) and status codes.

#### Requirements
Completed program should:

- Create a GET endpoint that retrieves all TODO items
- Create a POST endpoint that adds a new TODO item with validation
- Create a PUT endpoint that updates an existing TODO item
- Create a DELETE endpoint that removes a TODO item
- Return appropriate HTTP status codes (200, 201, 404, etc.)
- Include basic request/response validation using Pydantic models
- Store data in memory (list or dictionary)


### 🛠️ Enhance API with Features

#### Description
Extend your TODO API with additional functionality to make it production-ready. Add features for filtering, searching, and better data management.

#### Requirements
Completed program should:

- Add filtering by completion status (completed/incomplete)
- Implement search functionality to find TODOs by keywords
- Add timestamps for when items are created and updated
- Include query parameters for sorting and pagination
- Add error handling with descriptive error messages
- Include API documentation using FastAPI's built-in Swagger UI
- Persist data to a JSON file (optional challenge)
