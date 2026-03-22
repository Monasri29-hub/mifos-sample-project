from decimal import Decimal, getcontext

getcontext().prec = 10

def calculate_emi(principal, annual_rate, tenure_months):
    monthly_rate = Decimal(annual_rate) / Decimal(12 * 100)
    principal = Decimal(principal)
    tenure = Decimal(tenure_months)

    emi = principal * monthly_rate * (1 + monthly_rate) ** tenure / ((1 + monthly_rate) ** tenure - 1)
    return round(emi, 2)


def amortization_schedule(principal, annual_rate, tenure_months):
    emi = calculate_emi(principal, annual_rate, tenure_months)
    balance = Decimal(principal)
    monthly_rate = Decimal(annual_rate) / Decimal(12 * 100)

    schedule = []

    for month in range(1, tenure_months + 1):
        interest = balance * monthly_rate
        principal_paid = emi - interest
        balance -= principal_paid

        schedule.append({
            "month": month,
            "emi": float(emi),
            "principal_paid": float(principal_paid),
            "interest_paid": float(interest),
            "remaining_balance": float(balance)
        })

    return schedule

from decimal import Decimal

def prepayment_simulation(principal, rate, tenure, prepayment_amount, prepayment_month):
    principal = Decimal(principal)
    rate = Decimal(rate)
    tenure = int(tenure)
    prepayment_amount = Decimal(prepayment_amount)

    emi = Decimal(calculate_emi(principal, rate, tenure))
    monthly_rate = rate / Decimal(12 * 100)

    balance = principal
    total_interest = Decimal(0)
    months_taken = 0

    for month in range(1, tenure + 1):
        if balance <= 0:
            break

        interest = balance * monthly_rate
        principal_paid = emi - interest

        # Apply prepayment safely
        if month == prepayment_month:
            if prepayment_amount >= balance:
                balance = Decimal(0)
                months_taken += 1
                break
            else:
                balance -= prepayment_amount

        # Prevent overpayment by EMI
        if principal_paid >= balance:
            total_interest += interest
            balance = Decimal(0)
            months_taken += 1
            break

        balance -= principal_paid
        total_interest += interest
        months_taken += 1

    return {
        "remaining_balance": float(balance),
        "total_interest_paid": float(total_interest),
        "months_taken": months_taken
    }

    return {
        "remaining_balance": float(balance),
        "total_interest_paid": float(total_interest),
        "months_taken": len(schedule)
    }

def compare_prepayment(principal, rate, tenure, prepayment_amount, prepayment_month):
    # WITHOUT prepayment
    normal_schedule = amortization_schedule(principal, rate, tenure)
    total_interest_normal = sum(item["interest_paid"] for item in normal_schedule)
    months_normal = len(normal_schedule)

    # WITH prepayment
    prepay_result = prepayment_simulation(
        principal, rate, tenure, prepayment_amount, prepayment_month
    )

    return {
        "without_prepayment": {
            "total_interest": total_interest_normal,
            "months": months_normal
        },
        "with_prepayment": {
            "total_interest": prepay_result["total_interest_paid"],
            "months": prepay_result["months_taken"]
        },
        "difference": {
            "interest_saved": total_interest_normal - prepay_result["total_interest_paid"],
            "months_reduced": months_normal - prepay_result["months_taken"]
        }
    }