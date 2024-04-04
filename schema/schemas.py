def individual_serial(todo) -> dict:
    return {
        "id": str(todo["_id"]),
        "title": todo["title"],
        "description": todo["description"],
        "status": todo["status"],
    }

def list_serial(todos) -> list:
    return [individual_serial(todo) for todo in todos]