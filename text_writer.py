import os
from collections import defaultdict
from config import OUTPUT_DIR


def write_words_to_files(words: list[str]) -> None:
    """Write words grouped by length to separate text files and summary."""
    sorted_words = sorted(words, key=lambda w: (len(w), w))
    words_by_length = defaultdict(list)
    for word in sorted_words:
        words_by_length[len(word)].append(word)

    # Write individual word length files
    for word_len in sorted(words_by_length.keys()):
        filename = f"{word_len:02d}_letters.txt"
        filepath = os.path.join(OUTPUT_DIR, filename)

        with open(filepath, "w", encoding="utf-8") as f:
            for word in words_by_length[word_len]:
                f.write(f"{word}\n")
            words_word = "word" if len(words_by_length[word_len]) == 1 else "words"
            f.write(f"\nTotal: {len(words_by_length[word_len])} {words_word}\n")

    # Write summary file
    total_count = sum(len(words) for words in words_by_length.values())
    with open(os.path.join(OUTPUT_DIR, "summary.txt"), "w", encoding="utf-8") as f:
        f.write(f"Total words found: {total_count}\n\n")
        for word_len in sorted(words_by_length.keys()):
            words_word = "word" if len(words_by_length[word_len]) == 1 else "words"
            f.write(
                f"{word_len:2d} letters: {len(words_by_length[word_len])} {words_word}\n"
            )
