from PIL import Image
import os

def generate_rotated_frames(input_image_path, output_folder):

    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the image
    img = Image.open(input_image_path)

    # Get the original dimensions
    width, height = img.size

    # # Calculate the size needed to prevent cropping during rotation
    # # Using the diagonal of the image as the new size
    diagonal = int((width ** 2 + height ** 2) ** 0.5)

    # Create a new image
    new_size = (diagonal, diagonal)
    background = Image.new('RGBA', new_size, (255, 255, 255, 0))

    # Calculate position to paste the original image
    paste_x = (diagonal - width) // 2
    paste_y = (diagonal - height) // 2

    # Paste the original image onto the center of the larger background
    background.paste(img, (paste_x, paste_y))

    # Generate frames range = nr of frames
    for i in range(300):
        # Calculate rotation angle
        angle = i * 1.2

        # Rotate the image
        rotated = img.rotate(angle, expand=False, center=(width / 2, height / 2))

        # Save the frame
        frame_path = os.path.join(output_folder, f'frame_{i:03d}.png')
        rotated.save(frame_path)

        # Optional: Print progress
        if (i + 1) % 30 == 0:
            print(f'Generated {i + 1} frames...')

    print('All frames generated successfully!')


if __name__ == "__main__":
    input_image = "D:\\playerGIF\\first.png"  # Replace with your image path
    output_folder = "D:\\playerGIF"  # Replace with desired output folder
    generate_rotated_frames(input_image, output_folder)