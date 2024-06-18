# pip install rembg
# Call libraries
from rembg import remove
from PIL import Image

# store inpute
input_path = "original_pic.jpg"

# define output name
output_path = "output.png"

# Reading picture
input = Image.open(input_path)

# Remove bg
output = remove(input)

# Save final pic 
output.save(output_path)
