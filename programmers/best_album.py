def solution(genres, plays):
    answer = []
    genre_music = {}
    genre_count = {}
    for idx in range(len(genres)):
        try:
            genre_music[genres[idx]].append(idx)
            genre_count[genres[idx]] += plays[idx]
        except:
            genre_music[genres[idx]] = [idx]
            genre_count[genres[idx]] = plays[idx]

    sorted_plays = sorted(list(genre_count.items()), key=lambda x: -x[1])
    for genre, play_num in sorted_plays:
        if len(genre_music[genre]) == 1:
            answer.append(genre_music[genre][0])
        else:
            play_list = []
            for idx in genre_music[genre]:
                play_list.append([idx, plays[idx]])
            play_list.sort(key=lambda x: (-x[1], x[0]))
            answer.append(play_list[0][0])
            answer.append(play_list[1][0])
    return answer