def balancedString(s):
    m = "QWER"
    counts = []
    for i in range(len(m)):
        counts.append(s.count(m[i]))
    rem = []
    for j in range(len(counts)):
        if counts[j] >= len(s) / 4:
            rem.append(0)
        else:
            rem.append((len(s) / 4) - counts[j])
    out = sum(rem)
    return int(out)



s = "WWEQERQWQWWRWWERQWEQ"
print(balancedString(s))