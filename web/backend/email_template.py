from __future__ import annotations

from html import escape
from .models import Recipient

def render_message(recipient: Recipient, title: str, body: str) -> tuple[str, str]:
    subject = f"{title} · {recipient.store_name}".strip(" ·")
    html = f"""
    <div style="font-family:Arial,sans-serif;line-height:1.55;color:#182230">
      <p>Olá, equipe da <strong>{escape(recipient.store_name)}</strong>.</p>
      <div>{escape(body).replace(chr(10), '<br>')}</div>
      <p style="color:#667085;font-size:12px">Mensagem preparada por um fluxo operacional automatizado.</p>
    </div>
    """
    return subject, html
