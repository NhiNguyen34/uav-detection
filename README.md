<<<<<<< HEAD
# uav-detection
This repository provides checkpoints for YOLOv8, RT-DETR, and YOLOv10 models, each fine-tuned on the VisDrone dataset. These models are optimized specifically for detecting UAV (Unmanned Aerial Vehicle) images.
=======
# visdrone-detection

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

A short description of the project.

## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── demo
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see mkdocs.org for details
│
├── uav_models             <- Trained and serialized models, model predictions, or model summaries
│
│             
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in 
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
```


## Models

### YOLOv8
YOLOv8 is a state-of-the-art object detection model that offers high accuracy and speed. It is used in this project for vehicle detection tasks.

### RT-DETR
RT-DETR (Real-Time Detection Transformer) is another powerful model utilized for object detection. It leverages transformer architecture to enhance detection capabilities, providing robust results in real-time scenarios.

### YOLOv10
YOLOv10 is an advanced version of the YOLO series models, offering improved performance and accuracy. It is included in this project to explore its effectiveness in vehicle detection.

## Setup Instructions

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/visdrone-detection.git
    cd visdrone-detection
    ```

2. **Create and activate the conda environment**:

    ### On Linux/macOS:
    
    ```bash
    # Check for conda installation
    if ! command -v conda &> /dev/null
    then
        echo "conda could not be found. Please install Anaconda or Miniconda first."
        exit
    fi

    # Create a new conda environment
    conda create --name visdrone-det python=3.10 -y

    # Activate the environment
    source activate visdrone-det

    # Install dependencies
    pip install -r requirements.txt

    # Create necessary folders
    mkdir -p checkpoints
    mkdir -p demo

    echo "Setup complete. Please place your model checkpoints in the 'checkpoints' folder and your demo images in the 'demo' folder."
    ```

    ### On Windows:
    
    ```bat
    @echo off

    :: Check for conda installation
    where conda >nul 2>nul
    if %errorlevel% neq 0 (
        echo "conda could not be found. Please install Anaconda or Miniconda first."
        exit /b
    )

    :: Create a new conda environment
    conda create --name visdrone-det python=3.10 -y

    :: Activate the environment
    call conda activate visdrone-det

    :: Install dependencies
    pip install -r requirements.txt

    :: Create necessary folders
    mkdir checkpoints
    mkdir demo

    echo Setup complete. Please place your model checkpoints in the 'checkpoints' folder and your demo images in the 'demo' folder.
    ```

3. **Save the model checkpoint**:
    Download your model checkpoint and save it in the `checkpoints` folder. Ensure the file is named appropriately, e.g., `4epoch-rtdetr-best.pt`.

4. **Run the model**:
    ```bash
    python run.py --model_path checkpoints/4epoch-rtdetr-best.pt --image_path demo/demo-uav.jpg --model_detect Yolov8
    ```

## References

- YOLOv8 Documentation: [YOLOv8 GitHub](https://github.com/ultralytics/yolov8)
- RT-DETR Paper: [Real-Time Detection Transformer](https://arxiv.org/abs/2101.11781)
- YOLOv10 Documentation: [YOLOv10 GitHub](https://github.com/ultralytics/yolov10)
>>>>>>> master
