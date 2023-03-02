# Open the PNG image file
with open('input.png', 'rb') as f:
    data = f.read()

# Parse the PNG file header
header = data[:8]

# Check if the file is a valid PNG image
if header != b'\x89PNG\r\n\x1a\n':
    raise ValueError('Invalid PNG file')

# Extract the image data from the PNG file
img_data = data[33:]

# Convert the image data to grayscale by taking the average of the RGB channels
gray_data = bytearray()
for i in range(0, len(img_data), 3):
    gray = int((img_data[i] + img_data[i+1] + img_data[i+2]) / 3)
    gray_data.append(gray)

# Write the PGM image file
with open('output.pgm', 'wb') as f:
    # Write the PGM file header with width and height
    width, height = 100, 100  # Change this to the actual image size
    f.write(f'P2\n{width} {height}\n255\n'.encode())
    # Write the grayscale image data
    f.write(gray_data)