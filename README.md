
# Web Automation Framework (Python + Playwright + Pytest)

This repository contains an automation framework for testing using:

- **Python**
- **Playwright (Sync API)**
- **Pytest**
- **Allure Report**
- **HTML Pytest Report**

The tests run support **headless/headed execution**

---

## 1. Clone the Repository

```bash
git clone https://github.com/SStepanoFF/python_playwright_nxlog.git
```

---

## 2. Installation

### 2.1 Install Python (3.12+ recommended)

Download from: https://www.python.org/downloads/  

---

### 2.2 Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate         # macOS/Linux
# .venv\Scripts\activate        # Windows
```

---

### 2.3 Install project dependencies

```bash
pip install poetry

poetry install
```

---

### 2.4 Install Playwright Browsers

```bash
poetry run playwright install
```

---

### 2.5 Install Allure

#### macOS:

```bash
brew install allure
```

#### Windows:

Download from: https://github.com/allure-framework/allure2/releases

Validate installation:

```bash
allure --version
```

---

### 2.6 Install Pytest-HTML

```bash
pip install pytest-html
```

---

## 3. Test Execution

```bash
pytest
```

### Override configs

Run in headed mode:

```bash
pytest --headless=false
```

---

## 4. Generate Allure Report

```bash
allure serve allure-results
```

Or generate static report:

```bash
allure generate allure-results -o allure-report --clean
allure open allure-report
```

# Framework Highlights

- Playwright Sync API  
- Page Object Model architecture  
- Pytest fixtures & config  
- Allure reporting  
- HTML reporting  
- Automatic screenshots  
- Supports headless/headed execution  
