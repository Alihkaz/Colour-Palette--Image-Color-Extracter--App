
#imports
import colorgram
import matplotlib


class ColorResult():
    
    def __init__(self): 
      self.rgb_colors=[]
      self.proportions=[]
      self.hex_colors=[]
      self.top_10_colors=[]

    #so what we are doing here is extracting the colors from the images 
    # the we are accessing each color , extracting the rgb values , put them in one list special for that color
    # then appending them to the colors list !,
    #what we are doing here is accessing each color , then seeing its proportion , then saving the proportions in the list !

    #---------------------------------------------------- Extracting colors from the image ----------------------------------------------------

    def exract_colors(self,image):
        
        colors = colorgram.extract(image, 40000)

        #---------------------------------------------------- Extracted colors to RGB code colors----------------------------------------------------
        #converting colors to rgb colors!
        for color in colors:
          r=color.rgb.r
          g=color.rgb.g
          b=color.rgb.b
          new_color=(r,g,b)
          proportion  = color.proportion # proportion of the color!
          self.proportions.append(proportion)
          self.rgb_colors.append(new_color)

        #---------------------------------------------------- RGB  colors to hex code colors----------------------------------------------------

        #converting RGB  colors to hex code colors!
        for rgb in self.rgb_colors:
          # we are bradcasting the division on each rgb set by 255 to avoid (ValueError: RGBA values should be within 0-1 range)
          new_rgb=[value/255 for value in rgb]
          # ranged_rgb=int(new_rgb)/255
          hex_color=matplotlib.colors.to_hex(new_rgb)

          self.hex_colors.append(hex_color)

        self.top_10_colors=self.hex_colors[0:10]

     





