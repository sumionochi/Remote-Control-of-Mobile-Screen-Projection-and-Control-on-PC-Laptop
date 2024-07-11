import subprocess

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
