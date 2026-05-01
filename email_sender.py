import os
import smtplib
from datetime import date
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv

from quotes import get_random_quote

load_dotenv()

RECIPIENT = "deem.jhae@gmail.com"
SUBJECT = "Daily Quote"


def build_html(quote: dict) -> str:
    today = date.today().strftime("%B %d, %Y")
    theme_label = quote["theme"].replace("-", " ").title()
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <style>
    body {{ font-family: Georgia, serif; background: #f9f7f4; margin: 0; padding: 0; }}
    .container {{ max-width: 560px; margin: 48px auto; background: #fff;
                  border-radius: 12px; padding: 40px 48px;
                  box-shadow: 0 2px 12px rgba(0,0,0,.08); }}
    .date {{ font-size: 13px; color: #999; letter-spacing: .05em; margin-bottom: 32px; }}
    .quote {{ font-size: 22px; line-height: 1.6; color: #2d2d2d;
              border-left: 4px solid #6c63ff; padding-left: 20px; margin: 0 0 24px; }}
    .author {{ font-size: 15px; color: #555; font-style: italic; }}
    .theme {{ display: inline-block; margin-top: 28px; font-size: 12px;
              background: #f0eeff; color: #6c63ff; padding: 4px 12px;
              border-radius: 20px; letter-spacing: .04em; }}
    .footer {{ margin-top: 40px; font-size: 12px; color: #bbb; text-align: center; }}
  </style>
</head>
<body>
  <div class="container">
    <div class="date">{today}</div>
    <blockquote class="quote">"{quote['text']}"</blockquote>
    <div class="author">— {quote['author']}</div>
    <div class="theme">{theme_label}</div>
    <div class="footer">Your daily dose of inspiration · MisakiDate</div>
  </div>
</body>
</html>"""


def build_plain(quote: dict) -> str:
    today = date.today().strftime("%B %d, %Y")
    return (
        f"Daily Quote — {today}\n\n"
        f'"{quote["text"]}"\n\n'
        f"— {quote['author']}\n\n"
        f"Theme: {quote['theme']}\n"
    )


def send_daily_quote() -> None:
    smtp_user = os.environ["GMAIL_USER"]
    smtp_password = os.environ["GMAIL_APP_PASSWORD"]

    quote = get_random_quote()

    msg = MIMEMultipart("alternative")
    msg["Subject"] = SUBJECT
    msg["From"] = smtp_user
    msg["To"] = RECIPIENT

    msg.attach(MIMEText(build_plain(quote), "plain"))
    msg.attach(MIMEText(build_html(quote), "html"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(smtp_user, smtp_password)
        server.sendmail(smtp_user, RECIPIENT, msg.as_string())

    print(f"Sent: \"{quote['text'][:60]}...\" — {quote['author']}")


if __name__ == "__main__":
    send_daily_quote()
