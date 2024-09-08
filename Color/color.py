from flask import Flask, request, jsonify, render_template
from pytube import YouTube
import requests
from PIL import Image
from io import BytesIO
import numpy as np
from sklearn.cluster import KMeans
from urllib.parse import urlparse, parse_qs
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(int(rgb[0]), int(rgb[1]), int(rgb[2]))

def extract_colors(image, num_colors=3):
    # Resize image to speed up processing and reduce memory usage
    image.thumbnail((100, 100))
    pixels = np.array(image).reshape(-1, 3)
    
    # Perform k-means clustering
    kmeans = KMeans(n_clusters=num_colors, random_state=42)
    kmeans.fit(pixels)
    
    # Get the cluster centers (colors)
    colors = kmeans.cluster_centers_
    
    # Sort colors by frequency
    labels = kmeans.labels_
    color_counts = np.bincount(labels)
    colors = colors[np.argsort(color_counts)][::-1]
    
    # Convert colors to hex format
    hex_colors = [rgb_to_hex(color) for color in colors]
    return hex_colors

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        youtube_url = request.form.get('url')
        
        if not youtube_url:
            return jsonify({'error': 'No YouTube URL provided'}), 400

        try:
            # Validate the URL
            parsed_url = urlparse(youtube_url)
            if not parsed_url.scheme or not parsed_url.netloc:
                return jsonify({'error': 'Invalid URL format'}), 400

            # Extract the YouTube thumbnail
            yt = YouTube(youtube_url)
            thumbnail_url = yt.thumbnail_url
            
            # Log the thumbnail URL
            app.logger.info(f'Fetching thumbnail from: {thumbnail_url}')
            
            response = requests.get(thumbnail_url)
            response.raise_for_status()  # Raise an error for bad responses
            
            img = Image.open(BytesIO(response.content))
            hex_palette = extract_colors(img)
            
            return jsonify({'colors': hex_palette})

        except requests.exceptions.RequestException as e:
            app.logger.error(f'Error fetching thumbnail: {e}')
            return jsonify({'error': 'Failed to fetch the thumbnail image. Please check the URL and try again.'}), 500
        
        except Exception as e:
            app.logger.error(f'An unexpected error occurred: {e}')
            return jsonify({'error': 'An unexpected error occurred. Please try again.'}), 500
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
