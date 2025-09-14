from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

app = FastAPI()

# --- Helper Function ---
def generate_customer_id(user_id: int) -> str:
    return f"CUST-{user_id:04d}"

# --- Attachment Model ---
class Attachment(BaseModel):
    id: str
    name: str
    size: int  # in bytes
    type: str
    url: str

# --- Message Model ---
class Message(BaseModel):
    id: str
    customerId: str
    subject: str
    preview: str
    body: str
    timestamp: datetime
    from_: str = Field(..., alias="from")
    to: str
    status: str
    priority: str
    thread: List[str]
    attachments: List[Attachment]

# --- API Route ---
@app.get("/message", response_model=Message)
def get_message():
    customer_id = generate_customer_id(123)
    return {
        "id": "1",
        "customerId": customer_id,
        "subject": "Urgent: Need Boeing 737-800 Landing Gear Assembly",
        "preview": "We require immediate delivery of landing gear assembly for our Boeing 737-800 fleet...",
        "body": (
            "Dear Team,\n\n"
            "We require immediate delivery of landing gear assembly for our Boeing 737-800 fleet. "
            "This is a critical requirement as we have scheduled maintenance for 3 aircraft next week.\n\n"
            "Part Numbers Required:\n"
            "- Main Landing Gear: MLG-737-800-A\n"
            "- Nose Landing Gear: NLG-737-800-B\n"
            "- Brake Assembly: BA-737-800-C\n\n"
            "Please provide availability and pricing ASAP.\n\n"
            "Best regards,\n"
            "Skyline Airlines Procurement"
        ),
        "timestamp": datetime(2024, 12, 20, 10, 30, 0),
        "from": customer_id,
        "to": "sales@aeroparts.com",
        "status": "unread",
        "priority": "urgent",
        "thread": [],
        "attachments": [
            {
                "id": "att1",
                "name": "Technical_Specifications.pdf",
                "size": 2456789,
                "type": "application/pdf",
                "url": "#"
            }
        ]
    }
