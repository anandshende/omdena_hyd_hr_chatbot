import os
import pandas as pd

from utils.generate_questions import generate_questions
from utils.vectordb_operations import (
    generate_qa_vector_db,
    get_collection_from_vector_db,
    list_collections_from_vector_db,
)

if __name__ == "__main__":
    df = pd.read_excel('../data/processed/combined_dataset.xlsx')
    # Run the below command only once. It creates the ChromaDB collection in the data/chromadb_dir directory.
    # generate_qa_vector_db(
    #     os.environ.get('CHROMADB_PATH', '../data/chromadb'),
    #     df
    # )
    
    generate_questions(
        'Medical Assistant',
        ''
    )
