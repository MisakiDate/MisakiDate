import os
import smtplib
from datetime import date
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv

from quotes import get_random_item

load_dotenv()

RECIPIENT = "deem.jhae@gmail.com"
SUBJECT = "Daily Quote"

TONE_LABELS = {
    "warm": "Warm reminder",
    "sharp": "No-nonsense",
    "both": "Warm & sharp",
}

THEME_COLORS = {
    "finishing":                "#e63946",
    "hard work":                "#f4a261",
    "resilience":               "#2a9d8f",
    "self-doubt":               "#6c63ff",
    "intellectual perseverance":"#457b9d",
}


def _accent(item: dict) -> str:
    return THEME_COLORS.get(item["theme"], "#6c63ff")


def build_html(item: dict) -> str:
    today = date.today().strftime("%B %d, %Y")
    accent = _accent(item)
    tone_label = TONE_LABELS.get(item["tone"], item["tone"])
    theme_label = item["theme"].title()

    if item["type"] == "story":
        content_block = f"""
        <p style="font-size:13px;color:#888;letter-spacing:.06em;text-transform:uppercase;
                  margin:0 0 14px;">Today's Story</p>
        <p style="font-size:17px;line-height:1.75;color:#2d2d2d;margin:0 0 20px;">
          {item['text']}
        </p>
        <p style="font-size:14px;color:#555;font-style:italic;margin:0;">
          — {item['author']}
        </p>"""
    else:
        content_block = f"""
        <p style="font-size:13px;color:#888;letter-spacing:.06em;text-transform:uppercase;
                  margin:0 0 14px;">Today's Quote</p>
        <blockquote style="font-size:21px;line-height:1.6;color:#2d2d2d;
                            border-left:4px solid {accent};padding-left:20px;margin:0 0 20px;">
          "{item['text']}"
        </blockquote>
        <p style="font-size:14px;color:#555;font-style:italic;margin:0;">
          — {item['author']}
        </p>"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <style>
    body {{ margin:0; padding:0; background:#f4f1ee; font-family:Georgia,serif; }}
  </style>
</head>
<body>
  <table width="100%" cellpadding="0" cellspacing="0" style="background:#f4f1ee;padding:40px 0;">
    <tr><td align="center">
      <table width="560" cellpadding="0" cellspacing="0"
             style="background:#fff;border-radius:12px;overflow:hidden;
                    box-shadow:0 2px 16px rgba(0,0,0,.08);">

        <!-- header bar -->
        <tr>
          <td style="background:{accent};padding:6px 0;"></td>
        </tr>

        <!-- body -->
        <tr>
          <td style="padding:36px 44px 28px;">
            <p style="font-size:12px;color:#aaa;letter-spacing:.05em;margin:0 0 28px;">
              {today}
            </p>
            {content_block}
          </td>
        </tr>

        <!-- tags -->
        <tr>
          <td style="padding:0 44px 32px;">
            <span style="display:inline-block;font-size:11px;background:{accent}18;
                         color:{accent};padding:4px 12px;border-radius:20px;
                         margin-right:6px;letter-spacing:.04em;">{theme_label}</span>
            <span style="display:inline-block;font-size:11px;background:#f0f0f0;
                         color:#888;padding:4px 12px;border-radius:20px;
                         letter-spacing:.04em;">{tone_label}</span>
          </td>
        </tr>

        <!-- footer -->
        <tr>
          <td style="border-top:1px solid #f0eded;padding:16px 44px;
                     font-size:11px;color:#ccc;text-align:center;">
            Your daily PhD fuel &nbsp;·&nbsp; MisakiDate
          </td>
        </tr>

      </table>
    </td></tr>
  </table>
</body>
</html>"""


def build_plain(item: dict) -> str:
    today = date.today().strftime("%B %d, %Y")
    label = "Story" if item["type"] == "story" else "Quote"
    return (
        f"Daily {label} — {today}\n\n"
        f"{item['text']}\n\n"
        f"— {item['author']}\n\n"
        f"Theme: {item['theme']}  |  Tone: {item['tone']}\n"
    )


def send_daily_quote() -> None:
    smtp_user = os.environ["GMAIL_USER"]
    smtp_password = os.environ["GMAIL_APP_PASSWORD"]

    item = get_random_item()

    msg = MIMEMultipart("alternative")
    msg["Subject"] = SUBJECT
    msg["From"] = smtp_user
    msg["To"] = RECIPIENT

    msg.attach(MIMEText(build_plain(item), "plain"))
    msg.attach(MIMEText(build_html(item), "html"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(smtp_user, smtp_password)
        server.sendmail(smtp_user, RECIPIENT, msg.as_string())

    snippet = item["text"][:60]
    print(f'Sent [{item["type"]}]: "{snippet}..." — {item["author"]}')


if __name__ == "__main__":
    send_daily_quote()
