import moviepy.editor as mpy

def make_frame(t):
    return  # returns a 8-bit RGB array

clip = mpy.TextClip("Hello !", font="Amiri-Bold", fontsize=70, color="black")
clip.write_gif("circle.gif",fps=15)