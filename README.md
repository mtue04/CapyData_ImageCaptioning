# CapyData_ImageCaptioning_SportAction

## Project Structure:
📂 CapyData_ImageCaptioning
│
├── 📂 app/ # Application-related files (e.g., web UI, APIs)
│
├── 📂 data/ # Data storage
│ ├── 📂 metadata/ # Metadata related to images
│ ├── 📂 raw_images/ # Collected images before preprocessing
│ ├── 📂 raw_photos/ # Raw photos for captioning
│ ├── 📄 captions.txt # Generated image captions
│
├── 📂 models/ # Trained models and checkpoints
│
├── 📂 notebooks/ # Jupyter notebooks for data processing and annotation
│ ├── 📂 dataset/ # Dataset-related experiments and notebooks
│ │ ├── 📄 1_data_collection.ipynb # Data collection notebook
│ │ ├── 📄 2_pinterest_crawler.ipynb # Pinterest image crawler
│ │ ├── 📄 3_data-annotation_openai.ipynb # Image captioning annotation using OpenAI
│ ├── 📄 descriptions.txt # Additional descriptions for notebooks
│
├── 📂 scripts/ # Utility and automation scripts
│
├── 📂 src/ # Source code for preprocessing and other functionalities
│ ├── 📄 descriptions.txt # Description file related to src
│ ├── 📄 preprocessing.py # Data preprocessing script
│
├── 📄 LICENSE
├── 📄 README.md
├── 📄 requirements.txt