import colorsys
import time
from typing import List

def apply_glow(text: str, color: str = 'red') -> str:
    """Applies a 'glow' effect to the text by wrapping it with ANSI color codes."""
    ansi_colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'purple': '\033[95m',
    }
    reset = '\033[0m'
    glow_color = ansi_colors.get(color.lower(), '\033[91m')  # Defaults to red if color is not found
    
    return f"{glow_color}{text}{reset}"

def gradient_glow(text: str) -> str:
    """Applies a gradient glow effect by cycling through multiple colors."""
    colors = ['\033[91m', '\033[93m', '\033[92m', '\033[94m', '\033[95m']
    reset = '\033[0m'
    
    glowing_text = ""
    for i, char in enumerate(text):
        color = colors[i % len(colors)]
        glowing_text += f"{color}{char}"
    
    return f"{glowing_text}{reset}"

def ascii_glow_border(text: str) -> str:
    """Creates an ASCII border around the text with a glowing effect."""
    border = "*" * (len(text) + 4)
    return f"\033[93m{border}\n* {text} *\n{border}\033[0m"

def flashing_glow(text: str, color: str = 'red', times: int = 5) -> None:
    """Simulates a flashing effect on the text by making it blink."""
    ansi_colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'purple': '\033[95m',
    }
    reset = '\033[0m'
    glow_color = ansi_colors.get(color.lower(), '\033[91m')
    
    for _ in range(times):
        print(f"{glow_color}{text}{reset}", end='\r')
        time.sleep(0.5)
        print(' ' * len(text), end='\r')
        time.sleep(0.5)
    print(' ' * len(text))  # Clear the line

def smooth_gradient_glow(text: str, colors: List[str]) -> str:
    """Applies a smooth gradient glow effect with a list of colors."""
    reset = '\033[0m'
    gradient_text = ""
    color_count = len(colors)
    
    for i, char in enumerate(text):
        color = colors[i % color_count]
        gradient_text += f"{color}{char}"
    
    return f"{gradient_text}{reset}"

def custom_ascii_glow_border(text: str, border_char: str = '*') -> str:
    """Creates a custom ASCII border around the text with a glowing effect."""
    border = border_char * (len(text) + 4)
    return f"\033[93m{border}\n{border_char} {text} {border_char}\n{border}\033[0m"
