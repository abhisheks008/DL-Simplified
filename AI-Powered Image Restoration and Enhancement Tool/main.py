import torch
import cv2
import numpy as np
from torchvision.transforms import ToTensor, ToPILImage
from torchvision import transforms
from PIL import Image

# Load a pre-trained SRCNN model (for demo purposes, use a simple model or load a pre-trained one)
class SRCNN(torch.nn.Module):
    def __init__(self):
        super(SRCNN, self).__init__()
        self.conv1 = torch.nn.Conv2d(1, 64, kernel_size=9, padding=4)
        self.conv2 = torch.nn.Conv2d(64, 32, kernel_size=5, padding=2)
        self.conv3 = torch.nn.Conv2d(32, 1, kernel_size=5, padding=2)

    def forward(self, x):
        x = torch.nn.functional.relu(self.conv1(x))
        x = torch.nn.functional.relu(self.conv2(x))
        x = self.conv3(x)
        return x

# Initialize the model and load weights if available
model = SRCNN()
model.load_state_dict(torch.load('srcnn_pretrained.pth', map_location='cpu'))
model.eval()

def super_resolve_image(img_path):
    image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, (image.shape[1] * 2, image.shape[0] * 2))  # Upscale by factor 2
    image = ToTensor()(image).unsqueeze(0)

    with torch.no_grad():
        output = model(image)
    
    output_image = output.squeeze().clamp(0, 1).cpu()
    output_image = ToPILImage()(output_image)
    output_image.save("super_resolved_image.jpg")
    output_image.show()



def denoise_image(img_path):
    image = cv2.imread(img_path)
    denoised_image = cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 21)
    cv2.imwrite("denoised_image.jpg", denoised_image)
    cv2.imshow("Denoised Image", denoised_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



class ColorizationModel(torch.nn.Module):
    # Define a simple U-Net or load pre-trained weights from a colorization model here
    pass

def colorize_image(img_path):
    image = Image.open(img_path).convert("L")  # Convert to grayscale
    image = transforms.ToTensor()(image).unsqueeze(0)

    model = ColorizationModel()
    model.load_state_dict(torch.load("colorization_model.pth", map_location="cpu"))
    model.eval()

    with torch.no_grad():
        colorized = model(image)

    # Convert colorized image back to an RGB format for saving and display
    colorized_image = colorized.squeeze(0).permute(1, 2, 0).numpy()
    colorized_image = np.clip(colorized_image * 255, 0, 255).astype("uint8")
    colorized_image = Image.fromarray(colorized_image)
    colorized_image.save("colorized_image.jpg")
    colorized_image.show()



def process_image(img_path):
    print("Starting Super-Resolution...")
    super_resolve_image(img_path)
    print("Super-Resolution Completed.")

    print("Starting Denoising...")
    denoise_image("super_resolved_image.jpg")
    print("Denoising Completed.")

    print("Starting Colorization...")
    colorize_image("denoised_image.jpg")
    print("Colorization Completed.")


process_image("input_image.jpg")

