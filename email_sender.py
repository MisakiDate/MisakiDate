import os
import random
import smtplib
from datetime import date
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv

from quotes import ITEMS

load_dotenv()

RECIPIENT = "deem.jhae@gmail.com"
SUBJECT = "Daily Quote"

TONE_LABELS = {
    "warm": "Warm reminder",
    "sharp": "No-nonsense",
    "both": "Warm & sharp",
}

THEME_COLORS = {
    "finishing":                 "#e63946",
    "hard work":                 "#f4a261",
    "resilience":                "#2a9d8f",
    "self-doubt":                "#6c63ff",
    "intellectual perseverance": "#457b9d",
}

_DEFAULT_ACCENT = "#6c63ff"


def _accent(item: dict) -> str:
    return THEME_COLORS.get(item["theme"], _DEFAULT_ACCENT)


def _pick_daily() -> tuple[list[dict], dict]:
    quotes = [i for i in ITEMS if i["type"] == "quote"]
    stories = [i for i in ITEMS if i["type"] == "story"]
    daily_quotes = random.sample(quotes, min(5, len(quotes)))
    daily_story = random.choice(stories)
    return daily_quotes, daily_story


# ── HTML helpers ─────────────────────────────────────────────────────────────

def _quote_row(item: dict, index: int) -> str:
    accent = _accent(item)
    tone_label = TONE_LABELS.get(item["tone"], item["tone"])
    theme_label = item["theme"].title()
    return f"""
      <tr>
        <td style="padding:0 0 24px;">
          <table width="100%" cellpadding="0" cellspacing="0">
            <tr>
              <td style="border-left:3px solid {accent};padding:2px 0 2px 16px;">
                <p style="font-size:18px;line-height:1.6;color:#2d2d2d;margin:0 0 8px;">
                  "{item['text']}"
                </p>
                <p style="font-size:13px;color:#777;font-style:italic;margin:0 0 8px;">
                  — {item['author']}
                </p>
                <span style="display:inline-block;font-size:10px;background:{accent}18;
                             color:{accent};padding:3px 10px;border-radius:20px;
                             margin-right:4px;letter-spacing:.04em;">{theme_label}</span>
                <span style="display:inline-block;font-size:10px;background:#f0f0f0;
                             color:#999;padding:3px 10px;border-radius:20px;
                             letter-spacing:.04em;">{tone_label}</span>
              </td>
            </tr>
          </table>
        </td>
      </tr>"""


def _story_block(item: dict) -> str:
    accent = _accent(item)
    theme_label = item["theme"].title()
    return f"""
        <!-- Story section header -->
        <tr>
          <td style="padding:32px 44px 0;">
            <table width="100%" cellpadding="0" cellspacing="0">
              <tr>
                <td style="border-top:1px solid #ede9e4;padding-top:28px;">
                  <p style="font-size:11px;color:#aaa;letter-spacing:.1em;
                             text-transform:uppercase;margin:0 0 20px;">
                    Today's Story
                  </p>
                </td>
              </tr>
              <tr>
                <td style="background:#faf8f5;border-radius:8px;padding:24px 28px;">
                  <p style="font-size:16px;line-height:1.8;color:#2d2d2d;margin:0 0 16px;">
                    {item['text']}
                  </p>
                  <p style="font-size:13px;color:#777;font-style:italic;margin:0 0 12px;">
                    — {item['author']}
                  </p>
                  <span style="display:inline-block;font-size:10px;background:{accent}18;
                               color:{accent};padding:3px 10px;border-radius:20px;
                               letter-spacing:.04em;">{theme_label}</span>
                </td>
              </tr>
            </table>
          </td>
        </tr>"""


def build_html(quotes: list[dict], story: dict) -> str:
    today = date.today().strftime("%B %d, %Y")
    quote_rows = "".join(_quote_row(q, i + 1) for i, q in enumerate(quotes))

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <style>body{{margin:0;padding:0;background:#f4f1ee;font-family:Georgia,serif;}}</style>
</head>
<body>
  <table width="100%" cellpadding="0" cellspacing="0" style="background:#f4f1ee;padding:40px 0;">
    <tr><td align="center">
      <table width="580" cellpadding="0" cellspacing="0"
             style="background:#fff;border-radius:12px;overflow:hidden;
                    box-shadow:0 2px 16px rgba(0,0,0,.08);">

        <!-- top accent bar -->
        <tr><td style="background:#2d2d2d;padding:5px 0;"></td></tr>

        <!-- date + section header -->
        <tr>
          <td style="padding:32px 44px 24px;">
            <p style="font-size:12px;color:#aaa;letter-spacing:.05em;margin:0 0 20px;">{today}</p>
            <p style="font-size:11px;color:#aaa;letter-spacing:.1em;
                       text-transform:uppercase;margin:0 0 20px;">
              Today's Quotes
            </p>
            <table width="100%" cellpadding="0" cellspacing="0">
              {quote_rows}
            </table>
          </td>
        </tr>

        {_story_block(story)}

        <!-- footer -->
        <tr>
          <td style="padding:24px 44px;border-top:1px solid #f0eded;margin-top:24px;
                     font-size:11px;color:#ccc;text-align:center;">
            Your daily PhD fuel &nbsp;·&nbsp; MisakiDate
          </td>
        </tr>

      </table>
    </td></tr>
  </table>
</body>
</html>"""


def build_plain(quotes: list[dict], story: dict) -> str:
    today = date.today().strftime("%B %d, %Y")
    lines = [f"Daily Quote — {today}", "", "── TODAY'S QUOTES ──────────────────", ""]
    for i, q in enumerate(quotes, 1):
        lines += [f'{i}. "{q["text"]}"', f'   — {q["author"]}', ""]
    lines += ["── TODAY'S STORY ───────────────────", "", story["text"], "", f'— {story["author"]}', ""]
    return "\n".join(lines)


def send_daily_quote() -> None:
    smtp_user = os.environ["GMAIL_USER"]
    smtp_password = os.environ["GMAIL_APP_PASSWORD"]

    quotes, story = _pick_daily()

    msg = MIMEMultipart("alternative")
    msg["Subject"] = SUBJECT
    msg["From"] = smtp_user
    msg["To"] = RECIPIENT

    msg.attach(MIMEText(build_plain(quotes, story), "plain"))
    msg.attach(MIMEText(build_html(quotes, story), "html"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(smtp_user, smtp_password)
        server.sendmail(smtp_user, RECIPIENT, msg.as_string())

    print(f"Sent: {len(quotes)} quotes + 1 story — {story['author']}")


if __name__ == "__main__":
    send_daily_quote()
