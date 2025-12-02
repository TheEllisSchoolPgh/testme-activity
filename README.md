# PyIDE - AI-Powered Browser Python Editor

**PyIDE** is a lightweight, single-file Python Integrated Development Environment that runs entirely in your web browser. It leverages **Pyodide** (WebAssembly) to execute Python code locally without a backend server, and features a context-aware **AI Tutor** to help you learn and debug.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.11%20(Pyodide)-yellow)
![Status](https://img.shields.io/badge/status-active-success)

## Features

*   **Serverless Execution**: Runs Python 3.x entirely in the browser using WebAssembly.
*   **Context-Aware AI Tutor**: Integrated Chat UI (compatible with OpenAI/Local LLMs) that can "see" your code and console output to provide relevant help.
*   **Data Science Ready**: Built-in support for **Matplotlib** plotting (renders directly in the console).
*   **Package Manager**: Install pure Python libraries (Pandas, NumPy, etc.) via `micropip` directly from the UI.
*   **Interactive Input**: Supports Python's `input()` function (requires specific server headers, see below).
*   **Modern UI**:
    *   Light/Dark Theme toggle (Dracula & Eclipse themes).
    *   Resizable Split-View (Editor vs. Console).
    *   Syntax Highlighting & Bracket Matching.

## How to Run (Important)

Because this project uses `SharedArrayBuffer` to handle Python's `input()` function synchronously, **you cannot simply double-click the .html file.** It must be served over `localhost` with specific security headers (COOP and COEP).

### Option 1: Using Python (Recommended)
This repository includes a helper script (`serve.py`) that sets up the local server with the correct headers for you.

1.  Make sure you have Python installed.
2.  Open your terminal or command prompt in this folder.
3.  Run the server:
    ```bash
    python serve.py
    ```
4.  Open your browser to `http://localhost:8000`.

### Option 2: Using Node.js / http-server
If you prefer Node.js, you can run a server with flags:
```bash
npx http-server . --port 8000 --cors -H='{"Cross-Origin-Opener-Policy": "same-origin", "Cross-Origin-Embedder-Policy": "require-corp"}'
```

*(Note: If you do not execute input() statements in your code, you can open the HTML file directly, but you may see warnings in the browser console.)*

## Configuring the AI Tutor

The AI sidebar allows you to chat with an LLM that knows the context of your current editor.

1.  Click the **"AI Tutor"** button in the toolbar to open the sidebar.
2.  Click the **Settings** icon in the sidebar header.
3.  Enter your API details:
    *   **API Endpoint**: Default is Google AI Studio (`https://generativelanguage.googleapis.com/v1beta/openai/chat/completions`). You can change this to a local server (e.g., LM Studio, Ollama) if it supports OpenAI-compatible endpoints.
    *   **API Key**: Your API key (stored in browser LocalStorage only).
    *   **Model Name**: e.g., `gemini-2.5-flash`, `gemini-3-pro-preview`, or a local model name.
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
*   **Markdown Rendering**: [Marked.js](https://marked.js.org/).
*   **Fonts**: Inter & JetBrains Mono (via Google Fonts).

## License

This project is open-source. Feel free to modify and distribute it for educational or personal use.