import pandas as pd
import chromadb


def generate_questions(
    position: str, candidate_profile: str, vdb: chromadb.Collection
) -> pd.DataFrame:
    """This function will generate a set of relevant questions, given the candidate's position of choosing and their profile.

    Under the hood, it uses semantic search to extract the relevant questions from a vector database containing the
    embeddings of the question bank gathered as part of the project.

    Args:
        position (str): Position of the candidate for which the interview is taking place.
        candidate_profile (str): Description of the profile of the candidate.

    Returns:
        pd.DataFrame: Pandas dataframe containing a list of all relevant questions generated.
    """

    return pd.DataFrame
