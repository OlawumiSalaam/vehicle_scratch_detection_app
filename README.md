
# 🚗 AutoScratchAI – Vehicle Scratch Detection Web App

AutoScratchAI is a simple and responsive Flask web application that allows users to upload images of vehicles and automatically detects visible **scratches** using a custom-trained [YOLOv8](https://github.com/ultralytics/ultralytics) object detection model.


## 📸 Demo

![Result Page](static\Flask_deployment.png)


## 📁 Project Structure
```text

vehicle_scratch_detection_app/
│
├── app.py                 
├── model/
│   └── best.pt            
├── static/
│   ├── css/
│   │   └── style.css      
│   └── uploads/           
├── templates/
│   ├── index.html         
│   └── result.html        
├── requirements.txt      
└── README.md
```
## 🧠 Approach

1. **Model Training**
   - YOLOv8 was trained to detect a single class: `scratch`.
   - Input data consisted of vehicle images labeled using COCO format, then converted to YOLO format.
   - All non-scratch images were labeled as `no_damage` to avoid false positives.

2. **Web App Development**
   - Flask was used to serve a two-page web interface: image upload and results.
   - TailwindCSS ensures the UI is responsive and visually appealing.
   - The app:
     - Accepts an image from the user.
     - Runs the YOLOv8 model on it.
     - Displays both the original and annotated output side-by-side.
## Run Locally

Clone the project

```bash
  git clone https://github.com/OlawumiSalaam/vehicle_scratch_detection_app.git
```

Go to the project directory

```bash
  cd vehicle_scratch_detector
```
Create Virtual Environment

```bash
  python -m venv venv
  source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Run the Flask App

```bash
 run python app
```
Then open your browser and navigate to:
👉 http://127.0.0.1:5000

## License

📩 License
This project is built as part of a technical assessment and is for educational/demo purposes only.)


## Authors

Olawumi Salaam

ML Engineer • Open Source Contributor

- [LinkedIn](https://www.linkedin.com/in/olawumisalaam)


