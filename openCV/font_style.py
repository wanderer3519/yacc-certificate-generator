from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt


image_path = '1.jpg'  
image = Image.open(image_path)
draw = ImageDraw.Draw(image)


text = "Your Text Here" #we can add the required text here
font_size = 40 #font size
font_path = "arial.ttf"  #font style
font = ImageFont.truetype(font_path, font_size)


text_position = (50, 50) #where the text should be placed(cordinates)


draw.text(text_position, text, font=font, fill="black") #here we can change colour


output_path = 'output_image.jpg'
image.save(output_path)


plt.imshow(image)
plt.axis('off')
plt.show()
