def solution(genres, plays):
    answer = []
    genres_idx = {}
    genres_cnt = {}
    for i in range(len(genres)):
        if genres[i] in genres_cnt.keys():
            genres_cnt[genres[i]] += plays[i]
            genres_idx[genres[i]].append([plays[i], i])
        else:
            genres_cnt[genres[i]] = plays[i]
            genres_idx[genres[i]] = [[plays[i], i]]
    genres_cnt = sorted(genres_cnt.items(), key=lambda x: x[1], reverse=True)
    for key in genres_idx.keys():
        genres_idx[key].sort(reverse=True, key=lambda x: (x[0], -x[1]))
    for genre, genre_cnt in genres_cnt:
        for i in range(min(2, len(genres_idx[genre]))):
            answer.append(genres_idx[genre][i][1])
    return answer