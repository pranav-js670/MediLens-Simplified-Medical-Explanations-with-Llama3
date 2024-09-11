# MediLens-Simplified-Medical-Explanations-with-Llama3

**MediLens** is a powerful web-based application designed to simplify complex medical terminology and enhance patient-caregiver communication. Built using a Django frontend and integrated with a state-of-the-art Llama 3 model, the application dynamically provides extremely simplified explanations of medical terms. This project was developed as part of a 24-hour hackathon challenge and aims to make healthcare information more accessible to people with little to no medical knowledge.

### Hackathon Completion

This project was successfully completed within the 24-hour hackathon timeframe, demonstrating its feasibility, efficiency, and impact in real-world medical scenarios.

## Project Overview

The primary objective of **MediLens** is to bridge the communication gap between healthcare professionals and patients by providing clear, easy-to-understand explanations of medical terms. Through the use of the powerful Llama 3 model, the application dynamically processes medical terminology and delivers user-friendly explanations. The platform also allows users to ask follow-up questions, and the model intelligently responds based on context, without redundant information.

## Features

- **Dynamic Medical Term Explanations**: Automatically identifies medical terms and generates simplified explanations for users.
- **Context-Based Responses**: For subsequent questions, the model responds intelligently without providing unnecessary explanations unless explicitly requested.
- **Frontend Integration**: Fully functional Django-based frontend that allows users to interact with the model through a simple and intuitive web interface.
- **Biomedical NER Integration**: Uses a Named Entity Recognition (NER) model to detect medical terms within the responses dynamically.
- **Efficient Retrieval System**: Leveraging FAISS and RetrievalQA, the system fetches relevant context to answer queries accurately.

## Architecture

The project architecture is divided into two key components:
- **Backend**: Powered by Llama 3, integrated via a RetrievalQA system and FAISS for context-based medical explanations.
- **Frontend**: A Django-based web interface where users can input questions and view simplified medical explanations.

## Technologies Used

- **Llama 3**: State-of-the-art language model for generating dynamic responses and medical term explanations.
- **Django**: Framework for building the frontend web interface and managing user interactions.
- **FAISS**: Fast and efficient retrieval system to fetch relevant context.
- **Hugging Face Transformers**: Used for Biomedical NER to identify technical terms in the text.
- **Python**: Core programming language for backend development and API integration.
- **HTML/CSS/JavaScript**: Frontend web technologies for the Django-based interface.

## Setup and Installation

### Prerequisites

Ensure you have the following installed:
- Python 3.7+
- Django 3+
- Hugging Face Transformers
- FAISS

### Clone the Repository

```bash
git clone https://github.com/pranav-js670/MediLens-Simplified-Medical-Explanations-with-Llama3.git
```

## Usage

- Users can enter medical queries into the input field on the web interface.
- The Llama 3 model, via the backend, processes the text and provides simplified explanations for medical terms.
- Users can ask follow-up questions, and the model will provide direct answers without redundant information unless requested.

## Future Improvements

- Voice Input: Integrate speech-to-text functionality for better accessibility.
- Mobile Optimization: Improve the UI for mobile users.
- Real-time Data: Use real-time medical data sources to enhance the model’s response accuracy.
- Multilingual Support: Expand the model to support multiple languages, allowing users worldwide to benefit.


