import qrcode
data = "https://github.com"  #example data
filename = "web.png"  #output file name
img = qrcode.make(data)
img.save(filename)
