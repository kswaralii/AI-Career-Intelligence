import spacy


class NLPProcessor:
    """
    Handles NLP preprocessing using spaCy.
    """

    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def process_text(self, text: str):

        doc = self.nlp(text)

        tokens = []
        lemmas = []
        filtered_tokens = []

        for token in doc:

            if token.is_space:
                continue

            tokens.append(token.text)

            lemmas.append(token.lemma_)

            if not token.is_stop and not token.is_punct:
                filtered_tokens.append(token.lemma_.lower())

        return {
    "doc": doc,
    "tokens": tokens,
    "lemmas": lemmas,
    "filtered_tokens": filtered_tokens,
    "normalized_text": " ".join(filtered_tokens)
}