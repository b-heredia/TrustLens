from flask import Flask, render_template, request
from analyzer import analyze_url
from urllib.parse import urlparse

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    submitted_url = None
    analysis_result = None
    warning_count = 0
    risk_summary = None
    error_message = None

    if request.method == "POST":

        submitted_url = request.form.get("url", "").strip()

        try:
            parsed_url = urlparse(submitted_url)
            hostname = parsed_url.hostname

        except ValueError:
            hostname = None
            parsed_url = None

        if (
            parsed_url is None
            or any(char.isspace() for char in submitted_url)
            or parsed_url.scheme not in ["http", "https"]
            or not hostname
        ):
            error_message = "Please enter a valid URL starting with http:// or https://."

        else:
            analysis_result = analyze_url(submitted_url)

            warning_count = sum(
                1 for result in analysis_result
                if result.startswith("Warning:")
            )

            if warning_count == 0:
                risk_summary = "No predefined warning indicators detected."
            elif warning_count <= 2:
                risk_summary = (
                    "Some warning indicators detected. "
                    "Review the findings before proceeding."
                )
            else:
                risk_summary = (
                    "Several warning indicators detected. "
                    "Exercise caution and verify the destination."
                )

    return render_template(
        "index.html",
        submitted_url=submitted_url,
        analysis_result=analysis_result,
        warning_count=warning_count,
        risk_summary=risk_summary,
        error_message=error_message
    )


if __name__ == "__main__":
    app.run(debug=False)