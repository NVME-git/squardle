from wordfreq import top_n_list
from trie import Trie
from config import WORD_LIST_SIZE, MIN_WORD_LENGTH


# =========================
# Build Trie from English words
# =========================
def build_trie() -> Trie:
    words: list[str] = top_n_list("en", WORD_LIST_SIZE)
    words = [w.lower() for w in words if w.isalpha() and len(w) > MIN_WORD_LENGTH]
    trie: Trie = Trie()
    for w in words:
        trie.insert(w)
    return trie
