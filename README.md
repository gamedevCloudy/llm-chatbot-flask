# Kris: Geeta Scholar Chatbot

Kris is a chatbot that uses Gemini 1.5 flash as its model.
He's a friendly bot designed to help you with your life problems with wisdom from Geeta.

![Screenshot](./chatbot_UI.png)

---

## Build and Run

1. Clone this repo

```bash
git clone https://github.com/gamedevCloudy/llm-chatbot-flask.git
```

2. Enter this project

```bash
cd llm-chatbot-flask
```

3. Building:

```bash
docker build -t geeta-gemini .
```

4. Running:

```bash
docker run -p 5100:5100 -e GEMINI_API_KEY="your_actual_key" geeta-gemini
```

Alternately you can run this through Docker Desktop.

1. In images find this image `geeta-gemini`
2. Click the run icon
3. In Additional settings, add environment variable `GEMINI_API_KEY`
4. Optionally name your container.

---

## Tools Used:

- Python
- Gemini API (https://aistudio.google.com/)
- HTMX (https://htmx.org)
- Flask (https://flask.palletsprojects.com/)
- PicoCSS (https://picocss.com)
- HTML
- Docker

---
