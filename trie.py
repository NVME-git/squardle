# =========================
# Trie Implementation
# =========================
class TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, "TrieNode"] = {}
        self.is_word: bool = False


class Trie:
    def __init__(self) -> None:
        self.root: TrieNode = TrieNode()

    def insert(self, word: str) -> None:
        node: TrieNode = self.root
        for character in word:
            node = node.children.setdefault(character, TrieNode())
        node.is_word = True

    def has_prefix(self, prefix: str) -> bool:
        node: TrieNode = self.root
        for character in prefix:
            if character not in node.children:
                return False
            node = node.children[character]
        return True

    def contains(self, word: str) -> bool:
        node: TrieNode = self.root
        for character in word:
            if character not in node.children:
                return False
            node = node.children[character]
        return node.is_word
