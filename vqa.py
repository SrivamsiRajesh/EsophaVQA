from openai import OpenAI
import base64
from io import BytesIO
from PIL import Image
from prompts import SYSTEM_PROMPT

class EAVQA:
    def __init__(self, api_key):
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=api_key
        )
        self.model = "mistralai/mistral-small-3.2-24b-instruct:free"
    
    def encode_image(self, image):
        buffered = BytesIO()
        image.save(buffered, format="PNG")
        return base64.b64encode(buffered.getvalue()).decode('utf-8')
    
    def analyze(self, image, question):
        if image is None:
            return "Upload an image first"
        
        base64_image = self.encode_image(image)
        
        try:
            completion = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": question},
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/png;base64,{base64_image}"
                                }
                            }
                        ]
                    }
                ],
                max_tokens=600,
                temperature=0.2
            )
            
            return completion.choices[0].message.content
        
        except Exception as e:
            return f"Error: {str(e)}"