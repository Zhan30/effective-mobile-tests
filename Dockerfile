FROM python:3.12

WORKDIR /effective-mobile-tests

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN python -m playwright install chromium

COPY . .

CMD ["python", "-m", "pytest", "-q", "--alluredir=./allure-results"]