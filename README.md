# 🤟 Revolutionizing Sign Language Interpretation Using AI Modules

A web-based **Sign Language Detection and Interpretation** system powered by **YOLOv8** deep learning model. This application enables real-time sign language recognition through image uploads, video processing, and live camera feeds — bridging the communication gap between hearing and hearing-impaired communities.

---

## ✨ Features

- 🔐 **User Authentication** — Signup & Login system with SQLite database
- 🖼️ **Image Detection** — Upload an image to detect and annotate sign language gestures
- 🎥 **Video Processing** — Upload a video file for frame-by-frame sign language detection with FFmpeg conversion
- 📸 **Live Camera Feed** — Real-time sign language detection using your webcam
- 📊 **Performance Dashboard** — View model training metrics (F1 curve, PR curve, confusion matrix)
- 📈 **Charts & Analytics** — Visual analytics with training batch samples and validation results

---

## 🧠 Model Details

| Property | Details |
|---|---|
| **Architecture** | YOLOv8 (Ultralytics) |
| **Dataset** | CogniSign v2 — 3,625 images from [Roboflow](https://universe.roboflow.com/bnm-3bjls/cognisign/dataset/2) |
| **Classes** | 40 sign language gestures |
| **Input Size** | 640×640 |
| **Format** | YOLOv8 annotation format |

### Supported Signs (40 Classes)
`After`, `Again`, `Against`, `Age`, `All`, `Also`, `And`, `Ask`, `At`, `Eat`, `Engineer`, `Fight`, `From`, `Glitter`, `Go`, `God`, `Good`, `Great`, `Happy`, `Her`, `His`, `Home`, `Invent`, `Language`, `Learn`, `Me`, `Word`, `Work`, `You`, `finish`, `hand`, `what`, `when`, `where`, `which`, `whole`, `whose`, `why`, `will`, `with`

---

## 🛠️ Tech Stack

- **Backend** — Python, Flask
- **ML Model** — YOLOv8 (Ultralytics)
- **Computer Vision** — OpenCV
- **Database** — SQLite
- **Frontend** — HTML, CSS, JavaScript, Bootstrap
- **Video Processing** — FFmpeg

---

## 📁 Project Structure

```
SIGN_LANGUAGE_MAIN_CODE/
├── app.py                  # Main Flask application
├── run.py                  # Alternative entry point
├── data.yaml               # YOLO dataset configuration
├── templates/              # HTML templates
│   ├── index.html          # Landing page
│   ├── login.html          # Login page
│   ├── signup.html         # Signup page
│   ├── home.html           # Dashboard
│   ├── image.html          # Image detection results
│   ├── video.html          # Video detection page
│   ├── camera.html         # Live camera feed
│   ├── performance.html    # Model performance metrics
│   └── charts.html         # Analytics charts
├── static/                 # CSS, JS, fonts, images
├── CogniSign/              # Modular refactored version
│   ├── app/
│   │   ├── routes.py       # Web request handlers
│   │   ├── models.py       # Database models
│   │   ├── ml_engine.py    # YOLO model inference
│   │   └── camera.py       # Webcam handler
│   └── run_app.py          # CogniSign entry point
└── config/                 # Audio-to-Sign-Language converter
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- FFmpeg (for video processing)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YagneshReddy555/-Revolutionizing-Sign-Language-Interpretation-Using-AI-Modules.git
   cd -Revolutionizing-Sign-Language-Interpretation-Using-AI-Modules
   ```

2. **Download large files from Google Drive**
   > ⚠️ The datasets, model weights, and static assets are too large for GitHub.
   > Download them from the link below and place them in the project root directory.

   📥 **[Download Large Files from Google Drive](https://drive.google.com/drive/folders/1zqZEj4_NdFm0dlqq6ji1-6PefrNVMPUC?usp=drive_link)**

   This includes:
   | File/Folder | Size | Description |
   |---|---|---|
   | `train/` | 108 MB | Training dataset (images + labels) |
   | `valid/` | 11 MB | Validation dataset |
   | `test/` | 6 MB | Test dataset |
   | `best.pt` | 6 MB | Trained YOLOv8 model weights |
   | `yolov8n.pt` | 6 MB | Pretrained YOLOv8 nano weights |
   | `runs/` | 41 MB | YOLO training runs & logs |
   | `static/images/` | 2,610 MB | Static image assets |
   | `CogniSign/app/static/` | 2,646 MB | CogniSign static assets |
   | `CogniSign/data/` | 12 MB | CogniSign database & models |
   | `config/` | 15 MB | Audio-to-Sign-Language converter |
   | `runs.rar` | 38 MB | Archived training runs |

3. **Create and activate virtual environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate        # Windows
   source .venv/bin/activate     # macOS/Linux
   ```

4. **Install dependencies**
   ```bash
   pip install flask ultralytics opencv-python werkzeug
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Open your browser**
   ```
   http://127.0.0.1:5000
   ```

---

## 📊 Dataset

The dataset was sourced from [Roboflow](https://universe.roboflow.com/bnm-3bjls/cognisign/dataset/2) and includes:
- **3,625 annotated images** in YOLOv8 format
- **Pre-processing**: Auto-orientation, resized to 640×640
- **Augmentation**: Horizontal flip (50%), brightness adjustment (±25%), exposure adjustment (±25%), salt & pepper noise (1%)
- **License**: CC BY 4.0

---



## 👨‍💻 Authors

- **Yagnesh Reddy** — [GitHub](https://github.com/YagneshReddy555)
