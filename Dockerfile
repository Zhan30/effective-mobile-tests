FROM mcr.microsoft.com/playwright/python:latest

WORKDIR /effective-mobile-tests

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "-m", "pytest", "-q", "--alluredir=./allure-results"]