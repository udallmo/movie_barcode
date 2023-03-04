


<!-- PROJECT LOGO -->
<div align="center">

<h3 align="center">Video Barcode Converter</h3>

  <p>
    This Python script allows you to extract the dominant color for each frame of a video and visualize the colors in a color wheel or color bar. The script uses the OpenCV library to read the video and extract each frame as a numpy array. Then, it uses the KMeans algorithm from scikit-learn to cluster the pixels of each frame into a specified number of clusters (usually 3-5). Finally, the script calculates the centroid of each cluster and extracts the RGB values as the dominant colors.
</div>


<!-- ABOUT THE PROJECT -->
## About The Project

[![image](https://user-images.githubusercontent.com/26352484/222923323-78db6438-420a-44fa-a361-640fbe0ae04c.png)](https://www.etsy.com/ca/listing/1416775752/custom-video-barcodes)


### Built With

* Python
* Numpy
* OpenCV

<!-- USAGE EXAMPLES -->
## System Diagram

![system_flowchart drawio](https://user-images.githubusercontent.com/26352484/222925389-b8a4b048-1789-4932-a0eb-483b49337466.png)


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Installation

1. Clone the repo
   ```sh
   git clone git@github.com:udallmo/movie_barcode.git
   ```
3. Install packages
   ```sh
   pip install -r requirements.txt
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Running the script
   ```sh
   python .\main.py <VideoFilePath> <NameOutput>
   ```

example:
   ```sh
python .\main.py D:\Videos\spyxfamily.mkv spy_family_ep1
   ```

<!-- ROADMAP -->
## Roadmap

- [X] Output Color Bars
- [X] Output Color Wheels
- [ ] Output custom templates



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.
