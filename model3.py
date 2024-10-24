import os
import cv2
import numpy as np
fresh_folder = 'C:\\Users\\navya\\Desktop\\freshbanana'
rotten_folder = 'C:\\Users\\navya\\Desktop\\rottenbanana'
fresh_images = [cv2.imread(os.path.join(fresh_folder, img)) for img in os.listdir(fresh_folder)]
rotten_images = [cv2.imread(os.path.join(rotten_folder, img)) for img in os.listdir(rotten_folder)]
def average_rgb(image):
# Convert the image to float32 for precision
    image = image.astype(np.float32)
# Calculate the average color
    avg_color = image.mean(axis=(0, 1))  # Mean over height and width
    return avg_color
fresh_avg_rgb = [average_rgb(img) for img in fresh_images]
rotten_avg_rgb = [average_rgb(img) for img in rotten_images]
fresh_avg = np.mean(fresh_avg_rgb, axis=0)
rotten_avg = np.mean(rotten_avg_rgb, axis=0)

print("Average RGB for Fresh Bananas:", fresh_avg)
print("Average RGB for Rotten Bananas:", rotten_avg)
import matplotlib.pyplot as plt

# Bar chart for comparison
labels = ['Red', 'Green', 'Blue']
fresh_rgb = fresh_avg
rotten_rgb = rotten_avg

x = np.arange(len(labels))
plt.bar(x - 0.2, fresh_rgb, 0.4, label='Fresh Bananas', color='green')
plt.bar(x + 0.2, rotten_rgb, 0.4, label='Rotten Bananas', color='brown')
plt.xlabel('Color Channels')
plt.ylabel('Average Value')
plt.title('Average RGB Values of Bananas')
plt.xticks(x, labels)
plt.legend()
plt.show()


"""def classify_banana(avg_rgb):
    if avg_rgb[1] > 174 and avg_rgb[0] > 149 and avg_rgb[2] > 184.5:  # Using green channel as an example
        return 'Fresh'
    else:
        return 'Rotten'

new_image = cv2.imread(r'C:/Users/navya/Downloads/dataset/Test/freshbanana/b_f001.jpg')
new_avg_rgb = average_rgb(new_image)
classification = classify_banana(new_avg_rgb)
print("The new banana is:", classification)"""

def average_rgb(image):
    if image is None:
        raise ValueError("Image not loaded correctly.")
    image = image.astype(np.float32)
    avg_color = image.mean(axis=(0, 1))
    return avg_color

# Function to classify banana
def classify_banana(avg_rgb):
    if avg_rgb[1] > 174 and avg_rgb[0] > 149 and avg_rgb[2] > 184.5:  # Adjust thresholds based on your data
        return 'Fresh'
    else:
        return 'Rotten'

# Load the image (ensure the path is correct)
new_image_path = r'C:\Users\navya\Desktop\b_r002.png'
new_image = cv2.imread(new_image_path)

# Check if the image is loaded correctly
if new_image is None:
    print(f"Error: Could not load image from {new_image_path}")
else:
    # Calculate the average RGB and classify the banana
    new_avg_rgb = average_rgb(new_image)
    classification = classify_banana(new_avg_rgb)
    print("The new banana is:", classification)





