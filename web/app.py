from fastapi import FastAPI, HTTPException

from backend.email_template import render_message
from backend.excel_service import load_recipients

app = FastAPI(title="Store Communications Suite", version="portfolio")

@app.get("/api/health")
def health():
    return {"ok": True, "portfolio": True}

@app.post("/api/preview")
def preview(payload: dict):
    try:
        recipients = load_recipients(payload["spreadsheet"])
        title = str(payload.get("title") or "Operational update")
        body = str(payload.get("body") or "")
    except (KeyError, ValueError, OSError) as exc:
        raise HTTPException(status_code=422, detail=str(exc))

    items = []
    for recipient in recipients[:100]:
        subject, html = render_message(recipient, title, body)
        items.append({
            "store_code": recipient.store_code,
            "store_name": recipient.store_name,
            "email": recipient.email,
            "subject": subject,
            "html": html,
        })
    return {"count": len(items), "items": items}
