
import gradio as gr
from cun_core import run_llama_cli  # GỌI logic xử lý từ file lõi

# Giao diện Gradio
with gr.Blocks() as demo:
    gr.Markdown("# 🐶 Cún CLI toy")
    inp = gr.Textbox(label="Mày muốn hỏi gì?")
    out = gr.Textbox(label="Cún trả lời nè", lines=10)
    inp.submit(fn=run_llama_cli, inputs=inp, outputs=out)

demo.launch()
