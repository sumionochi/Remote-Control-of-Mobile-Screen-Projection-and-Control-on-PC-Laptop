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
