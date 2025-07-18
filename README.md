# latexit

Render LaTeX math formulas to PNG images from the command line, using pure Python and matplotlib's mathtext engine.

## Features
- **Pure Python**: No system LaTeX required, cross-platform.
- **CLI tool**: Convert LaTeX math snippets to PNG images -> No Background (good for slides)
- **Transparent background** and customizable DPI, font size, and padding.

## Limitations
- Only a subset of LaTeX math is supported (see [matplotlib mathtext documentation](https://matplotlib.org/stable/tutorials/text/mathtext.html)).

## Installation

### Option 1 Install via pip

```sh
$ pip install latexit
```

### Option 2 Install manually
1. Clone the repository:
```sh
$ git clone https://github.com/furkandotpy/latexit.git
$ cd latexit
```
2. Install dependencies:
```sh
pip install -r requirements.txt
# or, if using pyproject.toml:
pip install .
```

## Usage

```sh
latexit "\\frac{1}{2}" output.png
```
![alt text](https://github.com/furkandotpy/latexit/blob/main/output.png?raw=true)
The image is not rendered quite like I would have liked because it is a png. The background is removed which makes it perfect for slides!

Options:
- `--dpi`: Set output DPI (default: 300)
- `--fontsize`: Set font size (default: 24)
- `--padding`: Set padding in pixels (default: 10)


## License
MIT

## Acknowledgments
This project was developed with guidance and code suggestions from an AI assistant Cursor (powered by OpenAI's GPT-4). 
