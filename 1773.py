def countMatches(items, ruleKey, ruleValue):
    out_list = []
    count = 0
    if ruleKey == 'type':
        i = 0
    elif ruleKey == 'color':
        i = 1
    elif ruleKey == 'name':
        i = 2
    for j in range(len(items)):
        out_list.append(items[j][i])
    for k in range(len(out_list)):
        if out_list[k] == ruleValue:
            count += 1
    return count


items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]]
ruleKey = "type"
ruleValue = "phone"

print(countMatches(items, ruleKey, ruleValue))