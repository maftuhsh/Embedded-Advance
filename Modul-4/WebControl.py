from bottle import route, run
from gpiozero import LED, Button

# Inisialisasi LED dan tombol
leds = [LED(18), LED(23), LED(24)]
switch = Button(25)

# Status tombol
def switch_status():
    return 'Down' if switch.is_pressed else 'Up'

# HTML button untuk tiap LED
def html_for_led(led_number):
    return f"<input type='button' onClick='changed({led_number})' value='LED {led_number}'/>"

# Routing utama
@route('/')
@route('/<led_number>')
def index(led_number="n"):
    
    # Toggle LED jika ada input dari URL
    if led_number != "n":
        try:
            leds[int(led_number)].toggle()
        except (IndexError, ValueError):
            pass

    # Template HTML
    response = f"""
    <html>
    <head>
        <title>GPIO Control</title>
        <script>
            function changed(led) {{
                window.location.href = '/' + led;
            }}
        </script>
    </head>
    <body>
        <h1>PRAKTIKUM EMBEDDED LANJUT 2025</h1>
        <h2>Button = {switch_status()}</h2>
        <h2>LEDs</h2>
        {html_for_led(0)}
        {html_for_led(1)}
        {html_for_led(2)}
    </body>
    </html>
    """

    return response

# Jalankan server
run(host='10.10.13.184', port=8000)
