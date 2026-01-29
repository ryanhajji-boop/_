from flask import Flask, request, render_template, redirect, url_for
from pathlib import Path
from datetime import date, datetime

app = Flask(__name__)

DATA_PATH = Path(__file__).parent / "comments.txt"


def normalize_birthday(y: int, m: int, d: int) -> date:
    """
    Handles invalid dates such as Feb 29 on non-leap years
    by falling back to Feb 28.
    """
    try:
        return date(y, m, d)
    except ValueError:
        if m == 2 and d == 29:
            return date(y, 2, 28)
        raise


def calculate_birthday_stats(person_name: str, birth_date: date) -> dict:
    today = date.today()

    this_year = normalize_birthday(today.year, birth_date.month, birth_date.day)
    next_year = normalize_birthday(today.year + 1, birth_date.month, birth_date.day)

    upcoming = this_year if this_year >= today else next_year
    days_remaining = (upcoming - today).days
    upcoming_age = upcoming.year - birth_date.year

    display_fmt = "%d/%m/%Y"

    return {
        "name": person_name.strip() or "person",
        "dob": birth_date.strftime(display_fmt),
        "today": today.strftime(display_fmt),
        "next_birthday": upcoming.strftime(display_fmt),
        "days_to_birthday": days_remaining,
        "age_at_next_birthday": upcoming_age,
    }


@app.route("/birthday", methods=["GET", "POST"])
def birthday_page():
    if request.method == "GET":
        return render_template(
            "birthday_form.html",
            info=None,
            name="",
            dob=""
        )

    name_input = request.form.get("name", "")
    dob_input = request.form.get("dob", "")

    if not dob_input:
        return "Date of birth is required.", 400

    try:
        parsed_dob = date.fromisoformat(dob_input)
    except ValueError:
        return "Invalid date supplied.", 400

    details = calculate_birthday_stats(name_input, parsed_dob)

    return render_template(
        "birthday_form.html",
        info=details,
        name=name_input,
        dob=dob_input
    )


@app.route("/ping-template")
def template_test():
    return render_template(
        "birthday_form.html",
        info=None,
        name="Henry",
        dob=""
    )


def load_comments() -> list[str]:
    if not DATA_PATH.exists():
        return []
    return DATA_PATH.read_text(encoding="utf-8").splitlines()


def save_comment(author: str, message: str) -> None:
    author = (author or "").strip()
    message = (message or "").strip()

    if not message:
        return

    timestamp = datetime.now().isoformat(timespec="seconds")
    author_label = author if author else "Anonymous"

    entry = f"[{timestamp}] {author_label}: {message}"

    with DATA_PATH.open("a", encoding="utf-8") as file:
        file.write(entry + "\n")


@app.route("/comments", methods=["GET", "POST"])
def comments_page():
    if request.method == "POST":
        save_comment(
            request.form.get("name", ""),
            request.form.get("comment", "")
        )
        return redirect(url_for("comments_page"))

    return render_template(
        "comments.html",
        entries=load_comments()
    )


@app.route("/")
def home():
    return "sup add /birthday to the url to see the final thing"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8989)
