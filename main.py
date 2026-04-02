from usb_monitor import detect_usb
from encryption import encrypt_file, decrypt_file, generate_key
from auth import is_authorized

import time

def main():
    print("Secure USB System Running...")

    generate_key()

    known_drives = detect_usb()

    while True:
        time.sleep(5)
        current_drives = detect_usb()

        new_drives = list(set(current_drives) - set(known_drives))

        if new_drives:
            for drive in new_drives:
                print(f"USB Detected: {drive}")

                serial = "MyUSB123"

                if is_authorized(serial):
                    print("Authorized USB ✅")

                    file_path = drive + "test.txt"
                    try:
                        encrypt_file(file_path)
                    except:
                        print("File not found")
                else:
                    print("Unauthorized USB ❌ Access Blocked")

        known_drives = current_drives

if __name__ == "__main__":
    main()