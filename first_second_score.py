def first_second_score(scores):
    score1 = float('-inf')
    score2 = float('-inf')

    for score in scores:

        if score > score1:
            score2 = score1
            score1 = score
        elif score > score2:
            score2 = score

    return score1, score2


def two_sum(scores, total):
    seen = {}

    for key, score in enumerate(scores):

        complement = total - score

        if complement in seen:
            return seen[complement], key
        seen[score] = key


if __name__ == "__main__":
    data = [86, 85, 92, 91, 108, 85]
    print(first_second_score(data))
    print(two_sum(data, 183))
