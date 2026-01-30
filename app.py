from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict
from agent import summary_genrator

app = FastAPI()


# -----------------------
# Input Model (3 inputs)
# -----------------------
class InputData(BaseModel):
    signals: Dict  # Python dictionary input
    email_content: str  # String input 1
    label: str  # String input 2


# -----------------------
# Output Model
# -----------------------
class OutputData(BaseModel):
    result: str


# -----------------------
# FastAPI Route
# -----------------------
@app.post("/process", response_model=OutputData)
async def process_data(input_data: InputData):

    # Extract inputs
    signals = input_data.signals
    email_content = input_data.email_content
    label = input_data.label

    # --------------------
    # Your processing logic
    # --------------------
    # Example logic: combine everything
    inp = f"this is my 68 signals {signals} extract from email. This my email content {email_content}. This classification output {label}"

    result = summary_genrator(inp)
    # Return the required format
    return {"result": result}


# -----------------------
# Run using:
# uvicorn app:app --reload
# -----------------------
