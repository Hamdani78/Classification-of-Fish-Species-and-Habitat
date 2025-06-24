# Classification of Fish Species and Habitat

Live Demo: [Visit Web App](https://classification-of-fish-species-and-habitat-production.up.railway.app/)

A Computer Vision project using a Convolutional Neural Network (CNN) to classify **31 fish species** from uploaded images. Built with **Flask**, this app includes both species and habitat (freshwater/saltwater) predictions and is deployed on **Railway**.

---

## Features

- Upload fish images and get predicted **species** with **confidence percentage**.
- Predict habitat type (**freshwater** or **saltwater**).
- Simple, responsive Flask web interface.
- Trained using TensorFlow/Keras with thousands of fish images.

---

## Live Demo

You can try the app here:  
https://classification-of-fish-species-and-habitat-production.up.railway.app/

---

## Local Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Hamdani78/Classification-of-Fish-Species-and-Habitat.git
   cd Classification-of-Fish-Species-and-Habitat
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app locally**

   ```bash
   python app.py
   ```

5. Open your browser and go to:  
   `http://localhost:5000`

---

## Project Structure

```
Classification-of-Fish-Species-and-Habitat/
├── app.py
├── model_ikan.h5
├── class_indices.json
├── requirements.txt
├── Dockerfile
├── static/
│   └── upload/           # Uploaded images are saved here
├── templates/
│   └── index.html        # Flask HTML interface
```

---
## How It Works

- User uploads an image via the web interface.
- Image gets preprocessed (resized to 224×224, normalized).
- Uploaded image passed through the pre-trained CNN model (`model_ikan.h5`).
- The model outputs predicted class and confidence score.
- Species name is retrieved via `class_indices.json`.
- Habitat type (freshwater/saltwater) determined using `habitat_dict` in code.

---

## Dataset

**Source:** [Fish Dataset on Kaggle](https://www.kaggle.com/datasets/markdaniellampa/fish-dataset)  
**Description:** Contains thousands of labeled images of **31 fish species**, spanning both freshwater and saltwater types, with diverse lighting and angles. Used for training the classification model.

---

## Author

Developed by **MFH** ([Hamdani78](https://github.com/Hamdani78))  
Feel free to fork, contribute, and improve!
