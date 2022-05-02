1. Import Necessary Libraries

import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

2. Selecting the Dataset

For this example, use Dataset Top Games on Google Play Store from Kaggle.

Download the Dataset and save it in your current working directory for hassle-free code implementation.
Import the dataset into a variable of your choice. Here our data is imported to variable df.

df = pd.read_csv("android-games.csv")

3. Selecting the Text and Amount of Text for Word Cloud

4. Check for NULL values

It is required to check for the null values in our dataset as while creating the Word Cloud, it would not accept text with nan values.

df.isna().sum()

4. Adding Text to a Variable
Based on the parameters from Step 3, add the Text Data to a variable of your choice. Here, we are adding the data into variable text.

text = " ".join(cat.split()[1] for cat in df.category)

5. Creating the Word Cloud

Create an object of class WordCloud with the name of your choice and call the generate() method. Here we have created the object with the name word_cloud. 

WordCloud() takes several arguments as per the need. Here we are adding two arguments:

 1. collocations = False, which will ignore the collocation words from the Text

2. background_color = ‘White’, which will make the words look clearer

The .generate() method takes one argument of the text we created. In our case, we will give the text variable as an argument to .generate().

word_cloud = WordCloud(collocations = False, background_color = 'white').generate(text)

6. Plotting the Word Cloud
Using the .imshow() method of matplotlib.pyplot to display the Word Cloud as an image.

.imshow() takes several arguments, but in our example, we are taking two arguments:

1. word_cloud created in Step 5

2. interpolation = ‘bilinear’

Since we are creating an image with .imshow(), the resampling of the image is done as the image pixel size and screen resolution doesn’t not match. Here we are using bilinear interpolation.

Plotting the image with axis off as we don’t want axis ticks in our image.

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
