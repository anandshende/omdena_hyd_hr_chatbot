import os
import pandas as pd
import chromadb

from utils.common import split_into_sentences
from utils.vectordb_operations import get_collection_from_vector_db

def generate_questions(
    position: str, candidate_profile: str
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

    vdb = os.environ.get('CHROMADB_PATH', '../data/chromadb')
    question_collection: chromadb.Collection = get_collection_from_vector_db(vdb, 'question_collection')
    
    sentences = split_into_sentences(candidate_profile)
    question_df = pd.DataFrame(columns=["question", "q_id", "interview_phase", "position", "distance"])
    
    for sentence in sentences:
        query_response = question_collection.query(
            query_texts=[sentence],
            where={'position': position}
        )
    
        for q_id, metadata, document, distance in zip(query_response['ids'][0], query_response['metadatas'][0], query_response['documents'][0], query_response['distances'][0]):
            row = pd.DataFrame(data={
                'q_id': [q_id],
                'interview_phase': [metadata.get('interview_phase', None)],
                'position': [metadata.get('position', None)],
                'question': [document],
                'distance': [distance]
            })
            
            question_df = pd.concat([
                question_df,
                row
            ])
        
    question_df = question_df.drop_duplicates(subset=['question']).sort_values(by=['distance'], ascending=False).reset_index(drop=True)
    
    resulting_question_df = filter_questions(question_df)
    
    print(resulting_question_df)
    resulting_question_df.to_csv(f'Questions_{position}.csv')
    
    return resulting_question_df

def filter_questions(original_question_df: pd.DataFrame):
    INTERVIEW_PHASE_FLOW = [
        'Introduction',
        'Introduction',
        'Any',
        'Any',
        'Any',
        'Conclusion',
        'Conclusion'
    ]
    result_df = pd.DataFrame(columns=original_question_df.columns)
    
    for phase in INTERVIEW_PHASE_FLOW:
        if phase == 'Any':
            matched_df = original_question_df[(original_question_df.interview_phase != 'Introduction') & (original_question_df.interview_phase != 'Conclusion')][:1]
        else:
            matched_df = original_question_df[original_question_df.interview_phase == phase][:1]
        
        if matched_df.shape[0] == 1:
            original_question_df = original_question_df.drop(index=matched_df.index[0])
            
            result_df = pd.concat([
                result_df,
                matched_df
            ])
    
    return result_df.reset_index(drop=True)