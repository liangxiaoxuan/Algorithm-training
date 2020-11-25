# Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.
# It is guaranteed there is at least one word that isn't banned, and that the answer is unique.
#
# Words in the list of banned words are given in lowercase, and free of punctuation.
# Words in the paragraph are not case sensitive.  The answer is in lowercase


def mostCommonWord(paragraph, banned):
    """
    :type paragraph: str
    :type banned: List[str]
    :rtype: str
    """


if __name__ == '__main__':
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit"
    banned = ["a", "b"]
    banned_words = set(banned)
    print(banned_words)