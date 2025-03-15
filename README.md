Below is an updated `README.md` template that includes instructions for running both the **Streamlit** and **FastAPI** apps. Adjust file names, paths, or commands if your project structure differs.

---

# Social Security Claiming Simulator

**Disclaimer:** This program is **not** legal, financial, or tax advice. It is intended purely for informational and educational purposes. **Please consult a professional** (financial adviser, attorney, certified public accountant, etc.) to discuss how claiming decisions affect you personally.

---

## Table of Contents
1. [Overview](#overview)  
2. [Features](#features)  
3. [Getting Started](#getting-started)  
   - [Requirements](#requirements)  
   - [Installation](#installation)  
   - [Running the Streamlit App](#running-the-streamlit-app)  
   - [Running the FastAPI App](#running-the-fastapi-app)  
4. [Usage](#usage)  
5. [Developer Instructions](#developer-instructions)  
   - [Cloning the Repository](#cloning-the-repository)  
   - [Running Locally](#running-locally)  
6. [Contributing](#contributing)  
7. [Disclaimer](#disclaimer)

---

## Overview
The **Social Security Claiming Simulator** is a tool that helps users explore how different claiming ages and other assumptions can impact retirement benefits. The project includes both a **Streamlit** interactive web application and a **FastAPI** server, offering flexibility in how you run and interact with the simulator.

> **Note**: The results are based on user inputs, built-in assumptions, and simplifications. Real-world outcomes may differ due to inflation, legislative changes, and other unmodeled variables.

---

## Features
- **Multiple Claiming Age Comparisons**: Compare Social Security benefits at various ages (e.g., early claiming vs. full retirement age vs. delayed claiming).  
- **Lifetime Projection**: Estimate how total lifetime benefits might vary under different scenarios.  
- **Parameter Adjustments**: Modify assumptions for cost-of-living adjustments (COLA), discount rates, mortality assumptions, etc.  
- **Interactive Analysis**: The Streamlit app lets you tweak inputs on the fly, while the FastAPI server can be integrated with other tools or GUIs.

---

## Getting Started

### Requirements
- **Python 3.7+**  
- (Recommended) A virtual environment tool like `venv` or `conda`  
- **Streamlit** and **FastAPI** (both can be installed from `requirements.txt`)  
- **Uvicorn** (to run the FastAPI app)

### Installation
1. **Clone or download** the repository to your local machine:
   ```bash
   git clone https://github.com/jtayl222/social-security-claiming-simulator.git
   ```
2. **Navigate** to the project directory:
   ```bash
   cd social-security-claiming-simulator
   ```
3. (Optional) Create and activate a **virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS/Linux
   # or
   venv\Scripts\activate      # Windows
   ```
4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Streamlit App
1. Ensure you are in the main project directory:
   ```bash
   cd social-security-claiming-simulator
   ```
2. Run the Streamlit application:
   ```bash
   streamlit run src/streamlit_app.py
   ```
3. A local URL (typically `http://localhost:8501`) will appear in your terminal.  
4. Open that URL in your web browser to interact with the Social Security Claiming Simulator interface.

### Running the FastAPI App
1. Ensure you are in the main project directory:
   ```bash
   cd social-security-claiming-simulator
   ```
2. Run the FastAPI app using **Uvicorn**:
   ```bash
   uvicorn src.fastapi_app:app --reload
   ```
   - The `--reload` flag automatically restarts the server when file changes are detected.
3. Open the provided URL (typically `http://127.0.0.1:8000`) in your browser or use a REST client (e.g., Postman, cURL) to interact with the endpoints.
4. Visit `http://127.0.0.1:8000/docs` (by default) for the auto-generated Swagger UI and see the available endpoints.

---

## Usage
- **Streamlit App**:  
  1. Enter your details (current age, desired claiming age, projected COLA, etc.).  
  2. The app will calculate and display comparisons across different claiming strategies.  

- **FastAPI**:  
  1. Use the provided endpoints to submit parameters (e.g., current age, claiming age).  
  2. Receive JSON responses with computed benefit estimates and comparisons.  
  3. Integrate with your own frontend or scripts as needed.

- **Important**: The simulator is intended for educational use. Always consult with a qualified professional before making decisions regarding Social Security benefits.

---

## Developer Instructions

### Cloning the Repository
If you plan to modify or extend the simulator, clone the repo:
```bash
git clone https://github.com/jtayl222/social-security-claiming-simulator.git
cd social-security-claiming-simulator
```

### Running Locally
1. **Set up** a Python 3 environment (using `venv` or `conda` is recommended).
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the desired application**:
   - **Streamlit**:
     ```bash
     streamlit run src/streamlit_app.py
     ```
   - **FastAPI**:
     ```bash
     uvicorn src.fastapi_app:app --reload
     ```

---

## Contributing
1. **Fork** the repository on GitHub.  
2. **Create** a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature/my-new-feature
   ```
3. **Commit** your changes:
   ```bash
   git commit -am "Add new feature"
   ```
4. **Push** to your branch:
   ```bash
   git push origin feature/my-new-feature
   ```
5. Open a **Pull Request** on GitHub. We appreciate all contributions, whether it’s documentation improvements, bug fixes, or new functionality.

---

## Disclaimer
This project is **not** legal, financial, or tax advice. It is purely for informational and educational purposes. The estimations and projections generated by this tool may not reflect real-world outcomes. **Always consult a qualified professional** to discuss how Social Security claiming decisions affect your unique circumstances.

---

Thank you for using the **Social Security Claiming Simulator**! If you have any suggestions or encounter any issues, please open an [issue](https://github.com/jtayl222/social-security-claiming-simulator/issues) or submit a pull request.