from fastapi import FastAPI
from app.models import LoanRequest, EMIResponse, ScheduleResponse
from app.services import calculate_emi, amortization_schedule, prepayment_simulation

app = FastAPI(title="Loan Simulator API")

@app.get("/")
def home():
    return {"message": "Loan Simulator API Running"}

@app.post("/emi/", response_model=EMIResponse)
def get_emi(data: LoanRequest):
    emi = calculate_emi(data.principal, data.rate, data.tenure)
    return {"emi": emi}

@app.post("/schedule/", response_model=ScheduleResponse)
def get_schedule(data: LoanRequest):
    schedule = amortization_schedule(data.principal, data.rate, data.tenure)
    return {"schedule": schedule}

from app.models import PrepaymentRequest

@app.post("/prepayment/")
def simulate_prepayment(data: PrepaymentRequest):
    result = prepayment_simulation(
        data.principal,
        data.rate,
        data.tenure,
        data.prepayment_amount,
        data.prepayment_month
    )
    return result

from app.services import compare_prepayment
from app.models import ComparisonResponse

@app.post("/compare/", response_model=ComparisonResponse)
def compare(data: PrepaymentRequest):
    result = compare_prepayment(
        data.principal,
        data.rate,
        data.tenure,
        data.prepayment_amount,
        data.prepayment_month
    )
    return result