from PIL import Image
from functools import reduce
import math, operator

pic1 = Image.open("image\\landscape.jpg")
pic2 = Image.open("image\\us.jpg")
h1 = pic1.histogram()
h2 = pic2.histogram()
diff = math.sqrt(reduce(operator.add, list(map(lambda a,b: (a-b)**2, h1, h2)))/len(h1))

# print(diff)