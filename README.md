# PyIDE - AI-Powered Browser Python Editor

**PyIDE** is a lightweight, single-file Python Integrated Development Environment that runs entirely in your web browser. It leverages **Pyodide** (WebAssembly) to execute Python code locally without a backend server, and features a context-aware **AI Tutor** to help you learn and debug.

![Python](https://img.shields.io/badge/python-3.11%20(Pyodide)-yellow)
![Status](https://img.shields.io/badge/status-active-success)

## Features

*   **Serverless Execution**: Runs Python 3.x entirely in the browser using WebAssembly.
*   **Context-Aware AI Tutor**: Integrated Chat UI (compatible with OpenAI/Local LLMs) that can "see" your code and console output to provide relevant help.
*   **Data Science Ready**: Built-in support for **Matplotlib** plotting (renders directly in the console).
*   **Package Manager**: Install pure Python libraries (Pandas, NumPy, etc.) via `micropip` directly from the UI.
*   **Interactive Input**: Supports Python's `input()` function via `SharedArrayBuffer` and a Service Worker integration.
*   **Modern UI**:
    *   Light/Dark Theme toggle (Dracula & Eclipse themes).
    *   Resizable Split-View (Editor vs. Console).
    *   Syntax Highlighting & Bracket Matching.

## How to Run

To enable features like Python's `input()` function, this project uses a Service Worker to manage browser security requirements (`SharedArrayBuffer`). Service Workers **requires a web server** to function; they will not work if you simply double-click the `index.html` file.

You can use any static file server. Here are the easiest ways to get started:


### Option 1: Standard Python Server
If you prefer not to use the helper script, you can use Python's built-in module:

```bash
python -m http.server 8000
```

### Option 2: Node.js
If you have Node.js installed:

```bash
npx http-server . -p 8000
```

### Note on "file://" Access
If you open `index.html` directly from your file explorer (the URL starts with `file://`), the editor will load, but **interactive input and the AI tutor may fail** because browsers block Service Workers in this mode. Always serve via localhost.

## Configuring the AI Tutor

The AI sidebar allows you to chat with an LLM that knows the context of your current editor.

1.  Click the **AI Tutor** button in the toolbar to open the sidebar.
2.  Click the **Settings** icon in the sidebar header.
3.  Enter your API details:
    *   **API Endpoint**: Default is OpenAI (`https://api.openai.com/v1/chat/completions`). You can change this to a local server (e.g., LM Studio, Ollama) if it supports OpenAI-compatible endpoints.
    *   **API Key**: Your API key (stored in browser LocalStorage only).
    *   **Model Name**: e.g., `gpt-3.5-turbo`, `gpt-4`, or a local model name.
4.  Click **Save & Close**.

## Installing Packages

PyIDE supports installing Python packages that are pure Python or have wheels built for Pyodide (including NumPy, Pandas, Scipy, Matplotlib).

1.  Click the **Packages** button.
2.  Type the package names (one per line or separated by commas).
    *   *Example:* `numpy, pandas`
3.  Click **Install**.
4.  Wait for the "Packages installed" message in the console.

## Plotting Example

To test the plotting capabilities, run this code:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(5, 3))
plt.plot(x, y, label='Sine Wave', color='purple')
plt.title("PyIDE Plotting Demo")
plt.legend()
plt.grid(True)
plt.show() # This triggers the render in the console
```

## Tech Stack

*   **Core**: HTML5, CSS3, Vanilla JavaScript (ES6+).
*   **Python Engine**: [Pyodide](https://pyodide.org/) (v0.23.4).
*   **Editor**: [CodeMirror 5](https://codemirror.net/5/).
*   **Isolation**: [coi-serviceworker](https://github.com/gzuidhof/coi-serviceworker) (enables SharedArrayBuffer without strict server config).
*   **Markdown Rendering**: [Marked.js](https://marked.js.org/).

## License

This project is open-source. Feel free to modify and distribute it for educational or personal use.
