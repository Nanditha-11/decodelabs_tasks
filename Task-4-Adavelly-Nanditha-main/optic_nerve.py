import os, sys, subprocess, urllib.request  # type: ignore
try:
    import cv2, numpy as np, pytesseract  # type: ignore
except ImportError as e:
    print(f"\n{'='*70}\n[!] Error: Missing dependency: {str(e).split()[-1]}\n{'='*70}\nPlease install: pip install opencv-python numpy pytesseract\n{'='*70}"); sys.exit(1)
try: import easyocr; EASYOCR_AVAILABLE = True  # type: ignore
except ImportError: EASYOCR_AVAILABLE = False

PROTOTXT_FILE, CAFFEMODEL_FILE = "MobileNetSSD_deploy.prototxt", "MobileNetSSD_deploy.caffemodel"
PROTOTXT_URL, CAFFEMODEL_URL = "https://raw.githubusercontent.com/chuanqi305/MobileNet-SSD/master/voc/MobileNetSSD_deploy.prototxt", "https://github.com/PINTO0309/MobileNet-SSD-RealSense/raw/master/caffemodel/MobileNetSSD/MobileNetSSD_deploy.caffemodel"
CLASSES = "background aeroplane bicycle bird boat bottle bus car cat chair cow diningtable dog horse motorbike person pottedplant sheep sofa train tvmonitor".split()
TESS_INST = "\033[91m[!] Tesseract OCR Engine was not found on your system.\033[0m\n" + "-" * 65 + "\nTo resolve this, you have two options:\nOption A (Recommended): Install Tesseract OCR binary globally:\n   1. Open PowerShell and run: \033[96mwinget install tesseract-ocr.tesseract\033[0m\n   2. Restart your terminal window after installation.\n\nOption B (Python-only alternative): Use EasyOCR (No binary install needed):\n   1. Open PowerShell and run: \033[96mpip install easyocr\033[0m\n" + "-" * 65

