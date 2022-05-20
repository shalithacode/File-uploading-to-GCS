from flask import Flask, request, render_template,redirect
from werkzeug.utils import secure_filename
app = Flask(__name__, template_folder="template")

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")





@app.route("/result", methods=["GET", "POST"])
def speech():
    
    import os
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "shalitha98-9b0e0cb27e46.json"
    from google.cloud import storage
    
    bucket_name = "shalitha98.appspot.com"
    
    source_file_name =  request.files['filename'].filename
    destination_blob_name = "storage-object-name"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)


    return redirect('/')
    


if __name__ == "__main__":
    app.run(debug=True, threaded=True)
    