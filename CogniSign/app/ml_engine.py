from ultralytics import YOLO
from flask import current_app
import cv2
import os
import subprocess
from flask import current_app

_model = None

def get_model():
    global _model
    if _model is None:
        model_path = current_app.config['MODEL_PATH']
        _model = YOLO(model_path)
    return _model

def detect_frame(frame):
    model = get_model()
    results = model.predict(frame, verbose=False)
    
    for result in results[0].boxes.data.tolist():
        x1, y1, x2, y2, conf, cls = result
        x1, y1, x2, y2 = map(int, (x1, y1, x2, y2))
        label = f"{model.names[int(cls)]} {conf:.2f}"

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
    return frame

def detect_image(file_path):
    model = get_model()
    results = model(file_path)
    # Return the annotated image
    return results[0].plot()

def process_video(input_path, filename):
    model = get_model()
    cap = cv2.VideoCapture(input_path)
    output_path = os.path.join(current_app.config['RESULTS_FOLDER'], f"result_{filename}")
    temp_output = os.path.join(current_app.config['RESULTS_FOLDER'], "temp_video.mp4")

    # Get video properties
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frame_size = (width, height)

    # Initialize VideoWriter for temp output
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(temp_output, fourcc, fps, frame_size)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Detection
        results = model(frame, verbose=False)
        annotated_frame = results[0].plot()
        out.write(annotated_frame)

    cap.release()
    out.release()

    # Convert to web-compatible format using FFmpeg
    # Note: Requires ffmpeg to be in system PATH
    ffmpeg_command = [
        "ffmpeg", "-y", "-i", temp_output, 
        "-c:v", "libx264", "-preset", "medium", 
        "-crf", "23", "-c:a", "aac", "-strict", "experimental",
        output_path
    ]

    try:
        subprocess.run(ffmpeg_command, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        print(f"FFmpeg failed or not found: {e}")
        # Fallback: rename temp to output
        if os.path.exists(temp_output):
            if os.path.exists(output_path): os.remove(output_path)
            os.rename(temp_output, output_path)
    
    # Cleanup temp file if it still exists
    if os.path.exists(temp_output):
        os.remove(temp_output)

    return f"result_{filename}"
