import itertools, sys

def half_hash(docs):
    """Takes a list of docs and returns pairs
    of docs with a Levenshtein distance of <= 1."""
    candidate_pairs_map = {}
    for doc in docs:
        l = len(doc)
        halves = []
        if l % 2 == 0:
            halves.append(doc[0:l // 2])
            halves.append(doc[l // 2:l])
        else:
            halves.append(doc[0:l // 2])
            halves.append(doc[0:l // 2 + 1])
            halves.append(doc[l // 2 + 1:l])
            halves.append(doc[l // 2:l])
        for half in halves:
            if half in candidate_pairs_map:
                candidate_pairs_map[half].append(doc)
            else:
                candidate_pairs_map[half] = [doc]

    candidate_pairs = set()
    for bucket, similar_docs in candidate_pairs_map.items():
        if len(similar_docs) > 1:
            for candidate_pair in itertools.combinations(sorted(set(similar_docs)), 2):
                candidate_pairs.add(candidate_pair)
    return candidate_pairs





if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        lines = list(map(lambda x:x.lower().strip(), f.readlines()))
    print(len(half_hash(lines)))

