import cv2
import platform
import subprocess

def list_cameras():
    index = 0
    arr = []
    while True:
        cap = cv2.VideoCapture(index)
        if cap.read()[0]:
            arr.append(index)
            cap.release()
        else:
            break
        index += 1
    return arr

def windows_specific_camera_check():
    arr = []
    index = 0
    while True:
        command = f"ffmpeg -list_devices true -f dshow -i dummy 2>&1 | findstr /C:\"video devices\" /C:\" Alternative name\""
        result = subprocess.run(command, capture_output=True, text=True, shell=True)
        if 'Alternative name' in result.stderr:
            arr.append(index)
            index += 1
        else:
            break
    return arr

def get_available_cameras():
    system = platform.system().lower()
    if system == 'windows':
        camera_indices = windows_specific_camera_check()
    else:
        camera_indices = list_cameras()
    return camera_indices

camera_indices = get_available_cameras()
print("Available camera indices:", camera_indices)
