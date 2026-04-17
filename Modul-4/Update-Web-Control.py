from bottle import route, run, response
from gpiozero import LED, Button

# ======================
# GPIO SETUP
# ======================
leds = [LED(18), LED(23), LED(24)]
switch = Button(25)

# ======================
# STATUS PUSH BUTTON
# ======================
def switch_status():
    return 'Down' if switch.is_pressed else 'Up'

# ======================
# LED HTML BUTTON
# ======================
def html_for_led(i):
    return f"""
    <button class="led-btn" onclick="toggleLED({i})">
        LED {i}
    </button>
    """

# ======================
# MAIN PAGE
# ======================
@route('/')
def index():

    response_html = f"""
    <html>
    <head>
        <title>GPIO Control</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <style>
            body {{
                margin: 0;
                font-family: Arial;
                background: linear-gradient(135deg, #1e3c72, #2a5298);
                color: white;
                text-align: center;
            }}

            .container {{
                padding: 20px;
            }}

            .card {{
                background: rgba(255,255,255,0.1);
                padding: 20px;
                margin-top: 20px;
                border-radius: 15px;
            }}

            .led-btn {{
                padding: 15px 25px;
                margin: 10px;
                border: none;
                border-radius: 12px;
                cursor: pointer;
                font-size: 16px;
                background: #00c6ff;
                color: black;
                font-weight: bold;
                transition: 0.2s;
                -webkit-tap-highlight-color: transparent;
            }}

            .led-btn:active {{
                transform: scale(0.95);
            }}
        </style>

        <script>
            function toggleLED(id) {{
                fetch('/toggle/' + id)
                .then(() => console.log("LED toggled"));
            }}

            function updateStatus() {{
                fetch('/status')
                .then(r => r.text())
                .then(data => {{
                    document.getElementById("btn-status").innerText = data;
                }});
            }}

            setInterval(updateStatus, 200);
        </script>
    </head>

    <body>
        <div class="container">
            <h1>GPIO CONTROL</h1>

            <div class="card">
                Push Button Status: <b id="btn-status">{switch_status()}</b>
            </div>

            <div class="card">
                <h2>LED CONTROL</h2>

                {html_for_led(0)}
                {html_for_led(1)}
                {html_for_led(2)}
            </div>
        </div>
    </body>
    </html>
    """

    return response_html

# ======================
# TOGGLE LED
# ======================
@route('/toggle/<led_id:int>')
def toggle_led(led_id):
    try:
        leds[led_id].toggle()
        return "OK"
    except:
        return "ERROR"

# ======================
# PUSH BUTTON STATUS
# ======================
@route('/status')
def status():
    response.content_type = 'text/plain'
    return switch_status()

# ======================
# RUN SERVER
# ======================
run(host='0.0.0.0', port=8000)
