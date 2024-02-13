#Trust me i know ML/DL 🥲
# image classification using a deep neural network and a pre-trained model from the torchvision library. This example will use a ResNet model to classify images into 1,000 different categories from the ImageNet dataset.
#pip install torch torchvision

import torch
from torchvision import models, transforms
from PIL import Image

def load_and_preprocess_image(image_path):
    # Load and preprocess the input image
    image = Image.open(image_path).convert("RGB")
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    input_tensor = preprocess(image)
    input_batch = input_tensor.unsqueeze(0)  # Add a batch dimension
    return input_batch

def perform_image_classification(image_path):
    # Load a pre-trained ResNet model
    model = models.resnet50(pretrained=True)
    model.eval()

    # Load and preprocess the input image
    input_batch = load_and_preprocess_image(image_path)

    # Make a prediction
    with torch.no_grad():
        output = model(input_batch)

    # Load the labels used by the pre-trained model
    with open("imagenet_labels.txt", "r") as file:
        labels = [line.strip() for line in file.readlines()]

    # Get the predicted class index
    _, predicted_index = torch.max(output, 1)
    predicted_label = labels[predicted_index.item()]

    return predicted_label

if __name__ == "__main__":
    # Example image for classification
    example_image_path = "example_image.jpg"

    # Perform image classification
    predicted_label = perform_image_classification(example_image_path)

    # Display the result
    print(f"Predicted label: {predicted_label}")
