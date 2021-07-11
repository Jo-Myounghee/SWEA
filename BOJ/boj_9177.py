'''
1
cat tree tcraete

3
cat tree tcraete
cat tree catrtee
cat tree cttaree

10
abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxzyyz
abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxzyyz
abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxzyyz
abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxzyyz
abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxzyyz
abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxzyyz
abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxzyyz
abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxzyyz
abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxzyyz
abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxzyyz
abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz

1. if a[a_idx] == res[len]: dfs(a_idx+1, b_idx, len+1)
    if b[b_idx] == res[len]: dfs(a_idx, b_idx+1, len+1)
2. break 조건 : 증가한 길이 (len)이 세번째 문자열의 길이와 같아질 때
3. 만약 세번째 word에 첫번째 word와 두번째 word에 들어있지 않는 단어가 들어있다면? -> no 출력
만약 사용된 문자의 갯수가 다르다면 -> no 출력
'''
def test():
    global a, b, c
    a_b_lst = list(a) + list(b)
    a_b_set = list(set(a_b_lst))
    c_lst = list(c)
    c_set = list(set(c_lst))
    if a_b_set != c_set:
        return False
    a_b_dict = dict()
    c_dict = dict()
    for i in range(len(a_b_set)):
        word = a_b_set[i]
        a_b_dict[word] = a_b_lst.count(word)
    for i in range(len(c_set)):
        word = c_set[i]
        c_dict[word] = c_lst.count(word)
    for key in c_dict.keys():
        if c_dict[key] != a_b_dict[key]:
            return False
    return True

def find(a_idx, b_idx, c_idx):
    global a, b, c, answer

    # 종료 조건
    if c_idx == len(c)-2:
        answer = True
        return

    isAnswer = False
    if a_idx < len(a) and a[a_idx] == c[c_idx]:
        find(a_idx+1, b_idx, c_idx+1)
        isAnswer = True
    if b_idx < len(b) and b[b_idx] == c[c_idx]:
        find(a_idx, b_idx+1, c_idx+1)
        isAnswer = True

    if not isAnswer:
        answer = False
        return

T = int(input())
for tc in range(1, T+1):
    a, b, c = map(str, input().split())
    if not test():
        print(f'Data set {tc}: no')
        continue
    
    answer = False
    find(0, 0, 0)
    if answer:
        total = 'yes'
    else:
        total = 'no'
    print(f'Data set {tc}: {total}')