FROM python:3.12

WORKDIR /effective-mobile-tests

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y --no-install-recommends \
  ca-certificates fonts-liberation libnss3 libdbus-1-3 libasound2t64 \
  libatk1.0-0t64 libatk-bridge2.0-0t64 libxdamage1 libnspr4 libatspi2.0-0t64 \
  libxfixes3 libgbm1 libxkbcommon0 libxrandr2 libxcomposite1 \
  && rm -rf /var/lib/apt/lists/*

RUN python -m playwright install-deps
RUN python -m playwright install chromium

COPY . .

CMD ["python", "-m", "pytest", "-q", "--alluredir=./allure-results"]