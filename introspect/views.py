from django.shortcuts import render, redirect
from django.http import HttpResponse, StreamingHttpResponse
from pymongo import MongoClient
from datetime import datetime
from ultralytics import YOLO
import cv2

# Import MongoDB connection
from myproject.db_connect import get_db_connection



# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['login']  # Database name
collection = db['logindata']  # Collection name
collegename="kumaraguru college of technology"

# View for login
def index(request):
    return render(request, 'templates/index.html')

def login(request):
    if request.method == 'POST':
        aicte_id = request.POST['aicte_id']
        college_name = request.POST['college_name']
        password = request.POST['password']

        # Connect to MongoDB
        db = get_db_connection()
        collection = db['logindata']  # Collection where credentials are stored

        # Verify credentials
        user = collection.find_one({
            'aicte_id': aicte_id,
            'college_name': college_name,
            'password': password
        })

        if user:
            # If user is found, you can redirect to a success page
            return redirect('home')
        else:
            # If user is not found
            return HttpResponse("Invalid credentials. Please try again.")
    else:
        return render(request, 'templates/login.html')

def home(request):
    return render(request, 'templates/home.html')

def terms(request):
    return render(request, 'templates/cond.html')

def procedure(request):
    return render(request, 'templates/procedure.html')

def inspection(request):
    return render(request, 'templates/inspection.html')

def certificate_verification(request):
    return render(request, 'templates/certificate_verification.html')

def classroom_inspection(request):
    # Open the laptop camera (0 is the default camera index)
    cap = cv2.VideoCapture(0)

    # Set confidence threshold for detection
    conf_threshold = 0.5

    while True:
        ret, frame = cap.read()  # Read frame from the laptop camera
        if not ret:
            print("Failed to grab frame")
            break

        # Perform object detection
        results = model.predict(source=frame, show=False, conf=conf_threshold)

        # Prepare a list to hold detection records
        detection_records = []

        # Iterate through results and extract relevant information
        for r in results:
            boxes = r.boxes.xyxy  # Bounding box coordinates
            probs = r.boxes.conf  # Confidence scores
            class_ids = r.boxes.cls  # Class indices

            # Store each detection result
            for box, prob, class_id in zip(boxes, probs, class_ids):
                class_name = class_names[int(class_id)]  # Get class name
                detection_record = {
                    'class_name': class_name,
                    
                    'timestamp': datetime.now()
                }
                detection_records.append(detection_record)

        # Update the existing document for the college name
        collection.update_one(
            {'college_name': collegename},
            {'$set': {'detection': detection_records}}  # Store the detection records
        )

        # Log detected classes to the console (optional)
        for record in detection_records:
            print(f'Detected: {record["class_name"]} with confidence {record["confidence"]:.2f}')

        # Stop after one frame (or remove this condition to continuously inspect frames)
        break

    # Release the laptop camera
    cap.release()

    return render(request, 'templates/classroom_inspection.html', {
        'message': 'Object detection completed and results stored in MongoDB!'
    })


    

def faculty_credentials(request):
    return render(request, 'templates/Faculty_credentials.html')

def infrastructure_inspection(request):
    return render(request, 'templates/infrastructure_inspection.html')

def washroom_inspection(request):
    return render(request, 'templates/washroom_inspection.html')

def safety_measure(request):
    return render(request, 'templates/safety_measure.html')

def inspection_end(request):
    return render(request, 'templates/inspection_end.html')

# Function to stream video and handle YOLOv8 detection IT ALWAYS