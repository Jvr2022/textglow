# TextGlow

TextGlow is a Python package that adds "glow" effects to text for terminal-based applications. It allows you to apply ANSI color codes to create text highlights, gradients, and ASCII borders with a glowing effect.

## Features
- Apply glow effect to text using ANSI colors (supports red, green, yellow, blue, purple).
- Create gradient text with changing colors.
- Add an ASCII glow border around text for emphasis.
- Simulate a flashing effect on text.
- Apply smooth gradient effects with a list of colors.
- Use custom ASCII characters for borders.
- Support multi-line texts with borders.

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

### 4. Flashing Glow
Simulate a flashing effect on text:

    from textglow.glow import flashing_glow
    flashing_glow("Flashing Text", color="green", times=5)

### 5. Smooth Gradient Glow
Create a smooth gradient glow effect with multiple colors:

    from textglow.glow import smooth_gradient_glow
    print(smooth_gradient_glow("Smooth Gradient", ['\033[91m', '\033[92m', '\033[94m']))

### 6. Custom ASCII Glow Border
Use custom characters for borders:

    from textglow.glow import custom_ascii_glow_border
    print(custom_ascii_glow_border("Custom Border", border_char='#'))

## Running Tests
To run the unit tests, use the following command:

    python -m unittest discover
