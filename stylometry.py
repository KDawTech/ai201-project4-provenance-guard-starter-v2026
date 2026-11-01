"""Second AI-likeness signal: transparent, lexical / structural heuristics.

No stylometric feature establishes provenance. Use only as a low-trust signal.
All signals return in [0, 1] with larger = more AI-like.
"""
import re
import statistics


def words(text: str) -> list[str]:
    return re.findall(r"[a-z0-9']+", text.lower())


def sentences(text: str) -> list[str]:
    return [part.strip() for part in re.split(r'(?<=[.!?])\s+', text.strip()) if part.strip()]


def sentence_length_spread(text: str) -> float:
    """Coefficient of variation of sentence word counts, clipped to [0, 2]."""
    counts = [len(words(sentence)) for sentence in sentences(text)]
    counts = [count for count in counts if count]
    if len(counts) < 2 or not statistics.mean(counts):
        return 0.0
    return round(min(statistics.pstdev(counts) / statistics.mean(counts), 2.0), 4)


def type_token_ratio(text: str) -> float:
    """Fraction of unique tokens among all tokens (length sensitive)."""
    tokens = words(text)
    return round(len(set(tokens)) / len(tokens), 4) if tokens else 0.0


def punctuation_density(text: str) -> float:
    """Punctuation relative to words (commas, semicolons, colons, dashes)."""
    tokens = words(text)
    if not tokens:
        return 0.0
    marks = len(re.findall(r'[,;:\u2014\u2013-]', text))
    return round(min(marks / len(tokens), 1.0), 4)


def _clamp(value: float) -> float:
    return max(0.0, min(1.0, value))


def style_signal(text: str) -> float:
    """Return a modest heuristic signal. Short / one-sentence text is neutral.

    Components (AI-likeness direction):
      - 50% low sentence-length spread
      - 30% repetitive vocabulary in first 50 words
      - 20% uniform punctuation
    Scores are descriptive signals, not calibrated authorship probabilities.
    """
    tokens = words(text)
    if len(tokens) < 35 or len(sentences(text)) < 2:
        return 0.5

    spread = sentence_length_spread(text)
    first_50 = tokens[:50]
    local_diversity = len(set(first_50)) / len(first_50)
    density = punctuation_density(text)

    regularity = 1.0 - _clamp(spread / 0.60)
    repetition = 1.0 - _clamp((local_diversity - 0.45) / 0.45)
    sparse_punctuation = 1.0 - _clamp(density / 0.15)
    score = 0.50 * regularity + 0.30 * repetition + 0.20 * sparse_punctuation
    return round(_clamp(score), 4)


if __name__ == '__main__':
    import sys
    content = ' '.join(sys.argv[1:]) or (
        'Yesterday I walked to the station. The rain suddenly came down harder, '
        'and I missed the bus entirely. Today, though, I remembered my umbrella.'
    )
    print('sentence_length_spread:', sentence_length_spread(content))
    print('type_token_ratio:', type_token_ratio(content))
    print('punctuation_density:', punctuation_density(content))
    print('style_signal:', style_signal(content))
