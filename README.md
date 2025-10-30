# 📢 Hamari Awaaz (Our Voice) - MGNREGA Performance Dashboard

### Table of Contents
- [🎯 Project Goal & Context](#-project-goal--context-high-impact-summary)
- [✨ Key Features (The Brags)](#-key-features-the-brags)
- [🛠️ Tech Stack & Architecture](#️-tech-stack--architecture)
- [🚀 Quick Deployment Guide](#-quick-deployment-guide)
- [📂 Repository Structure](#-repository-structure)
- [⚖️ License](#️-license)

---

## 🎯 Project Goal & Context (High-Impact Summary)

**Hamari Awaaz (Our Voice)** is a high-performance, containerized dashboard designed to visualize key **MGNREGA performance metrics** for Rajasthan, India.  

This project tackles the challenge of **unreliable government APIs** by implementing a **decoupled, data-caching architecture** using Docker.  
It ensures stability, security, and cost-efficiency with **zero-cost deployment** options via services like the **Render Free Tier**.

The dashboard delivers **accessibility and inclusivity**, focusing on **low-literacy populations** through high-contrast visuals, intuitive icons, and essential **Hindi/Hinglish** terms.  
The goal: make government performance data **transparent, understandable, and actionable** at the grassroots level.

---

## ✨ Key Features (The Brags)

- **Low-Literacy UI/UX**  
  Built with Tailwind CSS featuring large fonts, high-contrast colors, and color-coded performance indicators  
  (green = good, yellow = moderate, red = poor).

- **Fully Dockerized**  
  Self-contained application with a single Docker container—no dependency issues, easy cross-cloud deployment  
  (AWS, GCP, Render, Cloud Run).

- **Rajasthan-Specific Data**  
  Uses publicly available district-wise MGNREGA data for real and relevant performance visualization.

- **Decoupled Architecture**  
  Eliminates risk of live API downtime or lag with preprocessed local caching for consistent real-time experience.

- **Geolocation Bonus Feature**  
  Detects user location via browser API and highlights local district metrics instantly.

---

## 🛠️ Tech Stack & Architecture

| Category         | Technology               | Purpose                                                       |
|------------------|---------------------------|---------------------------------------------------------------|
| **Backend**      | Python 3                 | Core application logic and routing                            |
| **Web Framework**| Flask                    | Lightweight web server for handling requests                  |
| **Data Processing** | Pandas               | Efficient data cleaning, analysis, and KPI generation         |
| **Frontend**     | Jinja2, HTML5, Tailwind CSS | Responsive, accessible UI templates                         |
| **Deployment**   | Docker                   | Containerization for stable, portable, and scalable deployment |

---

## 🚀 Quick Deployment Guide

Deploy instantly using the included **Dockerfile**.

### 1. Prerequisites
Make sure **Docker** is installed on your system or VPS/VM.

### 2. Build the Docker Image
Navigate to the project root (where the Dockerfile is located) and run:
```docker build -t mgnrega-app .```

### 3. Run the Container
Launch the containerized app on port **8088**:
```docker run -d -p 8088:5000 mgnrega-app```


### 4. Access the Dashboard
- **Local Access:** [http://localhost:8088](http://localhost:8088)  
- **VPS/VM Access:** [http://<YOUR_VM_IP_ADDRESS>:8088](http://<YOUR_VM_IP_ADDRESS>:8088)

---

## 📂 Repository Structure
```
.
├── Dockerfile               # Defines the container environment
├── app.py                   # Flask application and data logic
├── requirements.txt         # Python dependencies (Flask, Pandas)
├── rajasthan_data.csv       # Local cached dataset for Rajasthan
└── templates/
    └── index.html           # Frontend UI
```
---

## ⚖️ License

This project is licensed under the **MIT License**.  
You may freely modify and reuse the code for both commercial and private use,  
as long as you include the original copyright.
