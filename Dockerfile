FROM python:3.10
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8080
ENV PORT=8080
ENV GEMINI_API_KEY="key"
CMD python -m gunicorn --bind 0.0.0.0:$PORT "app:create_app()" --log-level debug