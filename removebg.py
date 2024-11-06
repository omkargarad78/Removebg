from rembg import remove
import easygui
from PIL import Image

inputPath=easygui.fileopenbox(title='Select the Image')
outputPath = easygui.filesavebox("Choose where to save file")

input=Image.open(inputPath)
output=remove(input)
output.save(f"{outputPath}.png")


 