from bottle import route, run, response
from gpiozero import LED, Button

# ======================
# GPIO SETUP
# ======================
leds = [LED(18), LED(23), LED(24)]
switch = Button(25)

def switch_status():
    return 'Down' if switch.is_pressed else 'Up'

def led_status():
    return [int(led.value) for led in leds]

# ======================
# MAIN PAGE
# ======================
@route('/')
def index():

    html = f"""
    <html>
    <head>
        <title>GPIO Control Panel</title>
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

            .btn {{
                display: inline-block;
                padding: 15px 25px;
                margin: 10px;
                border-radius: 12px;
                background: #444;
                color: white;
                font-weight: bold;
                cursor: pointer;
                user-select: none;
                -webkit-tap-highlight-color: transparent;
            }}

            .on {{
                background: #00ff88 !important;
                color: black;
            }}

            .off {{
                background: #444;
            }}

            .btn:active {{
                transform: scale(0.95);
            }}
        </style>

        <script>
            // LED toggle
            function toggleLED(id) {{
                fetch('/toggle/' + id)
                .then(() => updateLED());
            }}

            // UPDATE LED STATUS
            function updateLED() {{
                fetch('/led_status')
                .then(r => r.json())
                .then(data => {{
                    data.forEach((v, i) => {{
                        let el = document.getElementById("led"+i);
                        if (v == 1) {{
                            el.classList.add("on");
                            el.classList.remove("off");
                        }} else {{
                            el.classList.add("off");
                            el.classList.remove("on");
                        }}
                    }});
                }});
            }}

            // REAL-TIME PUSHBUTTON (FIX UTAMA)
            function updateButton() {{
                fetch('/status')
                .then(r => r.text())
                .then(data => {{
                    document.getElementById("btn-status").innerText = data;
                }});
            }}

            setInterval(updateButton, 200);  // REAL-TIME
            setInterval(updateLED, 300);

            window.onload = () => {{
                updateLED();
                updateButton();
            }};
        </script>
    </head>

    <body>
        <div class="container">
            <h1>GPIO CONTROL PANEL</h1>

            <div class="card">
                Push Button Status: <b id="btn-status">{switch_status()}</b>
            </div>

            <div class="card">
                <h2>LED CONTROL</h2>

                <div>
                    <div id="led0" class="btn off" onclick="toggleLED(0)">LED 0</div>
                    <div id="led1" class="btn off" onclick="toggleLED(1)">LED 1</div>
                    <div id="led2" class="btn off" onclick="toggleLED(2)">LED 2</div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """

    return html

# ======================
# TOGGLE LED
# ======================
@route('/toggle/<led_id:int>')
def toggle_led(led_id):
    try:
        leds[led_id].toggle()
    except:
        pass
    return "OK"

# ======================
# PUSHBUTTON STATUS
# ======================
@route('/status')
def status():
    response.content_type = 'text/plain'
    return switch_status()

# ======================
# LED STATUS
# ======================
@route('/led_status')
def led_status_api():
    response.content_type = 'application/json'
    return str(led_status())

# ======================
# RUN SERVER
# ======================
run(host='0.0.0.0', port=8000)