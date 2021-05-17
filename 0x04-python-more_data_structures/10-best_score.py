#!/usr/bin/python3
def best_score(a_dictionary):
    from collections import Counter
    score_best = Counter(a_dictionary)
    high = score_best.most_common()
    for i in high:
        if i not in high:
            return None
        else:
            for key in high:
                k = high[0]
                return(k[0])
