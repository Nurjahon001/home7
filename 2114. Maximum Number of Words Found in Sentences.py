def mostWordsFound(sentences):
    max_count = 0
    for sentence in sentences:
        words = sentence.split()
        max_count = max(max_count, len(words))
    return max_count
sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
print(mostWordsFound(sentences))