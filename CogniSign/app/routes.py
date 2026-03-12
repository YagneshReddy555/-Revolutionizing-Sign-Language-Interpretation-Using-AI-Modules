import os
from flask import Blueprint, render_template, request, redirect, url_for, session, send_from_directory, Response, current_app
from werkzeug.utils import secure_filename
import cv2
from .models import create_user, get_user, get_all_users
from .camera import video_camera
from .ml_engine import detect_image, process_video

bp = Blueprint('main', __name__)
# ... (lines between) ...

    if file:
        filename = secure_filename(file.filename)
        upload_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        file.save(upload_path)

        # Basic Check: Image vs Video
        if filename.lower().endswith(('.mp4', '.avi', '.mov', '.mkv')):
            # Video processing
            result_video_filename = process_video(upload_path, filename)
            
            return render_template('image.html', 
                                   original_file=filename, 
                                   result_video=result_video_filename)
        else:
            # Image processing
            results_path = os.path.join(current_app.config['RESULTS_FOLDER'], f"result_{filename}")
            annotated_img = detect_image(upload_path)
            cv2.imwrite(results_path, annotated_img)
            
            return render_template('image.html', 
                                   original_file=filename, 
                                   result_file=f"result_{filename}")

@bp.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(current_app.config['UPLOAD_FOLDER'], filename)

@bp.route('/results/<filename>')
def result_file(filename):
    return send_from_directory(current_app.config['RESULTS_FOLDER'], filename)

@bp.route('/video_feed')
def video_feed():
    return Response(video_camera.generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@bp.route('/close_camera', methods=['POST'])
def close_camera():
    video_camera.close()
    return '', 204

@bp.route('/camera')
def camera_page():
    return render_template('camera.html')

@bp.route("/details")
def details():
    if 'email' not in session:
        return redirect('/login')
    
    users = get_all_users()
    return render_template('details.html', result=users)
