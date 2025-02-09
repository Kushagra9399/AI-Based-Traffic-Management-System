from roboflow import Roboflow

# Initialize the Roboflow API with your API key
rf = Roboflow(api_key="API KEY")

# Choose your workspace and project name (replace these with your actual workspace and project name)
workspace = "YOUR_WORKSPACE_NAME"
project_name = "YOUR_PROJECT_NAME"

# Get the dataset (replace 'version' with your dataset version number)
dataset = rf.workspace("ambulancedetection-td1oy").project("ambulance-dn9qr").version(4).download("yolov8")  # Change '1' to your version number

print(f"Dataset downloaded to: {dataset.location}")
