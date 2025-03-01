from transformers import CLIPTextModel, CLIPTokenizer # type: ignore
from diffusers import StableDiffusionPipeline # type: ignore
import torch # type: ignore
from concurrent.futures import ThreadPoolExecutor

# Load the tokenizer and model
tokenizer = CLIPTokenizer.from_pretrained("openai/clip-vit-base-patch32")
text_model = CLIPTextModel.from_pretrained("openai/clip-vit-base-patch32")
   
# Load the Stable Diffusion pipeline
pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", torch_dtype=torch.float32)
pipe = pipe.to("cpu")

# Define the text prompt
prompt = """
            A futuristic human-AI hybrid working late at night in a high-rise office with a city skyline view. 
            The person has a cybernetic brain with glowing neural circuits, seamlessly integrated with advanced 
            AI technology. They are focused on multiple high-tech monitors displaying world maps, 
            data analytics, and futuristic UI elements. The dimly lit room is illuminated by the screens and 
            soft ambient lighting, creating a cyberpunk aesthetic. Ultra-detailed, hyper-realistic, 
            cinematic lighting, 8K resolution, highly detailed textures
        """

# Generate images
images = pipe(prompt, num_inference_steps=100, guidance_scale=7.5).images

# Function to save a single image
def save_image(index, image):
    image.save(f"util/temp/generated_image_{index}.png")

# Save the generated images in parallel
with ThreadPoolExecutor() as executor:
    executor.map(save_image, range(len(images)), images)

print("Images generated and saved.")