# This library was made by https://github.com/561fffDemon

"""
Edited by KDT (https://github.com/561fffDemon)

[+] Made a Class Drawer
[!] Edited a CenterColor Function

"""

from pystyle import Colorate
import shutil

class Drawer():
    def __init__(self):
        pass
    def rgbGrad(self,colors, steps=10):
        gradient = []
        num_colors = len(colors)  # Number of colors in the list

        # Calculate the number of steps between each color
        steps_per_color = steps // (num_colors - 1)

        for i in range(num_colors - 1):
            rgb1 = colors[i]
            rgb2 = colors[i + 1]

            # Calculate the difference between each RGB component
            r_diff = (rgb2[0] - rgb1[0]) / steps_per_color
            g_diff = (rgb2[1] - rgb1[1]) / steps_per_color
            b_diff = (rgb2[2] - rgb1[2]) / steps_per_color

            # Generate the gradient between the current and next color
            for j in range(steps_per_color):
                r = int(rgb1[0] + (r_diff * j))
                g = int(rgb1[1] + (g_diff * j))
                b = int(rgb1[2] + (b_diff * j))
                gradient.append(f"{r};{g};{b}")
                # print(r,g,b)

        gradient.append(f"{colors[-1][0]};{colors[-1][1]};{colors[-1][2]}")
        # print(colors[-1][0],colors[-1][1],colors[-1][2])

        return gradient

    def CenterColor(self,text,colors,steps,type):
        centered = ""
        txt = self.gradientText(colors,steps,text,type)
        spaces = 0
        string = text.split("\n")[0].center(shutil.get_terminal_size().columns)
        for i in string:
            if i == " ":
                spaces += 1
            else:
                break
        for i in txt.split("\n"):
            centered += (" " * spaces) + i + "\n"
        print(centered)
        return centered
    
    def Center(self,s):
        centered = ""
        for i in s.split("\n"):
            centered += i.center(shutil.get_terminal_size().columns) + "\n"
        print(centered,end="")

    def gradientText(self,colors,steps,text,type):
        gradient = self.rgbGrad(colors,steps)
        if type == "V":
            return f"{Colorate.Vertical(gradient, text, 1)}"
        elif type == "H":
            return f"{Colorate.Horizontal(gradient, text, 1)}"
        else:
            return f"{Colorate.Vertical(gradient, 'Incorrect type, Type can be V - Vertical & H - Horizontal', 1)}"
        
    def converting(self,dist):
        new = []
        for i in dist:
            new.append([i[0],i[1],i[2]])
        return new