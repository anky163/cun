import os
import subprocess
from datetime import datetime

LLAMA_CLI = "/home/k/llama.cpp/build/bin/llama-cli"
MODEL_PATH = "/home/k/llama.cpp/models/phi-2.Q4_K_M.gguf"
LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "last_run.txt")
TEST_PROMPT = "Bạn là ai?"


def write_log(content):
    os.makedirs(LOG_DIR, exist_ok=True)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"\n=== {datetime.now()} ===\n")
        f.write(content + "\n")


def check_file(path, label):
    if not os.path.isfile(path):
        msg = f"[❌ MISSING] {label} not found at: {path}"
        write_log(msg)
        print(msg)
        return False
    print(f"[✅ FOUND] {label}")
    return True


def run_test_prompt():
    try:
        cmd = [LLAMA_CLI, "-m", MODEL_PATH, "-p", TEST_PROMPT, "--n-predict", "128"]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True, timeout=60)
        output = result.stdout.strip()
        write_log("[✅ PASSED] llama-cli output:\n" + output)
        print("[✅ PASSED] Test prompt ran successfully. Check logs/last_run.txt")
    except subprocess.TimeoutExpired:
        msg = "[⏰ TIMEOUT] llama-cli chạy quá 60s. Có thể model đang load chậm hoặc prompt không rõ.\n" \
              "→ Thử chạy thủ công lệnh sau để xem chi tiết:\n" \
              f"{ ' '.join(cmd) }"
        write_log(msg)
        print(msg)
    except subprocess.CalledProcessError as e:
        msg = "[❌ llama-cli FAILED]\n" + e.stderr.strip()
        write_log(msg)
        print(msg)
    except FileNotFoundError as e:
        msg = f"[❌ FileNotFoundError]\n{str(e)}"
        write_log(msg)
        print(msg)


if __name__ == "__main__":
    print("🐶 Đang kiểm tra hệ thống Cún CLI...\n")
    ok = True
    ok &= check_file(LLAMA_CLI, "llama-cli")
    ok &= check_file(MODEL_PATH, "model .gguf")
    if ok:
        run_test_prompt()
    else:
        print("\n⚠ Dừng test vì thiếu file.")
