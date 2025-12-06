
# Web Automation Framework (Python + Playwright + Pytest)

This repository contains an automation framework for testing **Twitch mobile UI** using:

- **Python**
- **Playwright (Sync API)**
- **Pytest**
- **Allure Report**
- **HTML Pytest Report**

The tests run in **Chrome Mobile Emulation Mode**, support **headless/headed execution**, and follow the **Page Object Model (POM)**.

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

Use different mobile device:

```bash
pytest --mobile-device="iPhone 12"
```

Run a specific test:

```bash
pytest tests/test_mobile.py -v
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

## 5. API Test Cases
 ID | Test Name | Description | Endpoint | Steps | Expected Result |
|----|-----------|-------------|----------|--------|------------------|
| TC-API-01 | Get Image By ID | Verify that an existing image can be retrieved by its ID | `/images/{id}` | 1. Call `/images/search` to obtain an existing ID.<br>2. Call `/images/{id}` with this ID. | • Status code 200<br>• Returned ID matches<br>• URL valid<br>• Width/height > 0<br>• Breeds validated if present |
| TC-API-02 | Get Image With Wrong ID | Validate error handling when ID is invalid | `/images/{id}` | 1. Send request with invalid ID. | • Status code 400<br>• Correct error message |
| TC-API-03 | Search Images With Limit | Validate the `limit` parameter is respected | `/images/search` | 1. Request with `limit=1`.<br>2. Request with `limit=10`. | • Status code 200<br>• Number of items equals limit<br>• Basic DTO fields valid |
| TC-API-04 | Search Images With Breed Filter | Validate breed filtering via `has_breeds` | `/images/search` | 1. Request with `has_breeds=1`.<br>2. Request with `has_breeds=0`. | • Correct breed presence/absence<br>• Status code 200 |


## 5.1 Validation Summary

**Status codes** validate correct API behavior.

**DTO validation** ensures correct structure and ignores unknown fields.

**Field validation** (id, url, width, height) ensures integrity of returned objects.

**Filtering validation** checks that limit and has_breeds parameters produce correct results.

**Parametrized tests** increase coverage without test duplication.

---


---

# Framework Highlights

- Playwright Sync API  
- Mobile browser emulation (Chrome)  
- Page Object Model architecture  
- Pytest fixtures & config  
- Allure reporting  
- HTML reporting  
- Automatic screenshots  
- Supports headless/headed execution  
