from pydantic import BaseModel, Field

class LoanRequest(BaseModel):
    principal: float = Field(..., gt=0, example=100000)
    rate: float = Field(..., gt=0, example=10)
    tenure: int = Field(..., gt=0, example=12)


class EMIResponse(BaseModel):
    emi: float


class ScheduleItem(BaseModel):
    month: int
    emi: float
    principal_paid: float
    interest_paid: float
    remaining_balance: float


class ScheduleResponse(BaseModel):
    schedule: list[ScheduleItem]

class PrepaymentRequest(BaseModel):
    principal: float = Field(..., gt=0)
    rate: float = Field(..., gt=0)
    tenure: int = Field(..., gt=0)
    prepayment_amount: float = Field(..., gt=0)
    prepayment_month: int = Field(..., gt=0)

class ComparisonResponse(BaseModel):
    without_prepayment: dict
    with_prepayment: dict
    difference: dict