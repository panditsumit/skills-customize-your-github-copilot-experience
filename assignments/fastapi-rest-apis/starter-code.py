"""
FastAPI REST API Starter Code
Build a TODO API with Create, Read, Update, Delete operations
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# Initialize FastAPI app
app = FastAPI(
    title="TODO API",
    description="A simple TODO management REST API",
    version="1.0.0"
)

# Pydantic models for request/response validation
class TodoItem(BaseModel):
    """Model for a TODO item"""
    id: Optional[int] = None
    title: str
    description: Optional[str] = None
    completed: bool = False
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Learn FastAPI",
                "description": "Complete the FastAPI assignment",
                "completed": False
            }
        }


# In-memory storage for TODO items
todos_db: List[TodoItem] = [
    TodoItem(
        id=1,
        title="Sample TODO",
        description="This is a sample TODO item",
        completed=False,
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
]

# Track the next ID
next_id = 2


# TODO: Implement GET endpoint to retrieve all TODO items
# Endpoint: GET /todos
# Response: List of all TODO items


# TODO: Implement POST endpoint to create a new TODO item
# Endpoint: POST /todos
# Request body: TodoItem
# Response: Created TODO item with ID and timestamps


# TODO: Implement GET endpoint to retrieve a specific TODO by ID
# Endpoint: GET /todos/{todo_id}
# Response: Single TODO item or 404 error


# TODO: Implement PUT endpoint to update a TODO item
# Endpoint: PUT /todos/{todo_id}
# Request body: Updated TodoItem fields
# Response: Updated TODO item


# TODO: Implement DELETE endpoint to delete a TODO item
# Endpoint: DELETE /todos/{todo_id}
# Response: Confirmation message or 404 error


# Root endpoint for API health check
@app.get("/")
async def root():
    """Health check endpoint"""
    return {"message": "TODO API is running!", "status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
