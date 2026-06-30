# DecodeLabs Optic Nerve — Project 4
**Project Name:** Image & Text Recognition (Optic Nerve)

---

## 📌 Project Overview
This project is part of the **DecodeLabs Industrial Training program (Project 4)**.

It implements a terminal-based computer vision application ("Optic Nerve") consolidated into a single Python script. The application supports two distinct execution paths: Path 1 performs Optical Character Recognition (OCR) with full image preprocessing (grayscale, blur, Otsu thresholding, and deskewing), while Path 2 runs deep learning object detection using a pre-trained Caffe MobileNet-SSD network. Additionally, the tool includes auto-setup downloaders and diagnostic scripts to ensure all native binary engines and libraries are configured correctly.

---

## ⚙️ Features
1. **Interactive CLI Dashboard**: Runs entirely in the terminal with a custom ASCII banner and structured choice menus.
2. **Comprehensive Preprocessing (Path 1)**: Transforms text images through Grayscale, Gaussian Blur, Otsu's Thresholding, and Deskewing algorithms to clean pixel arrays.
3. **Dual OCR Engine**: Leverages Google Tesseract OCR with automatic binary path discovery on Windows, falling back to EasyOCR (PyTorch) if Tesseract is not installed globally.
4. **Neural Network Object Detection (Path 2)**: Translates images into normalized 4D Blobs and evaluates object classes using Caffe MobileNet-SSD.
5. **80% Confidence Gatekeeper**: Dynamically filters detected classes against a user-defined threshold, highlighting standard DecodeLabs gatekeeper standards.
6. **Tabular & Annotated Output**: Renders a clean coordinates table in the terminal and outputs the annotated bounding box image to `output_detection.jpg`.
7. **Diagnostics & Auto-Setup**: Verifies environment dependencies and automatically downloads missing Caffe model files and media samples.

---

## 📁 File Structure
```text
C:\Users\nandi\Documents\AI Project 4\
├── optic_nerve.py                 # Core CLI script containing the entire application
├── MobileNetSSD_deploy.prototxt   # Caffe model definition (auto-downloaded)
├── MobileNetSSD_deploy.caffemodel # Caffe model weights (auto-downloaded)
├── output_detection.jpg           # Annotated output image from object detection
└── samples/                       # Pre-packaged and generated testing media
    ├── text_sample_1.png          # Skewed sample image 1 (-6 degrees)
    ├── text_sample_2.png          # Skewed sample image 2 (5 degrees)
    ├── sample_objects.jpg         # Multi-class object sample image
    └── sample_bird.jpg            # Bird sample image
```

---

## 🚀 How to Run the Image & Text Recognition System

Make sure you have `opencv-python`, `numpy`, and `pytesseract` installed.

1. Open your terminal or Command Prompt in the project directory.
2. Run the application:
   ```bash
   python optic_nerve.py
   ```

---

## 📊 Execution Phase Details

The steps executed sequentially by the system are detailed below:

| Execution Phase | Step & Implementation | Detail / Metrics |
|---|---|---|
| **1. Model Setup** | Caffe Network Download | Validates and programmatically downloads `MobileNetSSD_deploy.prototxt` (29 KB) and `MobileNetSSD_deploy.caffemodel` (23 MB) from repository URLs if missing. |
| **2. Media Generation** | Testing Samples Creation | Generates synthetic skewed text sample pngs (`-6.0` and `5.0` degrees) and downloads test images for object recognition. |
| **3. Interactive Loop** | Dashboard Menu | Displays the custom `DECODELABS - AI INDUSTRIAL TRAINING KIT` ASCII banner and prompts for option `1-4`. |
| **4. Path 1: Preprocess** | Image Enhancement (OCR) | Ingests text image, applies Gray Conversion, Gaussian Blur, Otsu's Thresholding, and Deskewing (rotation correction). |
| **5. Path 1: Extraction** | OCR Engine Run | Runs Google Tesseract OCR (with EasyOCR fallback) using custom Page Segmentation Modes (PSM `3`, `6`, `7`, `11`). |
| **6. Path 2: Inference** | Neural Network Run | Scales image by `0.007843`, subtracts `127.5` mean, runs forward pass through MobileNet-SSD, and filters detections with a default `0.80` gatekeeper threshold. |
| **7. Path 2: Output** | Console Table & Saved Image | Renders an ASCII table showing Detected Classes, Confidence Scores, and Box Offsets `(X,Y,W,H)`. Saves annotated file to `output_detection.jpg`. |
| **8. Diagnostics** | Dependency Check | Evaluates versions of OpenCV, NumPy, EasyOCR presence, and Tesseract binary PATH discovery status. |
