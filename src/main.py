from pathlib import Path
from datetime import datetime
from utils.generate_questions import generate_questions
from utils.vectordb_operations import get_collection_from_vector_db

if __name__ == "__main__":
    # Run the below command only once. It creates the ChromaDB collection in the data/chromadb_dir directory.
    # df = pd.read_excel("../data/processed/combined_dataset.xlsx")
    # generate_qa_vector_db(os.environ.get("CHROMADB_PATH", "../data/chromadb"), df)

    vdb_location = (Path.cwd().parent / "data" / "chromadb").__str__()

    print(
        "Looking for question collection (part of ChromaDB) at directory: ",
        vdb_location,
        "\n",
    )
    start = datetime.now()
    print("Question generation process started at: ", datetime.now(), "\n")

    question_collection = get_collection_from_vector_db(
        vdb_location, "question_collection"
    )

    questions_df = generate_questions(
        "Nurse",
        "Dedicated and compassionate Registered Nurse with a diverse background in healthcare. Holds a [Degree or Certification] in Nursing from [Institution]. Proven expertise in providing patient-centered care, managing medical records, and collaborating with interdisciplinary teams. Skilled in administering medications, monitoring vital signs, and implementing nursing care plans. Demonstrates strong communication and interpersonal skills, fostering positive relationships with patients, families, and healthcare professionals. Upholds a commitment to continuous learning and professional development. Adept at maintaining a calm and focused demeanor in high-pressure situations. Excited about contributing clinical skills and compassionate care to a dynamic healthcare environment. [Optional: Specify any specializations, such as critical care, pediatrics, or other relevant areas of expertise.]",
        question_collection,
    )

    print("Question generation process ended at: ", datetime.now(), "\n")
    print("Total time taken for question generation: ", datetime.now() - start, "\n")

    print(questions_df.head(10))
    print("Shape of dataframe is:", questions_df.shape)
