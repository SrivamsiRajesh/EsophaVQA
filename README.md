# 🏥 Esophageal Atresia Visual Question Answering (VQA) System

An AI-powered medical imaging analysis system for detecting Esophageal Atresia (EA) from pediatric X-ray and ultrasound images.

## 📋 Overview

This project implements a Visual Question Answering system specialized in diagnosing Esophageal Atresia and related congenital anomalies. It uses state-of-the-art vision-language models to analyze medical images and provide accurate, structured diagnoses.

## ✨ Features

- **Medical Image Analysis**: Supports X-ray, ultrasound, and fluoroscopy images
- **Structured Diagnosis**: Categorizes findings as EA, Normal, or Uncertain
- **Interactive UI**: Simple Gradio interface for easy image upload and analysis
- **High Accuracy**: Powered by Mistral small 3.2 24B
- **Safety-Focused**: Emphasizes caution and clear radiological evidence

## 🎯 Diagnostic Categories

The system classifies images into three categories:

- **EA**: Clear signs of esophageal atresia are visible
- **Normal**: No abnormality detected
- **Uncertain**: Image quality insufficient or findings ambiguous

## 🔬 Key Radiological Features Detected

- Proximal blind pouch (air-filled upper esophagus ending blindly)
- Absence of air below the diaphragm (pure EA without TEF)
- Air in the stomach (indicates distal tracheoesophageal fistula)
- Abnormal gas patterns and NG tube curling in proximal pouch

## 📁 Project Structure
```
project/
├── main.py              # Application entry point
├── vqa.py               # VQA system implementation
├── prompts.py           # System prompts and instructions
├── ui.py               # Gradio UI interface
├── .env                 # API keys (not committed)
├── .gitignore          # Git ignore rules
└── data/
    └── dataset.json     # Dataset metadata (11 cases)
```

## 📊 Dataset

The system was developed and tested on a curated dataset of:

- **8 EA cases**: Various types (Type A, Type C) across different modalities
- **3 Normal cases**: Baseline comparisons
- **Total**: 11 annotated cases from Radiopaedia

Dataset structure stored in `data/dataset.json`:
- Modalities: Ultrasound, X-ray, Fluoroscopy
- Each case includes: diagnosis, clinical info, key findings

## 🔒 Safety & Limitations

⚠️ **Important Disclaimers**:

- This is a research/educational tool, **NOT a diagnostic device**
- Always consult qualified medical professionals for actual diagnosis
- The system may produce false positives or false negatives
- Image quality significantly affects accuracy
- Not validated for clinical use

## 📚 References

- Gross RE. The Surgery of Infancy and Childhood. Philadelphia: Saunders, 1953
- [Radiopaedia - Esophageal Atresia](https://radiopaedia.org/articles/oesophageal-atresia)
- Qwen2.5-VL Technical Report

---