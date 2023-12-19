# HR Round Preparation LLM Based Chatbot
HR Round Chatbot created as part of Omdena Hyderabad Local Chapter project


### Installation

To install the project, make sure you have 
- [Git](https://git-scm.com/downloads)
- [Python 3.10.12](https://www.python.org/downloads/release/python-31012/)
- [Poetry](https://python-poetry.org/docs/#installation) installed.


**1. Clone the repository**
```bash
git clone https://github.com/abheeeshekdutta/omdena_hyd_hr_chatbot.git
```

**2. Install Poetry and activate the virtual environment**
```bash
poetry install
poetry shell
```

**3. Setup environment variables**
```bash
cp .env.example .env
```
Replace the values in `.env` with your own values.

### Folder Structure

The project follows the following folder structure:

```
.
├── README.md                         --> Project README
├── LICENSE                           --> License file
├── data                              --> Data Directory
│   ├── chromadb_dir/                 --> Directory for storing ChromaDB collections
│   ├── originals/                    --> Original data files received from team
│   ├── processed/                    --> Combined and processed dataset
├── poetry.lock                       --> Poetry Lock File
├── pyproject.toml                    --> Poetry Project File
├── src/                              --> Source Directory
│    ├── utils/                       --> Common directory for utility functions
│    ├── main.py                      --> Main application file
└── tests/                            --> Directory containing all unit tests
```