FROM python:3.10
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV GEMINI_API_KEY="key"
CMD ["python", "-m", "flask", "--app", "app", "run", "--host", "0.0.0.0", "--port", "$PORT"]