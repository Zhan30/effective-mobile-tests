FROM python:3.11-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
  ca-certificates fonts-liberation libnss3 libxss1 libasound2 \
  libatk1.0-0 libatk-bridge2.0-0 libcups2 libdbus-1-3 libx11-xcb1 \
  libxcb-dri3-0 libgbm1 libxkbcommon0 xdg-utils \
  && rm -rf /var/lib/apt/lists/*

RUN python -m playwright install chromium

WORKDIR /effective-mobile-tests

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "-m", "pytest", "-q", "--alluredir=./allure-results"]