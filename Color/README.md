# YouTube Color Palette Extractor

This web application extracts the dominant color palette from YouTube video thumbnails. Users can input a YouTube URL, and the app will display the three most prominent colors used in the video's thumbnail.

## Features

- Extract dominant colors from YouTube video thumbnails
- Display color palette with hex codes
- Copy hex codes to clipboard with a single click
- Responsive design for both desktop and mobile devices

## Technologies Used

- Backend: Python with Flask
- Frontend: HTML, CSS, JavaScript
- Color Extraction: scikit-learn (K-means clustering)
- Image Processing: Pillow (PIL)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/youtube-color-palette-extractor.git
   cd youtube-color-palette-extractor
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install flask pytube requests pillow numpy scikit-learn
   ```

## Usage

1. Run the Flask application:
   ```
   python color.py
   ```

2. Open a web browser and navigate to `http://localhost:5000`

3. Paste a YouTube URL into the input field and click "Extract Colors"

4. The app will display the three dominant colors from the video's thumbnail

5. Click on a color to copy its hex code to your clipboard

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Created By

[Vivek Tiwari](https://github.com/probablyvivek)