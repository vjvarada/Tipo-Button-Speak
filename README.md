# Raspberry Pi Zero Button Speak

This project allows you to use a Raspberry Pi Zero to detect button presses and play corresponding audio phrases through an LM386 amplifier. It is designed to be simple and effective for various applications, such as educational tools, interactive displays, or assistive devices.

## Project Structure

```
raspberry-pi-zero-button-speak
├── src
│   ├── main.py          # Entry point of the application
│   ├── buttons.py       # Handles button setup and monitoring
│   ├── audio.py         # Manages audio playback
│   └── config.py        # Configuration constants
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

## Setup Instructions

1. **Hardware Requirements:**
   - Raspberry Pi Zero
   - 6 push buttons
   - LM386 audio amplifier
   - Speaker
   - Jumper wires
   - Breadboard (optional)

2. **Wiring:**
   - Connect each button to a GPIO pin on the Raspberry Pi.
   - Connect the LM386 amplifier to GPIO 18 for PWM audio output.
   - Ensure the speaker is connected to the amplifier.

3. **Software Requirements:**
   - Raspbian OS installed on the Raspberry Pi.
   - Python 3.x

4. **Install Dependencies:**
   - Clone the repository:
     ```
     git clone https://github.com/yourusername/raspberry-pi-zero-button-speak.git
     cd raspberry-pi-zero-button-speak
     ```
   - Install the required Python packages:
     ```
     pip install -r requirements.txt
     ```

5. **Enable PWM Audio on Pin 18:**
   - Update and upgrade the system:
     ```sh
     sudo apt update
     sudo apt upgrade
     ```
   - Install PulseAudio:
     ```sh
     sudo apt install pulseaudio
     ```
   - Edit the `/boot/config.txt` file to enable PWM audio on GPIO 18:
     ```sh
     sudo nano /boot/config.txt
     ```
     Add the following lines to the end of the file:
     ```sh
     dtoverlay=pwm-2chan
     dtoverlay=audremap,pins_18_19
     ```
   - Reboot the Raspberry Pi:
     ```sh
     sudo reboot
     ```
   - Verify the audio configuration:
     ```sh
     aplay -l
     ```

## Usage

1. **Run the Application:**
   - Navigate to the `src` directory:
     ```
     cd src
     ```
   - Execute the main script:
     ```
     python main.py
     ```

2. **Press the Buttons:**
   - Each button corresponds to a distinct word or phrase. Press a button to hear the associated audio playback.

## Additional Information

- Ensure that the GPIO pins used for the buttons and audio output are correctly configured in `config.py`.
- Modify the audio files in the project to customize the phrases played for each button.
- This project can be expanded by adding more buttons or integrating additional features such as LED indicators.

## License

This project is open-source and available for modification and distribution under the MIT License.

## Auto-Start on Boot

To auto-start the script when the Raspberry Pi boots up, follow these steps:

1. **Create a systemd service file:**

   Create a new service file for your application:
   ```sh
   sudo nano /etc/systemd/system/button_speak.service


   Add the following content to the service file:
   ```
   [Unit]
Description=Button Speak Service
After=multi-user.target

[Service]
Type=simple
ExecStart=/usr/bin/python3 /home/pi/Tipo-Button-Speak/src/main.py
Restart=on-abort

[Install]
WantedBy=multi-user.target
```
Make sure to replace /home/pi/Tipo-Button-Speak/src/main.py with the correct path to your main.py script.

Reload systemd to recognize the new service:
```
sudo systemctl daemon-reload
sudo systemctl enable button_speak.service
sudo systemctl start button_speak.service
sudo systemctl status button_speak.service
```


## Development 
- Download the image from https://www.raspberrypi.com/software/
- use lite OS
- usine SD card formatter to format SD card
- Enable USB SSH: https://medium.com/@aasthathakker/raspberry-pi-setup-no-monitor-needed-0186e74cc2a4
- Install pyttsx3: [pysstx3](https://pypi.org/project/pyttsx3/)
- install audio drivers: `sudo apt install pulseaudio`
- ultimately ended up using espeak: https://www.dexterindustries.com/howto/make-your-raspberry-pi-speak/
