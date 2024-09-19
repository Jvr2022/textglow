# TextGlow

TextGlow is a Python package that adds "glow" effects to text for terminal-based applications. It allows you to apply ANSI color codes to create text highlights, gradients, and ASCII borders with a glowing effect.

## Features
- Apply glow effect to text using ANSI colors (supports red, green, yellow, blue, purple).
- Create gradient text with changing colors.
- Add an ASCII glow border around text for emphasis.

## Installation

You can install the package using pip:

    pip install textglow

## Usage

### 1. Apply Glow to Text
Import the `apply_glow` function and pass the text and color:

    from textglow.glow import apply_glow
    print(apply_glow("Hello World", color="blue"))

### 2. Create Gradient Glow
Import the `gradient_glow` function and pass the text:

    from textglow.glow import gradient_glow
    print(gradient_glow("Hello Gradient!"))

### 3. Add ASCII Glow Border
Use `ascii_glow_border` to create a glow effect around text:

    from textglow.glow import ascii_glow_border
    print(ascii_glow_border("Glowing Border"))

## Running Tests
To run the unit tests, use the following command:

    python -m unittest discover
