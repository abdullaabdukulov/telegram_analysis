from functools import lru_cache
from keybert import KeyBERT

kw_model = KeyBERT()


@lru_cache(maxsize=128)
def extract_topic(text: str) -> str:
    keywords = kw_model.extract_keywords(text, keyphrase_ngram_range=(1, 2), stop_words='english', top_n=1)
    return keywords[0][0] if keywords else "No topic"
