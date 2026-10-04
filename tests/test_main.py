import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert data["status"] == "healthy"

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_read_items_empty():
    response = client.get("/items/")
    assert response.status_code == 200
    assert response.json() == {}

def test_create_item():
    item_data = {
        "name": "Test Item",
        "description": "A test item",
        "price": 10.99,
        "tax": 1.99
    }
    response = client.post("/items/1", json=item_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Item"
    assert data["price"] == 10.99

def test_read_item():
    # First create an item
    item_data = {
        "name": "Test Item",
        "price": 10.99
    }
    client.post("/items/2", json=item_data)

    # Then read it
    response = client.get("/items/2")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Item"

def test_read_item_not_found():
    response = client.get("/items/999")
    assert response.status_code == 404

def test_update_item():
    # First create an item
    item_data = {
        "name": "Original Name",
        "price": 10.99
    }
    client.post("/items/3", json=item_data)

    # Then update it
    updated_data = {
        "name": "Updated Name",
        "price": 20.99
    }
    response = client.put("/items/3", json=updated_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Updated Name"
    assert data["price"] == 20.99

def test_delete_item():
    # First create an item
    item_data = {
        "name": "To Delete",
        "price": 10.99
    }
    client.post("/items/4", json=item_data)

    # Then delete it
    response = client.delete("/items/4")
    assert response.status_code == 200
    assert response.json() == {"message": "Item deleted"}

    # Verify it's gone
    response = client.get("/items/4")
    assert response.status_code == 404
