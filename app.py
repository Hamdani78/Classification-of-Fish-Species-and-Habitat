from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from werkzeug.utils import secure_filename
from datetime import datetime
import numpy as np
import json
import os

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Konfigurasi folder upload
UPLOAD_FOLDER = 'static/upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load model dan class indices
model = load_model("model_ikan.h5")
with open("class_indices.json") as f:
    class_indices = json.load(f)
label_map = {v: k for k, v in class_indices.items()}

# Daftar spesies & habitat
species_list = [
    "Bangus", "Big Head Carp", "Black Spotted Barb", "Carp", "Catfish", "Climbing Perch",
    "Fourfinger Threadfin", "Freshwater Eel", "Glass Perchlet", "Goby", "Gold Fish", "Gourami",
    "Guppy", "Hampala Barb", "Harlequin Fish", "Indian Mackerel", "Jaguar Gapote", "Janitor Fish",
    "Knifefish", "Long-Snouted Pipefish", "Mosquito Fish", "Mudfish", "Mullet", "Pangasius", "Perch",
    "Scat Fish", "Silver Barb", "Snakehead", "Snapper", "Tetra", "Tilapia"
]

habitat_list = [
    "Air Laut/Asin", "Air Tawar", "Air Tawar", "Air Tawar", "Air Tawar", "Air Tawar",
    "Air Laut/Asin", "Air Tawar", "Air Tawar", "Air Laut/Asin", "Air Tawar", "Air Tawar",
    "Air Tawar", "Air Tawar", "Air Tawar", "Air Laut/Asin", "Air Tawar", "Air Tawar",
    "Air Tawar", "Air Laut/Asin", "Air Tawar", "Air Tawar", "Air Laut/Asin", "Air Tawar", "Air Tawar",
    "Air Laut/Asin", "Air Tawar", "Air Tawar", "Air Laut/Asin", "Air Tawar", "Air Tawar"
]

habitat_dict = dict(zip(species_list, habitat_list))

# Fungsi prediksi
def predict(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    confidence = np.max(prediction)
    class_idx = np.argmax(prediction)
    species = label_map[class_idx]
    habitat = habitat_dict.get(species, "Tidak Diketahui")

    return species, habitat, confidence

# Halaman utama
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if 'image' not in request.files:
            return render_template("index.html", error="Tidak ada file yang dipilih.",
                                   species_list=species_list, habitat_list=habitat_list)

        img_file = request.files["image"]
        if img_file.filename == '':
            return render_template("index.html", error="Nama file kosong.",
                                   species_list=species_list, habitat_list=habitat_list)

        if img_file:
            filename = secure_filename(img_file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            img_file.save(filepath)

            species, habitat, confidence = predict(filepath)
            confidence_percent = f"{confidence * 100:.2f}"

            return render_template("index.html",
                                   filename=filename,
                                   prediction=True,
                                   species=species,
                                   habitat=habitat,
                                   confidence=confidence_percent,
                                   timestamp=datetime.now().timestamp(),  # ⬅️ Tambahkan timestamp
                                   species_list=species_list,
                                   habitat_list=habitat_list)

    return render_template("index.html", prediction=False,
                           species_list=species_list, habitat_list=habitat_list)

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
