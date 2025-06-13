import subprocess
import time
import os

def run_llama_cli(prompt):
    model_path = "/home/k/llama.cpp/models/phi-2.Q4_K_M.gguf"
    llama_cli_path = "/home/k/llama.cpp/build/bin/llama-cli"
    log_path = "logs/prompt_debug.txt"

    raw_prompt = prompt.strip()
    if raw_prompt.endswith('?') or len(raw_prompt.split()) <= 5:
        wrapped_prompt = f"Bạn là một trợ lý AI tên Cún. Nếu được hỏi '{raw_prompt}', hãy giới thiệu chính bạn ngắn gọn."
    else:
        wrapped_prompt = raw_prompt

    os.makedirs("logs", exist_ok=True)
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(f"\n=== {time.ctime()} ===\n")
        f.write(f"[PROMPT RAW]    {raw_prompt}\n")
        f.write(f"[PROMPT FINAL]  {wrapped_prompt}\n")

    try:
        cmd = [
            llama_cli_path,
            "-m", model_path,
            "-p", wrapped_prompt,
            "--n-predict", "128"
        ]
        start = time.time()
        result = subprocess.run(cmd, capture_output=True, text=True, check=True, timeout=60)
        end = time.time()
        duration = end - start
        output = result.stdout.strip()

        if "def " in output or "return " in output:
            output = "[⚠ Bot có vẻ generate nhầm sang code. Gợi ý: chỉnh lại prompt.]\n" + output

        return f"[⏱ {duration:.2f}s]\n" + output
    except subprocess.CalledProcessError as e:
        return f"[Lỗi hệ thống]: {e.stderr.strip()}"
    except FileNotFoundError as e:
        return f"[Lỗi hệ thống]: {str(e)}"
