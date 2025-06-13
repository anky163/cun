import subprocess
import time

print("🐶 Bắt đầu kiểm tra hệ thống Cún...")

try:
    # Bước 1: chạy check_app.py
    check = subprocess.run(["python3", "check_app.py"], check=True)
    print("\n✅ Hệ thống ổn. Đang mở giao diện Cún GUI...\n")

    time.sleep(1)

    # Bước 2: mở GUI
    subprocess.run(["python3", "app.py"])
except subprocess.CalledProcessError:
    print("\n❌ Có lỗi khi kiểm tra hệ thống. Dừng chạy GUI.")
