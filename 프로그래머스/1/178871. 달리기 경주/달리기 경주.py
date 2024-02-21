def solution(players, callings):
    players_position = {player :i for i, player in enumerate(players)}
    for call in callings:
        now_idx = players_position[call]
        players[now_idx], players[now_idx-1] = players[now_idx-1], players[now_idx] # players 배열 update
        # dict update
        players_position[players[now_idx]] = now_idx 
        players_position[players[now_idx-1]] = now_idx-1
    return players