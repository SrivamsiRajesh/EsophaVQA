import gradio as gr

def create_interface(vqa):
    
    with gr.Blocks(theme=gr.themes.Soft()) as demo:
        gr.Markdown("# Esophageal Atresia AI Diagnosis")
        
        with gr.Row():
            with gr.Column():
                image = gr.Image(type="pil", label="Upload Medical Image")
                question = gr.Textbox(
                    label="Question",
                    placeholder="Is there esophageal atresia? If yes, what type? If no, is it normal?",
                    lines=2
                )
                btn = gr.Button("🔍 Analyze", variant="primary", size="lg")
            
            with gr.Column():
                output = gr.Textbox(label="Diagnosis", lines=15)
        
        btn.click(vqa.analyze, [image, question], output)

    
    return demo