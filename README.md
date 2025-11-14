# 🩺 MediMind - AI-Powered Health Prediction Platform

<div align="center">

![MediMind Banner](frontend/src/assets/medimind-logo-white.svg)

**Your Health, Powered by AI**

</div>

---

## 📋 Table of Contents

- [About](#about)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Machine Learning Models](#machine-learning-models)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [API Documentation](#api-documentation)
- [Contributors](#contributors)
- [License](#license)

---

## 🎯 About

**MediMind** is an intelligent, AI-powered healthcare platform that predicts potential diseases based on user-reported symptoms. The system leverages advanced machine learning algorithms trained on a comprehensive medical dataset to provide accurate disease predictions, personalized doctor recommendations, and practical precautionary measures.

### 🌟 Why MediMind?

- **Accessibility**: Makes healthcare advice accessible, especially in regions with limited medical resources
- **Speed**: Get instant AI-powered health predictions without waiting for appointments
- **Accuracy**: Utilizes ensemble learning with 95%+ prediction accuracy
- **Comprehensive**: Connects users with verified doctors and nearby hospitals
- **24/7 Availability**: AI chatbot provides round-the-clock health assistance

---

## ✨ Features

### 🤖 AI-Powered Prediction
- Multi-symptom analysis using ensemble machine learning models
- Trained on 132 symptoms and 41 diseases
- Real-time disease probability calculations

### 🏥 Healthcare Services
- **Doctor Directory**: Browse and filter verified healthcare professionals by specialization
- **Hospital Locator**: Interactive map showing nearby hospitals with contact information
- **Appointment Booking**: Schedule appointments with doctors directly through the platform
- **Chatbot Assistant**: 24/7 AI-powered chatbot for health queries and symptom analysis

### 👤 User Features
- Secure user authentication and profile management
- Prediction history tracking
- Previous appointment management
- Personalized health recommendations

### 📊 Admin Dashboard
- User management and analytics
- Doctor and hospital database management
- System monitoring and reporting

---


## 🧰 Tech Stack

### Frontend
| Technology | Purpose |
|-----------|---------|
| **React.js 18** | UI framework with Hooks and Context API |
| **Vite** | Fast build tool and dev server |
| **Tailwind CSS** | Utility-first CSS framework |
| **Axios** | HTTP client for API requests |
| **React Router** | Client-side routing |
| **Lucide React** | Modern icon library |
| **Leaflet** | Interactive map integration |

### Backend
| Technology | Purpose |
|-----------|---------|
| **Python 3.10+** | Core programming language |
| **Flask 3.0** | Lightweight web framework |
| **Flask-CORS** | Cross-origin resource sharing |
| **Flask-PyMongo** | MongoDB integration |
| **Flask-JWT-Extended** | JWT authentication |
| **APScheduler** | Background task scheduling |

### Database
| Technology | Purpose |
|-----------|---------|
| **MongoDB Atlas** | Cloud-hosted NoSQL database |
| **PyMongo** | Python MongoDB driver |

### Machine Learning
| Library | Purpose |
|---------|---------|
| **scikit-learn** | ML algorithms and preprocessing |
| **XGBoost** | Gradient boosting framework |
| **NumPy** | Numerical computations |
| **Pandas** | Data manipulation |
| **Pickle** | Model serialization |

## 🧠 Machine Learning Models

### Dataset
- **132 unique symptoms** across medical specialties
- **41 disease categories** including common and critical conditions
- **4,920 training samples** with balanced class distribution

### Model Architecture

Our system uses an **ensemble learning approach** combining multiple classifiers:

1. **Support Vector Machine (SVM)** - Linear kernel for high-dimensional symptom space
2. **Naive Bayes** - Probabilistic predictions based on symptom frequencies
3. **Random Forest** - 100 decision trees for robust feature importance
4. **XGBoost** - Gradient boosting for handling complex symptom patterns

### Voting Classifier
- **Soft voting** strategy combines probability estimates from all models
- Achieves **95%+ accuracy** on test dataset
- Provides confidence scores for each prediction

### Performance Metrics
```
Overall Accuracy: 95.2%
Precision: 94.8%
Recall: 95.1%
F1-Score: 94.9%
```

### Model Training Pipeline
```python
1. Data preprocessing and cleaning
2. Feature encoding (symptom one-hot encoding)
3. Train-test split (80-20)
4. Individual model training
5. Ensemble with VotingClassifier
6. Cross-validation (10-fold)
7. Model serialization with Pickle
```

---

## 🛠️ Installation

### Prerequisites

- **Node.js** (v16 or higher)
- **Python** (v3.10 or higher)
- **MongoDB Atlas** account (or local MongoDB)
- **Git**

### 📦 Backend Setup

1. **Clone the repository**:
```bash
git clone https://github.com/official-ashutosh/MediMind.git
cd MediMind/backend
```

2. **Create and activate virtual environment**:
```bash
# Linux/macOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

3. **Install Python dependencies**:
```bash
pip install -r requirements.txt
```

4. **Create `.env` file** in the `backend` directory:
```env
MONGO_URI=mongodb+srv://<username>:<password>@cluster.mongodb.net/medimind?retryWrites=true&w=majority
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
JWT_SECRET_KEY=your-jwt-secret-key-here
```

5. **Seed the database** (optional but recommended):
```bash
python seed_doctors.py
python seed_hospitals.py
python seed_precautions.py
```

6. **Run the Flask server**:
```bash
flask run
# or
python app.py
```

Server starts at: `http://localhost:5000`

### 💻 Frontend Setup

1. **Navigate to frontend directory**:
```bash
cd ../frontend
```

2. **Install Node.js dependencies**:
```bash
npm install
```

3. **Create `.env` file** in the `frontend` directory:
```env
VITE_BASE_URL=http://127.0.0.1:5000
```

4. **Run the development server**:
```bash
npm run dev
```

Frontend starts at: `http://localhost:5173`

5. **Build for production**:
```bash
npm run build
npm run preview  # Preview production build
```

---

## 📁 Project Structure

```
MediMind/
├── backend/
│   ├── app.py                    # Main Flask application
│   ├── config.py                 # Configuration settings
│   ├── database.py               # MongoDB connection
│   ├── modeltraining.py          # ML model training script
│   ├── requirements.txt          # Python dependencies
│   ├── datasets/                 # Training and testing data
│   │   ├── Training.csv
│   │   └── Testing.csv
│   ├── ml_models/                # Serialized ML models
│   │   └── voting_classifier.pkl
│   ├── routes/                   # API route handlers
│   │   ├── auth_routes.py        # Authentication endpoints
│   │   ├── prediction_routes.py  # Disease prediction API
│   │   ├── doctor_routes.py      # Doctor management
│   │   ├── hospital_routes.py    # Hospital data
│   │   ├── user_routes.py        # User profile
│   │   └── admin_routes.py       # Admin operations
│   └── services/                 # Business logic
│       ├── predictor.py          # ML prediction service
│       ├── chatbot_predictor.py  # Chatbot logic
│       ├── doctor_service.py
│       ├── hospital_service.py
│       └── user_service.py
│
├── frontend/
│   ├── src/
│   │   ├── components/           # React components
│   │   │   ├── mainHome.jsx      # Landing page
│   │   │   ├── login.jsx         # Login page
│   │   │   ├── signup.jsx        # Registration page
│   │   │   ├── Predict.jsx       # Symptom input
│   │   │   ├── SymptomPredictor.jsx  # Prediction results
│   │   │   ├── ChatBot.jsx       # AI chatbot
│   │   │   ├── DoctorList.jsx    # Doctor directory
│   │   │   ├── Hospitals.jsx     # Hospital locator
│   │   │   ├── BookAppointment.jsx   # Booking form
│   │   │   ├── PreviousPrediction.jsx # History
│   │   │   ├── AboutUs.jsx       # About page
│   │   │   └── Navbar.jsx        # Navigation
│   │   ├── context/
│   │   │   └── AuthContext.jsx   # Global auth state
│   │   ├── App.jsx               # Main app component
│   │   ├── main.jsx              # Entry point
│   │   └── index.css             # Global styles
│   ├── public/
│   │   ├── symptoms.txt          # Symptom suggestions
│   │   └── _redirects            # Netlify routing
│   ├── package.json
│   ├── vite.config.js
│   └── tailwind.config.js
│
└── README.md
```

---

## 📡 API Documentation

### Base URL
```
Development: http://localhost:5000
Production: https://your-api-domain.com
```

### Authentication Endpoints

#### Register User
```http
POST /auth/register
Content-Type: application/json

{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "securepassword",
  "age": 30,
  "gender": "male",
  "contact_no": "+1234567890",
  "address": "123 Main St"
}
```

#### Login
```http
POST /auth/login
Content-Type: application/json

{
  "email": "john@example.com",
  "password": "securepassword"
}

Response: { "token": "jwt-token", "user": {...} }
```

### Prediction Endpoints

#### Predict Disease
```http
POST /predict
Authorization: Bearer <token>
Content-Type: application/json

{
  "symptoms": ["fever", "cough", "fatigue"]
}

Response: {
  "disease": "Common Cold",
  "confidence": 0.92,
  "precautions": [...],
  "medications": [...]
}
```

#### Get Prediction History
```http
GET /user/predictions
Authorization: Bearer <token>
```

### Doctor Endpoints

#### Get All Doctors
```http
GET /doctors?specialization=Cardiologist&location=New York
```

#### Book Appointment
```http
POST /appointments
Authorization: Bearer <token>
Content-Type: application/json

{
  "doctor_id": "doc123",
  "date": "2025-11-20",
  "time": "10:00 AM",
  "reason": "Regular checkup"
}
```

### Hospital Endpoints

#### Get Nearby Hospitals
```http
GET /hospitals?lat=40.7128&lng=-74.0060&radius=10
```

---

## 👥 Contributors

<table>
  <tr>
    <td align="center">
      <img src="frontend/src/assets/ashu.jpeg" width="100px;" alt="Ashutosh"/>
      <br />
      <sub><b>Ashutosh</b></sub>
      <br />
      <sub>Full Stack & ML</sub>
    </td>
    <td align="center">
      <img src="frontend/src/assets/deepak.jpeg" width="100px;" alt="Deepak"/>
      <br />
      <sub><b>Deepak</b></sub>
      <br />
      <sub>Backend & Database</sub>
    </td>
    <td align="center">
      <img src="frontend/src/assets/hmt.jpeg" width="100px;" alt="Hemant"/>
      <br />
      <sub><b>Hemant</b></sub>
      <br />
      <sub>ML & Data Analysis </sub>
    </td>
    <td align="center">
      <img src="frontend/src/assets/pooni.jpeg" width="100px;" alt="Poonam"/>
      <br />
      <sub><b>Poonam</b></sub>
      <br />
      <sub>Frontend & UI/UX</sub>
    </td>
  </tr>
</table>

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Dataset sourced from Kaggle's Medical Symptom Disease Database
- Icons from Lucide React
- Map integration powered by Leaflet
---

<div align="center">

**Made with ❤️ by the MediMind Team**

© 2025 MediMind - All Rights Reserved

*Empowering healthcare through artificial intelligence*

</div>
