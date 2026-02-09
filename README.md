# pix2pix GAN — Image-to-Image Translation

A PyTorch implementation of **pix2pix Generative Adversarial Network (GAN)** for image-to-image translation tasks such as:

✔ Semantic maps → Realistic scenes  
✔ Edges → Color images  
✔ Sketches → Photo-like outputs

This project reproduces the original pix2pix research and provides a working training + inference pipeline.

---

## 🚀 Project Overview

pix2pix is a conditional GAN that learns a **mapping from input images to output images** using paired data.

This repository includes:
✔ Data preprocessing  
✔ Model definition (Generator & Discriminator)  
✔ Training loop with losses  
✔ Inference functionality  
✔ Image results visualization

Ideal for:
- Computer Vision portfolios  
- Research reproduction  
- Generative models learning

---

## 🧠 How pix2pix Works

A GAN consists of two networks:

### Generator
Learns to generate images that mimic the target distribution.

### Discriminator
Learns to distinguish real images from generated ones.

pix2pix adds **conditional inputs**, so the generator sees both the input image and noise, producing the corresponding output.

Loss components include:
- Adversarial loss  
- L1 pixel loss

---

## 🛠️ Tech Stack

- Python 3.8+
- PyTorch  
- NumPy  
- Pillow / Matplotlib

---

## 📦 Installation

Clone the repo:

```bash
git clone https://github.com/Hari7383/pix2pix_GAN.git
cd pix2pix_GAN
```
Create and activate a virtual environment:
```
python -m venv venv
source venv/bin/activate     # Mac/Linux
venv\Scripts\activate         # Windows
```
