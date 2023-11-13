def sansdoublons_liste(L):
    R = []
    for i in range(len(L)):
        # ce test est de plus en plus lent
        # que L est grand
        if L[i] not in R:
            R.append(L[i])

    return R

def sansdoublons_avecEnsemble(L):
    R = []
    S = set()
    for i in range(len(L)):
        # ce test est toujours très rapide
        if L[i] not in S:
            R.append(L[i])
            S.add(L[i])

    return R