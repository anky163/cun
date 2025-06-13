
import subprocess

def run_llama_cli(prompt):
    model_path = "/home/k/llama.cpp/models/phi-2.Q4_K_M.gguf"
    llama_cli_path = "/home/k/llama.cpp/build/bin/llama-cli"

    try:
        cmd = [llama_cli_path, "-m", model_path, "-p", prompt]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"[Lỗi hệ thống]: {e.stderr.strip()}"
    except FileNotFoundError as e:
        return f"[Lỗi hệ thống]: {str(e)}"
