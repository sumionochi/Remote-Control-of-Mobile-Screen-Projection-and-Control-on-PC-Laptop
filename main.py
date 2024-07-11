import subprocess
import cv2
import tkinter as tk
import time

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

def send_keyevent(keycode):
    subprocess.Popen(f'adb shell input keyevent {keycode}', shell=True)

# Tkinter window
root = tk.Tk()
root.title("Android Device Control")
instructions_label = tk.Label(root, text="Press the buttons to control your Android device:")
instructions_label.pack(pady=10)
button_frame = tk.Frame(root)
button_frame.pack()

# Button functions
def left():
    send_keyevent(123)

def right():
    send_keyevent(124)

def up():
    send_keyevent(19)

def down():
    send_keyevent(20)

left_button = tk.Button(button_frame, text="Left", command=left)
left_button.grid(row=0, column=0, padx=5, pady=5)

right_button = tk.Button(button_frame, text="Right", command=right)
right_button.grid(row=0, column=1, padx=5, pady=5)

up_button = tk.Button(button_frame, text="Up", command=up)
up_button.grid(row=0, column=2, padx=5, pady=5)

down_button = tk.Button(button_frame, text="Down", command=down)
down_button.grid(row=0, column=3, padx=5, pady=5)

def play_pause_music():
    send_keyevent(85)

def next_song():
    send_keyevent(87)

def prev_song():
    send_keyevent(88)

music_button = tk.Button(button_frame, text="Play/Pause Music", command=play_pause_music)
music_button.grid(row=1, column=0, padx=5, pady=5)

next_song_button = tk.Button(button_frame, text="Next Song", command=next_song)
next_song_button.grid(row=1, column=1, padx=5, pady=5)

prev_song_button = tk.Button(button_frame, text="Previous Song", command=prev_song)
prev_song_button.grid(row=1, column=2, padx=5, pady=5)

def run_test_case(case):
    global test_result_label
    test_result_label.config(text="Running test case...")
    root.update()

    if case == 1:
        subprocess.Popen('adb shell am start -n com.android.camera/.Camera', shell=True)
        subprocess.Popen('adb shell input keyevent 4', shell=True)  # Press the back button to close the camera app
    elif case == 2:
        subprocess.Popen('adb shell am start -n com.google.android.apps.messaging/.ui.ConversationListActivity', shell=True)
        subprocess.Popen('adb shell input keyevent 4', shell=True)  # Press the back button to close the messaging app
    elif case == 3:
        subprocess.Popen('adb shell am start -n com.google.android.googlequicksearchbox/.SearchActivity', shell=True)
        subprocess.Popen('adb shell input keyevent 4', shell=True)  # Press the back button to close the music player app
    elif case == 4:
        subprocess.Popen('adb shell am start -n com.miui.calculator/.cal.CalculatorActivity', shell=True)
        subprocess.Popen('adb shell input keyevent 4', shell=True)  # Press the back button to close the calculator app
    elif case == 5:
        subprocess.Popen('adb shell am start -n com.google.android.dialer/.extensions.GoogleDialtactsActivity', shell=True)
        subprocess.Popen('adb shell input keyevent 4', shell=True)  # Press the back button to close the browser app
    else:
        test_result_label.config(text="Invalid test case")

    root.update()

test_case_frame = tk.Frame(root)
test_case_frame.pack(pady=10)

test_case_1_button = tk.Button(test_case_frame, text="Test Case 1", command=lambda: run_test_case(1))
test_case_1_button.grid(row=0, column=0, padx=5, pady=5)

test_case_2_button = tk.Button(test_case_frame, text="Test Case 2", command=lambda: run_test_case(2))
test_case_2_button.grid(row=0, column=1, padx=5, pady=5)

test_case_3_button = tk.Button(test_case_frame, text="Test Case 3", command=lambda: run_test_case(3))
test_case_3_button.grid(row=0, column=2, padx=5, pady=5)

test_case_4_button = tk.Button(test_case_frame, text="Test Case 4", command=lambda: run_test_case(4))
test_case_4_button.grid(row=0, column=3, padx=5, pady=5)

test_case_5_button = tk.Button(test_case_frame, text="Test Case 5", command=lambda: run_test_case(5))
test_case_5_button.grid(row=0, column=4, padx=5, pady=5)

test_result_label = tk.Label(test_case_frame, text="")
test_result_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

last_frame_time = 0
new_frame_time = 0
min_frame_time = 1 / 10 

while True:
    try:
        # Screen capture from the device
        output, error = subprocess.Popen('adb exec-out screencap -p > screen.png', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        if error:
            print(f"Error capturing screen: {error.decode('utf-8')}")
            continue

        # OpenCV image loaded for screen capture
        img = cv2.imread('screen.png')

        # Resizing the image to fit the window
        img = cv2.resize(img, (window_width, window_height))

        # Display the screen capture
        cv2.imshow('Android Screen', img)

        cv2.setMouseCallback('Android Screen', mouse_callback)

        # Frame rate calculation
        new_frame_time = time.time()
        frame_time = new_frame_time - last_frame_time
        fps = 1 / frame_time
        last_frame_time = new_frame_time
        print(f"FPS: {int(fps)}")

        if frame_time < min_frame_time:
            time.sleep(min_frame_time - frame_time)

        # Processing Tkinter events
        root.update_idletasks()
        root.update()

        # Commands to send to the device based on user input
        key = cv2.waitKey(max(1, int(1000 / 60)))
    except cv2.error as e:
        print(f"OpenCV error: {e}")
        break

    if key == ord('q'):
        break

# Stopping screen mirroring
screen_mirror.terminate()

# Release the OpenCV window
cv2.destroyAllWindows()
