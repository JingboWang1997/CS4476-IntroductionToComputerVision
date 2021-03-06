import matplotlib.pyplot as plt

def displaySeam(im, seam, type):
    plt.imshow(im)
    if type == "VERTICAL":
        for i in xrange(len(seam)):
            plt.plot(seam[i], i,'r,')
    elif type == "HORIZONTAL":
        for i in xrange(len(seam)):
            plt.plot(i, seam[i], 'r,')
    plt.show()

