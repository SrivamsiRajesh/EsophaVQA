import os
from dotenv import load_dotenv
from vqa import EAVQA
from ui import create_interface

def main():
    
    load_dotenv()
    
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        print("\n❌ Error: OPENROUTER_API_KEY not found in .env file")
        print("Create a .env file with: OPENROUTER_API_KEY='your-key'")
        return
    
    
    vqa = EAVQA(api_key)
    
    print("\n🚀 Launching Gradio interface...")
    demo = create_interface(vqa)
    demo.launch(share=True, server_port=7860)

if __name__ == "__main__":
    main()