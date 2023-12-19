from utils.generate_questions import generate_questions
from utils.vectordb_operations import (
    generate_qa_vector_db,
    get_collection_from_vector_db,
    list_collections_from_vector_db,
)

if __name__ == "__main__":
    # Run the below command only once. It creates the ChromaDB collection in the data/chromadb_dir directory.
    generate_qa_vector_db()