def configure_tesseract():
    try:
        subprocess.run(["tesseract", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True, "System PATH"
    except Exception: pass
    for p in [r"C:\Program Files\Tesseract-OCR\tesseract.exe", r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe", os.path.join(os.environ.get("USERPROFILE", ""), r"AppData\Local\Tesseract-OCR\tesseract.exe")]:
        if os.path.exists(p): pytesseract.pytesseract.tesseract_cmd = p; return True, p
    return False, None

def download_file(url, dest_path):
    print(f"Connecting to download {os.path.basename(dest_path)}...")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=30) as resp:
            total, downloaded = int(resp.info().get('Content-Length', 0)), 0
            with open(dest_path, 'wb') as f:
                while chunk := resp.read(8192):
                    f.write(chunk); downloaded += len(chunk)
                    if total > 0:
                        filled = int(round(30 * downloaded / total))
                        sys.stdout.write(f"\r[{'='*filled + '-'*(30-filled)}] {(downloaded/total)*100:.1f}% ({downloaded/1048576:.2f} MB / {total/1048576:.2f} MB)")
                    else: sys.stdout.write(f"\rDownloaded {downloaded/1048576:.2f} MB")
                    sys.stdout.flush()
        print(f"\n[OK] Saved to {dest_path}\n"); return True
    except Exception as e:
        print(f"\n[ERR] Failed to download {os.path.basename(dest_path)}: {e}")
        if os.path.exists(dest_path): os.remove(dest_path)
        return False

def check_and_download_models():
    print(f"\n{'='*60}\n           MobileNet-SSD Model Auto-Setup\n{'='*60}"); ok = True
    for fn, url in [(PROTOTXT_FILE, PROTOTXT_URL), (CAFFEMODEL_FILE, CAFFEMODEL_URL)]:
        if not os.path.exists(fn): print(f"[!] {fn} is missing."); ok = download_file(url, fn) and ok
        else: print(f"[OK] {fn} is already present.")
    print("=" * 60); return ok

def setup_samples():
    os.makedirs("samples", exist_ok=True)
    text_samples = [
        ("text_sample_1.png", -6.0, ["DECODELABS OPTIC NERVE", "Project 4: Image & Text Recognition", "This text is skewed to test the alignment algorithm.", "Otsu thresholding and Deskewing preprocess data.", "Validated Confidence target: 80% minimum."]),
        ("text_sample_2.png", 5.0, ["COMPUTER VISION PIPELINE", "Image processing enables machine intelligence", "to interpret high-dimensional visual data.", "OpenCV functions provide advanced filter matrices.", "Robust systems require clean preprocessing."])
    ]
    for fn, angle, lines in text_samples:
        dp = os.path.join("samples", fn)
        if not os.path.exists(dp):
            img = np.ones((400, 800, 3), dtype=np.uint8) * 255
            for i, ln in enumerate(lines):
                fs, th = (1.1, 3) if i == 0 else (0.7 if "-" in ln or "$" in ln else 0.75, 2)
                cv2.putText(img, ln, (50, 80 + i * 60), cv2.FONT_HERSHEY_SIMPLEX, fs, (129, 185, 16) if i == 0 else (20, 20, 20), th, cv2.LINE_AA)
            cv2.imwrite(dp, cv2.warpAffine(img, cv2.getRotationMatrix2D((400, 200), angle, 1.0), (800, 400), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_CONSTANT, borderValue=(255, 255, 255)))
            print(f"[OK] Created: {dp}")
    for fn, url in [("sample_objects.jpg", "https://raw.githubusercontent.com/pjreddie/darknet/master/data/dog.jpg"), ("sample_bird.jpg", "https://raw.githubusercontent.com/pjreddie/darknet/master/data/eagle.jpg")]:
        dp = os.path.join("samples", fn)
        if not os.path.exists(dp):
            try:
                req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req, timeout=15) as resp:
                    with open(dp, 'wb') as f: f.write(resp.read())
                print(f"[OK] Saved: {dp}")
            except Exception as e:
                print(f"[!] Warning: {fn} download failed: {e}. Creating placeholder...")
                img = np.ones((500, 500, 3), dtype=np.uint8) * 128; cv2.circle(img, (250, 250), 100, (0, 0, 255), -1); cv2.imwrite(dp, img)

def deskew_image(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) if len(img.shape) == 3 else img
    _, th = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    pts = np.column_stack(np.where(th > 0))
    if not len(pts): return img, 0.0
    ang = cv2.minAreaRect(pts)[-1]
    ang = -(90 + ang) if ang < -45 else -ang
    h, w = img.shape[:2]
    return cv2.warpAffine(img, cv2.getRotationMatrix2D((w//2, h//2), ang, 1.0), (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_CONSTANT, borderValue=(255, 255, 255)), ang

def print_banner():
    print("\033[92m" + "=" * 80)
    print(f"{'DECODELABS'.center(80)}")
    print(f"{'OPTIC NERVE - IMAGE & TEXT RECOGNITION'.center(80)}")
    print("=" * 80 + "\033[0m")

def run_diagnostics():
    print(f"\n{'-'*30} RUNNING DIAGNOSTICS {'-'*30}\n[OK] OpenCV: {cv2.__version__}\n[OK] NumPy: {np.__version__}")
    found, path = configure_tesseract()
    print(f"[OK] Tesseract OCR: FOUND (Location: {path})" if found else "[ERR] Tesseract OCR: NOT FOUND")
    if found:
        try: print(f"     Version: {pytesseract.get_tesseract_version()}")
        except Exception: print("     Warning: Unable to query Tesseract version string.")
    print(f"{'[OK] EasyOCR (PyTorch alternative): READY' if EASYOCR_AVAILABLE else '[WARN] EasyOCR not installed. Run: pip install easyocr'}")
    if not found and not EASYOCR_AVAILABLE: print(TESS_INST)
    proto, caffe = os.path.exists(PROTOTXT_FILE), os.path.exists(CAFFEMODEL_FILE)
    print(f"{'[OK] MobileNet-SSD Models: READY' if proto and caffe else '[ERR] MobileNet-SSD Models: MISSING'}")
    if not proto: print(f"      - Missing: {PROTOTXT_FILE}")
    if not caffe: print(f"      - Missing: {CAFFEMODEL_FILE}")
    print("-" * 81 + "\n")

def path_1_ocr():
    print(f"\n{'='*25} PATH 1: OCR ENGINE {'='*25}")
    tess_found, _ = configure_tesseract()
    if not tess_found and not EASYOCR_AVAILABLE: print(TESS_INST); return
    print("\nSelect a text image to analyze:\n  [1] samples/text_sample_1.png\n  [2] samples/text_sample_2.png\n  [3] Enter a custom image path")
    choice = input("Select an option (1-3) [Default: 1]: ").strip()
    img_path = os.path.join("samples", "text_sample_2.png") if choice == "2" else (input("Enter custom image path: ").strip().strip('"\'') if choice == "3" else os.path.join("samples", "text_sample_1.png"))
    if not os.path.exists(img_path): print(f"\033[91m[Error] File not found: {img_path}\033[0m"); return
    print(f"\n[1] Reading image: {img_path}")
    img = cv2.imread(img_path)
    if img is None: print("\033[91m[Error] Failed to read image.\033[0m"); return
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(cv2.GaussianBlur(gray, (5, 5), 0), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    rotated, _ = deskew_image(thresh)
    print("\nPage Segmentation Modes (PSM):\n  3 - Fully automatic page segmentation (Default)\n  6 - uniform block\n  7 - single line\n 11 - Sparse text")
    psm_input = input("Choose PSM (3, 6, 7, 11) [Default: 3]: ").strip()
    psm = int(psm_input) if psm_input in ["3", "6", "7", "11"] else 3
    if tess_found:
        print(f"\n[2] Ingesting final binary matrix into Google Tesseract OCR (PSM={psm})...")
        try:
            txt = pytesseract.image_to_string(rotated, config=f"--psm {psm}")
            print(f"\n{'-'*30} EXTRACTED MACHINE INTELLIGENCE (TESSERACT) {'-'*30}\n\033[94m{txt.strip()}\033[0m" if txt.strip() else "\033[93m[!] OCR returned no text.\033[0m")
        except Exception as e: print(f"\033[91m[Error] Tesseract failed: {e}\033[0m")
    else:
        print(f"\n[2] Tesseract not found. Ingesting final binary matrix into EasyOCR fallback...")
        try:
            reader = easyocr.Reader(['en'], gpu=False)  # type: ignore
            txt = "\n".join([r[1] for r in reader.readtext(rotated)])  # type: ignore
            print(f"\n{'-'*30} EXTRACTED MACHINE INTELLIGENCE (EASYOCR) {'-'*30}\n\033[94m{txt.strip()}\033[0m" if txt.strip() else "\033[93m[!] EasyOCR returned no text.\033[0m")
        except Exception as e: print(f"\033[91m[Error] EasyOCR failed: {e}\033[0m")
    print("-" * 92)

def path_2_detection():
    print(f"\n{'='*20} PATH 2: OBJECT DETECTION ENGINE {'='*20}")
    if not (os.path.exists(PROTOTXT_FILE) and os.path.exists(CAFFEMODEL_FILE)):
        print("\033[93m[!] MobileNet-SSD model files not found. Initiating auto-setup...\033[0m")
        if not check_and_download_models(): print("\033[91m[Error] Auto-setup failed.\033[0m"); return
    print("\nSelect an image to analyze:\n  [1] samples/sample_objects.jpg\n  [2] samples/sample_bird.jpg\n  [3] Enter a custom image path")
    choice = input("Select an option (1-3) [Default: 1]: ").strip()
    img_path = os.path.join("samples", "sample_bird.jpg") if choice == "2" else (input("Enter custom image path: ").strip().strip('"\'') if choice == "3" else os.path.join("samples", "sample_objects.jpg"))
    if not os.path.exists(img_path): print(f"\033[91m[Error] File not found: {img_path}\033[0m"); return
    try: thr = float(input("Enter confidence threshold (0.0 to 1.0) [Default: 0.80]: ").strip() or 0.80)
    except: thr = 0.80
    print(f"\n[1] Ingesting image: {img_path}")
    img = cv2.imread(img_path)
    if img is None: print("\033[91m[Error] Failed to read image.\033[0m"); return
    h, w = img.shape[:2]
    print("[2] Loading pre-trained MobileNet-SSD Caffe network...\n[3] Step 1: Pre-Processing image into a 4D Blob...\n[4] Step 2: Running inference...\n[5] Step 3: Filtering candidates...")
    net = cv2.dnn.readNetFromCaffe(PROTOTXT_FILE, CAFFEMODEL_FILE)
    net.setInput(cv2.dnn.blobFromImage(img, 0.007843, (300, 300), 127.5))
    detections = net.forward()
    print("[5] Step 3: Filtering candidates and rendering bounding boxes...")
    detected, ann = [], img.copy()
    for i in range(detections.shape[2]):
        conf = detections[0, 0, i, 2]
        if conf >= thr:
            c_name = CLASSES[int(detections[0, 0, i, 1])]
            bx = (detections[0, 0, i, 3:7] * np.array([w, h, w, h])).astype("int")
            sx, sy, ex, ey = max(0, bx[0]), max(0, bx[1]), min(w, bx[2]), min(h, bx[3])
            detected.append({"class": c_name, "confidence": conf, "box": (sx, sy, ex - sx, ey - sy)})
            color = (129, 185, 16) if c_name == "person" else (246, 130, 59)
            cv2.rectangle(ann, (sx, sy), (ex, ey), color, 2)
            cv2.putText(ann, f"{c_name.upper()}: {conf*100:.1f}%", (sx, sy - 10 if sy - 10 > 10 else sy + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2, cv2.LINE_AA)
    print(f"\n{'-'*75}\n| {'Object Detected':<15} | {'Confidence Score':<18} | {'Bounding Box (X, Y, W, H)':<32} |\n{'-'*75}")
    if detected:
        for o in detected:
            bx, by, bw, bh = o["box"]
            c_str, b_str = f"{o['confidence']*100:.2f}%", f"({bx}, {by}, {bw}, {bh})"
            print(f"| {o['class'].upper():<15} | {c_str:<18} | {b_str:<32} |")
    else: print(f"| {'NO OBJECTS DETECTED ABOVE CONFIDENCE THRESHOLD':^71} |")
    print(f"{'-'*75}\n\n[OK] Visual Confirmation: Annotated output saved to [./output_detection.jpg]")
    cv2.imwrite("output_detection.jpg", ann)

def main():
    configure_tesseract()
    if not (os.path.exists(PROTOTXT_FILE) and os.path.exists(CAFFEMODEL_FILE)):
        print("\033[93m[!] Pre-trained MobileNet-SSD models not found. Initiating auto-setup...\033[0m")
        check_and_download_models()
    setup_samples()
    while True:
        print_banner()
        print("  [1] Path 1: Optical Character Recognition (OCR)\n  [2] Path 2: Object Detection (MobileNet-SSD)\n  [3] Run Diagnostics Check & Auto-Setup\n  [4] Exit\n" + "=" * 65)
        choice = input("Select an option (1-4): ").strip()
        if choice == "1": path_1_ocr()
        elif choice == "2": path_2_detection()
        elif choice == "3": check_and_download_models(); setup_samples(); run_diagnostics()
        elif choice == "4": print("\nExiting Optic Nerve Pipeline. Happy Engineering!"); break
        else: print("\033[91mInvalid selection. Please choose a number from 1 to 4.\033[0m")
        input("\nPress Enter to return to the main menu...")
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()
