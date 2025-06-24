# Classification of Fish Species and Habitat

A Computer Vision project using a Convolutional Neural Network (CNN) to classify **31 species of fish** from uploaded images. This web application is built using **Flask** and is ready for deployment on **Railway**.

---

## Features

- Upload fish images and get predicted **species** and **habitat (freshwater or saltwater)**.
- Shows prediction **confidence percentage**.
- Built-in Flask interface with upload & result preview.
- Model trained with image classification using TensorFlow/Keras.

---

## Local Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo.git
cd Classification-of-Fish-Species-and-Habitat
```

### 2. Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate  
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

Then open your browser and visit: [http://localhost:5000](http://localhost:5000)

---

## 📁 Project Structure

```
Classification-of-Fish-Species-and-Habitat/
├── app.py
├── model_ikan.h5
├── class_indices.json
├── requirements.txt
├── Procfile
├── static/
│   └── upload/           # Uploaded images saved here
├── templates/
│   └── index.html        # HTML interface
```

---

## How It Works

- Image is uploaded and preprocessed to size (224x224).
- Image passed into pre-trained CNN model (`model_ikan.h5`).
- Model outputs prediction and confidence score.
- Species is mapped using `class_indices.json`.
- Habitat is determined from internal dictionary (`habitat_dict`).

---

## License

This project is for educational purposes. Please contact the author if you intend to use it commercially or modify it for public deployment.

---

## Author

Developed by **MFH**  
Feel free to fork, contribute, and improve!
