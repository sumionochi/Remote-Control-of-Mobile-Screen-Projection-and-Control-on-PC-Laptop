import subprocess
import cv2

# Connection to the Android device
adb_connect = subprocess.Popen('adb connect 192.168.29.82:24', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, error = adb_connect.communicate()

# Successful or not
if error:
    print(f"Error connecting to device: {error.decode('utf-8')}")
    exit(1)
else:
    print(f"Connected to device: {output.decode('utf-8')}")

# Screen mirroring with audio capture
screen_mirror = subprocess.Popen('adb shell screenrecord --bit-rate=8m --output-format=h264 --audio-source=1 -', shell=True)

# Screen resolution automatic adjustment
device_resolution = subprocess.check_output('adb shell wm size', shell=True).decode().strip().split(': ')[1]
device_width, device_height = map(int, device_resolution.split('x'))

# Aspect ratio calculation
window_aspect_ratio = device_width / device_height
max_window_height = 800
window_height = max_window_height
window_width = int(window_height * window_aspect_ratio)

# Device Pointer on Pc to control mobile
mouse_down = False
start_x, start_y = 0, 0

def mouse_callback(event, x, y, flags, param):
    global mouse_down, start_x, start_y

    if event == cv2.EVENT_LBUTTONDOWN:
        mouse_down = True
        start_x, start_y = x, y
    elif event == cv2.EVENT_LBUTTONUP:
        mouse_down = False

        # Tap coordinates for PC -> mobile control
        tap_x = int((x / window_width) * device_width)
        tap_y = int((y / window_height) * device_height)

        subprocess.Popen(f'adb shell input tap {tap_x} {tap_y}', shell=True)
    elif event == cv2.EVENT_MOUSEMOVE and mouse_down:
        # Swipe coordinates based on the screen resolution
        start_x_device = int((start_x / window_width) * device_width)
        start_y_device = int((start_y / window_height) * device_height)
        end_x_device = int((x / window_width) * device_width)
        end_y_device = int((y / window_height) * device_height)

        subprocess.Popen(f'adb shell input swipe {start_x_device} {start_y_device} {end_x_device} {end_y_device} 500', shell=True)
