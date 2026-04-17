from bottle import route, run, redirect
from gpiozero import LED, Button

# Inisialisasi LED dan tombol
leds = [LED(18), LED(23), LED(24)]
switch = Button(25)

def switch_status():
    return 'Down' if switch.is_pressed else 'Up'

def html_for_led(led_number):
    return f"""
    <button class="led-btn" onclick="changed({led_number})">
        LED {led_number}
    </button>
    """

@route('/')
@route('/<led_number>')
def index(led_number="n"):
    
    # Toggle LED lalu balik ke halaman utama
    if led_number != "n":
        try:
            leds[int(led_number)].toggle()
        except (IndexError, ValueError):
            pass
        return redirect('/')  # ?? penting biar tidak toggle terus

    response = f"""
    <html>
    <head>
        <title>GPIO Control</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <style>
            body {{
                margin: 0;
                font-family: 'Segoe UI', sans-serif;
                background: linear-gradient(135deg, #1e3c72, #2a5298);
                color: white;
                text-align: center;
            }}

            .container {{
                padding: 20px;
            }}

            h1 {{
                margin-bottom: 5px;
            }}

            .card {{
                background: rgba(255,255,255,0.1);
                padding: 20px;
                border-radius: 15px;
                box-shadow: 0 8px 20px rgba(0,0,0,0.3);
                margin-top: 20px;
            }}

            .status {{
                font-size: 20px;
                margin: 10px 0;
            }}

            .led-container {{
                display: flex;
                justify-content: center;
                flex-wrap: wrap;
                gap: 15px;
                margin-top: 15px;
            }}

            .led-btn {{
                padding: 15px 25px;
                font-size: 18px;
                border: none;
                border-radius: 12px;
                cursor: pointer;
                background: #00c6ff;
                color: black;
                font-weight: bold;
                transition: all 0.3s ease;
            }}

            .led-btn:hover {{
                background: #0072ff;
                color: white;
                transform: scale(1.05);
            }}

            @media (max-width: 600px) {{
                .led-btn {{
                    width: 100%;
                }}
            }}
        </style>

        <script>
            function changed(led) {{
                window.location.href = '/' + led;
            }}
        </script>
    </head>

    <body>
        <div class="container">
            <h1>? GPIO Control</h1>

            <div class="card">
                <div class="status">
                    Button Status: <b>{switch_status()}</b>
                </div>
            </div>

            <div class="card">
                <h2>Control LED</h2>
                <div class="led-container">
                    {html_for_led(0)}
                    {html_for_led(1)}
                    {html_for_led(2)}
                </div>
            </div>
        </div>
    </body>
    </html>
    """

    return response

run(host='0.0.0.0', port=8000)
