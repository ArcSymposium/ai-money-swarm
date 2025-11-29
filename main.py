from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import subprocess, os

app = FastAPI()
templates = Jinja2Templates(directory=".")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.get_template("index.html").render({"request": request})

@app.post("/summarize")
async def summarize(url: str = Form(...)):
    result = subprocess.run(
        ["python3", "app.py", url],
        capture_output=True, text=True, cwd="."
    )
    summary = result.stdout.decode()
    return HTMLResponse(f"""
    <pre style="font-size:18px; padding:30px">{summary}</pre>
    <br><a href="/">← Another video</a>
    """)

# Simple landing page (your agent already wrote the summarizer — we just wrap it)
with open("index.html","w") as f:
    f.write("""
    <html><body style="font-family:sans-serif; max-width:700px; margin:auto; padding:40px">
    <h1>YouTube → Newsletter in 8 Seconds</h1>
    <form method=post action="/summarize">
      <input name=url placeholder="https://youtube.com/watch?v=..." style="width:100%; padding:15px; font-size:18px"><br><br>
      <button style="padding:15px 30px; font-size:18px">Create Newsletter →</button>
    </form>
    <p><small>$29/month · cancel anytime · powered by your Chromebook</small></p>
    </body></html>
    """)
