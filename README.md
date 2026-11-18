# 🏥 Hospital Fees API

A REST API built with **Python and FastAPI** that provides predefined hospital treatment cost breakdowns for 90 different diseases.

The API allows users to submit a disease name and retrieve its corresponding doctor fee, test charges, medicine costs, and total estimated bill.

## 🚀 Features

- Supports 90 predefined diseases.
- Retrieves billing information using disease names.
- Provides doctor consultation fees.
- Provides medical test charges.
- Provides medicine costs.
- Returns the total estimated bill.
- Uses FastAPI for REST API development.
- Automatic API documentation with Swagger UI.

## 🛠️ Technologies Used

- Python
- FastAPI
- Uvicorn
- REST API

## 📂 Project Structure

```text
Api_for_hospital-_bills/
│
├── main.py
└── README.md
```

## ⚙️ Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/deep-dharmani/Api_for_hospital-_bills.git
```

### 2. Navigate to Project Directory

```bash
cd Api_for_hospital-_bills
```

### 3. Create Virtual Environment

```bash
python -m venv venv
```

### 4. Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install fastapi uvicorn
```

### 6. Run the Application

```bash
uvicorn main:hospital_fees_api --reload
```

## 📡 API Usage

### Endpoint

```http
POST /
```

### Request Parameter

| Parameter | Type | Description |
|---|---|---|
| disease | string | Name of the disease |

## 📖 API Documentation

After running the server, access the interactive documentation:

- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

## 🎯 Learning Objectives

This project helped me practice:

- Building REST APIs using FastAPI.
- Understanding HTTP POST requests.
- Handling query parameters.
- Working with Python dictionaries.
- Implementing conditional logic.
- Returning structured API responses.

## ⚠️ Disclaimer

This project uses predefined sample billing data for educational purposes. The costs are illustrative and should not be considered actual hospital prices, medical advice, or verified treatment estimates.

## 👨‍💻 Author

**Deep Dharmani**

Python Developer | Learning Backend Development

- GitHub: https://github.com/deep-dharmani
- LinkedIn: https://www.linkedin.com/in/deep-dharmani/

---

⭐ If you find this project interesting, feel free to explore the repository!
