from libqtile import bar, widget
from libqtile.command import lazy
import subprocess

# Define a dictionary to map each country to its code
country_codes = {
    "United States": "us",
    "United Kingdom": "uk",
    "Canada": "ca",
    "Netherlands": "nl",
    "Sweden": "se",
    "Switzerland": "ch"
}

class NordVPN(widget.TextBox):
    def __init__(self, **config):
        super().__init__("NordVPN", **config)
        self.add_callbacks({'Button1': self.connect_vpn})

    def connect_vpn(self, qtile):
        country = "United States"  # you can change this to select a different country
        code = country_codes[country]
        try:
            subprocess.run(["nordvpn", "connect", code])
        except Exception as e:
            self.text = "NordVPN: error"
            qtile.current_screen.bar.draw()
            print(f"An error occurred: {str(e)}")

    def update(self, text):
        self.text = text
        self.bar.draw()

    def timer_setup(self):
        self.timeout_add(self.update_interval, self.poll)

    def poll(self):
        try:
            result = subprocess.run(["nordvpn", "status"], stdout=subprocess.PIPE)
            status = result.stdout.decode().split('\n')[0]
            self.update("NordVPN: " + status)
        except Exception as e:
            self.update("NordVPN: error")
            print(f"An error occurred: {str(e)}")
        self.timer_setup()

