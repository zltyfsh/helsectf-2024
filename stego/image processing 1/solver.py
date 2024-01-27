import numpy as np
from PIL import Image
from pprint import pprint

data = np.array(Image.open('ekorn.png'))
ft = np.fft.fft2(data)
fshift = np.fft.fftshift(ft)
spectrum = np.log(np.abs(fshift))

im = Image.fromarray(spectrum.astype(np.uint8))
im.save('processed.png')
