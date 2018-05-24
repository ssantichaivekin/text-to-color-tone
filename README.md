This is a python example that displays the color tone of a text. The process of transforming text to color works as follows:

1. Use Google search API to search images using the text as the query.
2. Obtain from the search thumbnails (currently 6 by default) of the text.
3. Use KNN (K nearest neighbors) algorithm on the thumnails to get colors (5 by default) that best represent the pixel concatenation.
4. Display the colors (called collectively as color tone) using matplotlib.

The app also supports command line arguments using the function argparse. Here is an example of how you run the commands:

```bash
python3 get_color_tone.py 'Groot'
python3 get_color_tone.py 'Snack'
```

Here are some example usage snapshot of the app.

<img src="screenshot1.png" width="400"/> <img src="screenshot2.png" width="400"/>

The index of the app is in get_color_tone.py -- you should start from there if you want to read how the app works.

Python Library Dependencies: scikit, matplotlib, opencv(cv2), requests

Built @ May 2018

Note that you will need your own google API key to be able to run the app. The app by default tries to read it from google-api-key.txt -- If you want to try this on your own machine, make you you get a Google Custom Search API key.