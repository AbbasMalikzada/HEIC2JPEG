
# HEIC2JPEG Python Script

HEIC2JPEG is a simple Python script designed to convert HEIC images to JPEG format. This script can be particularly useful for users who need to batch convert HEIC (High Efficiency Image Coding) files to a more widely supported JPEG format.

## Features

- Converts `.HEIC` files to `.JPEG` images.
- Easy to use: Just put it in the folder containing the `.HEIC` files and run the script.
- Batch processing: Automatically processes all HEIC files in the directory.
- Lightweight and efficient.

## Installation

To use the HEIC2JPEG script, make sure you have Python installed on your system. You can download Python from the official website: [Python Downloads](https://www.python.org/downloads/).

### Required Dependencies

This script requires the `pyheif` and `Pillow` libraries to process and convert HEIC files.

You can install the necessary dependencies by running:

```bash
pip install pyheif Pillow
```

## Usage

1. Download the script and place it in the folder containing your `.HEIC` files.
2. Run the script:

```bash
python heic2jpeg.py
```

The script will convert all `.HEIC` files in the current directory to `.JPEG` format and save them in the same folder.

### Command-line arguments (optional):

- `--output_folder`: Specify a custom folder for saving converted files.

Example:

```bash
python heic2jpeg.py --output_folder /path/to/your/folder
```

## Example

Assuming you have a directory with the following files:

```
image1.HEIC
image2.HEIC
image3.HEIC
```

After running the script, the resulting `.JPEG` files will be:

```
image1.JPEG
image2.JPEG
image3.JPEG
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## Acknowledgements

- [pyheif](https://github.com/xzdk/pyheif) for providing the ability to read HEIC files in Python.
- [Pillow](https://python-pillow.org/) for handling image conversion to JPEG format.
