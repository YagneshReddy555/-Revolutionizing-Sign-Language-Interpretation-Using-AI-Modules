# CogniSign - Sign Language Interpretation

This is the refactored, modular version of the Sign Language Interpretation project.

## Structure

-   **`run_app.py`**: The entry point to start the server.
-   **`config.py`**: Configuration settings (secrets, paths).
-   **`app/`**: Main application package.
    -   `routes.py`: Handles web requests (Login, Signup, Upload).
    -   `models.py`: Database logic (User authentication).
    -   `ml_engine.py`: YOLOv8 model loading and inference.
    -   `camera.py`: Webcam handling logic.
-   **`data/`**: Stores the database (`app.db`) and ML models (`best.pt`).

## How to Run

1.  Open a terminal in this folder (`CogniSign`).
2.  Run the application:
    ```bash
    python run_app.py
    ```
3.  Open your browser to `http://127.0.0.1:5000`.

## Notes
-   The database was migrated from `Python.db` to `data/database/app.db`.
-   The model is loaded from `data/ml_models/best.pt`.
