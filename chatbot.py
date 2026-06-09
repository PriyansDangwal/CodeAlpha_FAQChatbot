import nltk

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt', quiet=True)

def get_best_answer(user_question, faqs):

    questions = list(faqs.keys())

    corpus = questions + [user_question]

    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform(corpus)

    similarity = cosine_similarity(
        vectors[-1],
        vectors[:-1]
    )

    best_match = similarity.argmax()

    score = similarity[0][best_match]

    if score < 0.2:
        return "Sorry, I couldn't find a matching answer."

    return faqs[questions[best_match]]