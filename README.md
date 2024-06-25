# uav-detection

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

This repository provides checkpoints for YOLOv8, RT-DETR, and YOLOv10 models, each fine-tuned on the VisDrone dataset. These models are optimized specifically for detecting UAV (Unmanned Aerial Vehicle) images.

## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── README.md          <- The top-level README for developers using this project.
├── demo
│
├── docs               <- A default mkdocs project; see mkdocs.org for details
│
├── uav_models         <- Trained and serialized models, model predictions, or model summaries
│
│             
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in 
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
                          generated with `pip freeze > requirements.txt`
```


## Models

- YOLOv8: YOLOv8 is a state-of-the-art object detection model that offers high accuracy and speed. It is used in this project for vehicle detection tasks.

- RT-DETR: RT-DETR (Real-Time Detection Transformer) is another powerful model utilized for object detection. It leverages transformer architecture to enhance detection capabilities, providing robust results in real-time scenarios.

- YOLOv10: YOLOv10 is an advanced version of the YOLO series models, offering improved performance and accuracy. It is included in this project to explore its effectiveness in vehicle detection.

## Setup Instructions

1. **Clone the repository**:
    ```bash
    git clone https://github.com/NhiNguyen34/uav-detection.git
    cd uav-detection
    ```

2. **Create and activate the conda environment**:

    ### On Linux/macOS:
    
    ```bash
    # Create a new conda environment
    conda create --name visdrone-det python=3.10 -y

    # Activate the environment
    source activate visdrone-det

    # Install dependencies
    pip install -r requirements.txt

    echo "Setup complete. Please place your model checkpoints in the 'checkpoints' folder and your demo images in the 'demo' folder."
    ```

    ### On Windows:
    
    ```bat

    :: Create a new conda environment
    conda create --name visdrone-det python=3.10 -y

    :: Activate the environment
    conda activate visdrone-det

    :: Install dependencies
    pip install -r requirements.txt

    echo Setup complete. Please place your model checkpoints in the 'checkpoints' folder and your demo images in the 'demo' folder.
    ```

3. **Save the model checkpoint**:
    Download your model checkpoint and save it in the `checkpoints` folder. Ensure the file is named appropriately, e.g., `4epoch-rtdetr-best.pt`.

4. **Run the model**:
    ```bash
    python run.py --model_path checkpoints/your_model_checkpoint.pt --image_path demo/your_image.jpg --model_detect "your_model" 
    ```

## References

- YOLOv8 Documentation: [YOLOv8 GitHub](https://github.com/ultralytics/ultralytics)
- RT-DETR Paper: [Real-Time Detection Transformer](https://arxiv.org/pdf/2304.08069)
- YOLOv10 Documentation: [YOLOv10 GitHub](https://github.com/THU-MIG/yolov10)
