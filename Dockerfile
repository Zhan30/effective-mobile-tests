FROM python:3.11-slim

WORKDIR /effective-mobile-tests

RUN apt-get update && apt-get install -y \
    ca-certificates fonts-liberation libnss3 libxss1 libasound2 \
    libatk1.0-0 libatk-bridge2.0-0 libcups2 libdbus-1-3 libx11-xcb1 \
    libxcomposite1 libxdamage1 libgbm1 libxrandr2 xdg-utils

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python -m playwright install chromium

CMD ["python", "-m", "pytest", "-q", "--alluredir=./allure-results"]