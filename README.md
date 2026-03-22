# Intelligent Loan Amortization and What-If Simulation Service

A modular FastAPI-based financial microservice for loan amortization, EMI computation, and advanced what-if financial simulations such as prepayment and loan restructuring.

This project is designed for integration with the Mifos X ecosystem, enabling real-time financial decision-making for borrowers and loan officers.

---

## 🚀 Project Overview

Traditional loan systems generate static repayment schedules and lack dynamic financial exploration capabilities.

This project introduces a real-time loan simulation engine that allows users to:

- Compute EMI schedules
- Generate amortization tables
- Simulate loan prepayments
- Compare multiple repayment scenarios
- Analyze financial impact instantly

---

## 🧠 Key Features

- EMI calculation engine using high-precision arithmetic (Decimal)
- Loan amortization schedule generator
- Prepayment simulation (what-if analysis)
- Comparison between normal vs modified repayment plans
- RESTful API using FastAPI
- Input validation using Pydantic models
- Modular microservice architecture

---

## 🏗 System Architecture

Client (Web / Mobile / Mifos UI)
        ↓
FastAPI API Layer
        ↓
-------------------------------------
| EMI Engine                        |
| Amortization Engine              |
| Prepayment Simulation Engine     |
-------------------------------------
        ↓
Comparison & Analytics Layer
        ↓
JSON Response API

---

## 📡 API Endpoints

### EMI Calculation
POST /emi

### Amortization Schedule
POST /schedule

### Prepayment Simulation
POST /prepayment

### Comparison Engine
POST /compare

---

## 🧪 Example Request

{
  "principal": 100000,
  "rate": 7.5,
  "tenure": 24
}

---

## 📦 Tech Stack

- Python
- FastAPI
- Pydantic
- REST API
- Financial Mathematics
- Microservices Architecture

---

## 📁 Project Structure

app/
├── main.py          # FastAPI entry point
├── models.py        # Pydantic request/response models
├── services.py      # Core business logic (EMI, amortization, prepayment, comparison)
├── __pycache__/
requirements.txt

---

## 🎯 Benefits

- Helps borrowers understand repayment impact before making decisions
- Assists loan officers in restructuring analysis
- Improves transparency in financial systems
- Reduces manual calculation errors
- Enables future AI-driven financial advisory systems

---

## 🔮 Future Improvements

- Redis caching for performance optimization
- Visualization dashboard for EMI trends
- AI-based financial recommendation system
- Docker + Kubernetes deployment
- Mobile app integration via API

---

## 👩‍💻 Author

Monasri Kundeti

GitHub: https://github.com/Monasri29-hub  
LinkedIn: https://www.linkedin.com/in/kundeti-monasri-3650ba326/

---

## 📚 References

- Mifos X Loan Product Documentation
- Financial Mathematics (Amortization Theory)
- FastAPI Official Documentation

---

## ⭐ Acknowledgement

This project is developed as part of preparation for Google Summer of Code (GSoC) 2026 under The Mifos Initiative.
