import PIL
from PIL import Image, ImageFont, ImageDraw

# read image and convert to RGB
image=Image.open("readonly/msi_recruitment.gif")
image=image.convert('RGB')

images=[]

for j in range(0,3):
    for i in (0.1, 0.5, 0.9): 
        #add note
        box = Image.new('RGBA', (image.width,80), "black")
        draw = ImageDraw.Draw(box)
        draw.text((0, 0), "channel {}intensity{}".format(j, i), (255,255,255), font = ImageFont.truetype('readonly/fanwood-webfont.ttf', 50))
        image.paste(box, (0, 410))
        
        #change colour 
        r, g, b = image.split()
        if j==0:
            r = r.point(lambda x: x * i)
        if j==1:
            g = g.point(lambda x:x*i)
        if j==2:
            b= b.point(lambda x:x*i)
            
        out = Image.merge('RGB', (r, g, b))
        images.append(out)

first_image=images[0]

contact_sheet=PIL.Image.new(first_image.mode, (first_image.width*3,first_image.height*3))
x=0
y=0

for img in images:
    contact_sheet.paste(img, (x, y))
    if x+first_image.width == contact_sheet.width:
        x=0
        y=y+first_image.height
    else:
        x=x+first_image.width

# resize and display the contact sheet
contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))
display(contact_sheet)
