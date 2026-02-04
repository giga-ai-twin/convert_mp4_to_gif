# 🎥 MP4 to GIF Converter

A lightweight, efficient Python CLI tool to convert video clips into optimized GIFs.  
Perfect for creating quick demos, memes, or progress updates for Slack/Discord.

> **Key Features:** Auto-trimming, 3x speed-up, and resolution optimization.

---

## ✨ Features

* **⚡ Smart Trimming**: Automatically captures a 20-second segment (default) from your specified start time.
* **⏩ Time-Lapse Effect**: Accelerates the video by **3x speed** for a snappy viewing experience.
* **📉 Size Optimization**: Resizes output to **50% scale** to keep file sizes manageable without losing context.
* **🛡️ Error Handling**: Intelligent checks for start times to prevent crashes if the video is too short.

---

## 📂 Project Structure

```text
.
├── convert_mp4_to_gif.py   # Main script
├── requirements.txt        # Dependencies
├── .gitignore              # Ignored files (videos/gifs)
├── LICENSE                 # MIT License
└── README.md               # Documentation
```

---

## 🚀 Installation

1. **Clone the repository**
```bash
git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
cd YOUR_REPO_NAME

```

2. **Install dependencies**
Make sure you have Python 3.x installed.
```bash
pip install -r requirements.txt

```



---

## 💻 Usage

Run the script from your terminal.

### 1. Basic Conversion (Default)

Starts from `0s` (the beginning) and captures the first 20 seconds.

```bash
python convert_mp4_to_gif.py input_video.mp4

```

### 2. Specify Start Time

Start capturing from a specific timestamp (e.g., 10 seconds in).

```bash
python convert_mp4_to_gif.py input_video.mp4 10

```

> **Note:** The output file will be saved in the same directory with the `.gif` extension (e.g., `input_video.gif`).

---

## ⚙️ Configuration

You can easily customize the behavior by editing the constants at the top of `convert_mp4_to_gif.py`:
```python
CLIP_DURATION = 20.0  # Change duration (seconds)
```

To change the **speed** or **resize factor**, modify this section in the `convert_to_gif` function:
```python
new_clip = (clip
    .subclipped(start_time, end_time)
    .resized(0.5)                  # Change 0.5 to 1.0 for original size
    .with_effects([MultiplySpeed(3)])  # Change 3 to 1 for normal speed
)
```

---

## 📝 Requirements

* Python 3.6+
* moviepy

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](https://www.google.com/search?q=LICENSE) file for details.

```
