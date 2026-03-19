# 🚗 Car Dealership & Reviews Management System

> **IBM Full Stack Software Developer Capstone Project**
>
> Final capstone for the IBM Full Stack Software Developer Professional Certificate on Coursera. Demonstrates a comprehensive real-world application using microservices architecture, containerization, and cloud-native deployment.

---

## 🚀 Project Overview

A full-stack platform where users can browse car dealerships, view detailed information about car models, and read or submit reviews. Integrates a sentiment analysis microservice to automatically categorize user reviews as **Positive**, **Neutral**, or **Negative**.

### Key Features

- 🔐 **User Authentication** — Secure Sign-up, Login, and Logout functionality
- 🏢 **Dealership Management** — Dynamic listing of dealerships filtered by state
- ✍️ **Review System** — Users can post reviews for specific dealerships
- 🤖 **AI Sentiment Analysis** — Integration with Watson NLP to analyze review sentiment
- 📱 **Responsive UI** — Built with React for a seamless user experience

---

## 🛠️ Tech Stack

| Component       | Technology                                      |
|-----------------|-------------------------------------------------|
| **Frontend**    | React.js, Bootstrap, HTML5, CSS3                |
| **Backend**     | Django (Python), SQLite (Development)           |
| **Microservices** | Node.js, Express (Sentiment Analysis)         |
| **AI/ML**       | Watson NLP Library                              |
| **DevOps**      | Docker, Kubernetes (K8s), IBM Cloud Container Registry |
| **CI/CD**       | GitHub Actions (Linting & Testing)              |

---

## 🏗️ Architecture & Deployment

The project follows a modern deployment workflow:

1. **Linting** — Automated PEP8 and JSHint checks via GitHub Actions
2. **Containerization** — The Django backend is containerized using a multi-stage `Dockerfile`
3. **Orchestration** — Managed and scaled on a Kubernetes cluster
4. **Cloud Registry** — Images are hosted on IBM Cloud Container Registry (ICR)

---

## 📁 Project Structure

```
.
├── frontend/               # React.js application source code
├── server/
│   ├── djangoapp/          # Main Django application logic
│   ├── djangoproj/         # Django project configuration
│   ├── Dockerfile          # Containerization recipe
│   ├── deployment.yaml     # Kubernetes deployment configuration
│   ├── entrypoint.sh       # Database migration and startup script
│   └── manage.py           # Django management utility
└── .github/workflows/      # CI/CD pipeline for linting
```

---

## 🔧 Installation & Setup

To run this project locally:

**1. Clone the repository**

```bash
git clone https://github.com/catnipp9/xrwvm-fullstack_developer_capstone.git
cd xrwvm-fullstack_developer_capstone
```

**2. Install Backend Dependencies**

```bash
pip install -r requirements.txt
```

**3. Install Frontend Dependencies**

```bash
cd server/frontend && npm install && npm run build
```

**4. Run Migrations**

```bash
python manage.py migrate
```

**5. Start the Server**

```bash
python manage.py runserver
```

---

## 🎓 Acknowledgments

- **IBM Skills Network** — for the lab environment and cloud infrastructure
- **Coursera** — for providing the platform for the Full Stack Developer Professional Certificate
