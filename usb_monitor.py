import win32file

def detect_usb():
    drives = win32file.GetLogicalDrives()
    drive_list = []

    for d in range(26):
        if drives & (1 << d):
            drive_letter = f"{chr(65 + d)}:\\"
            drive_list.append(drive_letter)

    return drive_list