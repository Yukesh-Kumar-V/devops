from flask import Flask, request, redirect, url_for

app = Flask(__name__)

html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Web Calculator</title>
    <style>
        body {{ font-family: Arial; display: flex; justify-content: center; margin-top: 50px; }}
        .calculator {{ width: 320px; }}
        input[type="text"] {{ width: 100%; height: 60px; font-size: 24px; text-align: right; padding: 10px; }}
        .buttons {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; margin-top: 10px; }}
        button {{ height: 60px; font-size: 20px; }}
    </style>
</head>
<body>
    <form class="calculator" method="post">
        <input type="text" name="expression" value="{expression}" readonly>
        <input type="text" value="{result}" readonly>
        <div class="buttons">
            {buttons_html}
        </div>
    </form>
</body>
</html>
"""

# Buttons layout
button_rows = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]

@app.route("/", methods=["GET", "POST"])
def calculator():
    expression = ""
    result = ""
    if request.method == "POST":
        expression = request.form.get("expression", "")
        btn = request.form.get("btn")
        if btn == "C":
            expression = ""
        elif btn == "=":
            try:
                result = str(eval(expression))
            except:
                result = "Error"
        else:
            expression += btn

    buttons_html = ""
    for row in button_rows:
        for btn in row:
            buttons_html += f"""
                <button type="submit" name="btn" value="{btn}">{btn}</button>
            """
    return html_template.format(expression=expression, result=result, buttons_html=buttons_html)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
