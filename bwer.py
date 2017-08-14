from PIL import Image
import glob, os

for infile in glob.glob("./examples_raw/*.png"):
    path, fname = os.path.split(infile)
    im = Image.open(infile)
    im_bw = im.convert('1', dither=Image.NONE)
    im_bw.save("./examples_bw/{}".format(fname))
