import os 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

sample_files = [doc for doc in os.listdir() if doc.endswith('.txt')]
sample_notes = [open(_file, encoding='utf-8').read() for _file in sample_files]

def vectorize(Text):
    return TfidfVectorizer().fit_transform(Text).toarray()

def similarity(doc1, doc2): 
    return cosine_similarity([doc1, doc2])

vectors = vectorize(sample_notes)
s_vectors = list(zip(sample_files, vectors))
plagiarism_results = set()

def check_plagiarism(): 
    global s_vectors
    for sample_a, test_vector_a in s_vectors: 
        new_vectors = s_vectors.copy()
        current_index = new_vectors.index((sample_a, test_vector_a))
        del new_vectors[current_index]
        for sample_b, test_vector_b in new_vectors: 
            sim_score = similarity(test_vector_a, test_vector_b)[0][1]
            sample_pair = sorted((sample_a, sample_b))
            score = (sample_pair[0], sample_pair[1], sim_score) 
            plagiarism_results.add(score)
    return plagiarism_results

for data in check_plagiarism(): 
    print(data)