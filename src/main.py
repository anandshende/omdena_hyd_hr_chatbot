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
        'Nurse',
        'Dedicated and compassionate Registered Nurse with a diverse background in healthcare. Holds a [Degree or Certification] in Nursing from [Institution]. Proven expertise in providing patient-centered care, managing medical records, and collaborating with interdisciplinary teams. Skilled in administering medications, monitoring vital signs, and implementing nursing care plans. Demonstrates strong communication and interpersonal skills, fostering positive relationships with patients, families, and healthcare professionals. Upholds a commitment to continuous learning and professional development. Adept at maintaining a calm and focused demeanor in high-pressure situations. Excited about contributing clinical skills and compassionate care to a dynamic healthcare environment. [Optional: Specify any specializations, such as critical care, pediatrics, or other relevant areas of expertise.]'
    )
