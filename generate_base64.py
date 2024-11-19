import base64

# Open the image and encode it to base64 -test
with open("assests/profilepic.png", "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode()

# Print the base64-encoded image string
print(encoded_image)
