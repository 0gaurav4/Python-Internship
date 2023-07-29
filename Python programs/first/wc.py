# author : @mysgrown

import numpy as np
from PIL import Image
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

# Replace 'C:\\' with the path to your JPG image
image_path = 'C:\\Users\\gaura\\OneDrive\\Desktop\\Python Internship\\Python programs\\first\\p1.png'
image = Image.open(image_path)

image_array = np.array(image)

# Replace 'C:\\' with the path to your text file or provide your text here
with open('C:\\Users\\gaura\\OneDrive\\Desktop\\Python Internship\\Chapters\\day1.html', 'r') as file:
    text = file.read()

wordcloud = WordCloud(background_color=None, mask=image_array, contour_color='white', contour_width=1, stopwords=set(STOPWORDS))
wordcloud.generate(text)

plt.figure(figsize=(10, 10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()