#!/usr/bin/env python3


def list_comprehensions(players: list) -> None:
    high_scores = [i['name'] for i in players if i['score'] > 2000]
    scores_doubled = [i['score'] * 2 for i in players]
    active_players = [i['name'] for i in players if i['status'] == 'active']
    banned_players = [
        (i['name'], f"Reason: {i['ban_reason']}")
        for i in players if i['status'] == 'banned']
    print(
        f"High scores (<2000): {high_scores}\n"
        f"Scores doubled: {scores_doubled}\n"
        f"Active players: {active_players}\n"
        f"Ban Hammer history: {'- ' .join(map(str, banned_players))}"
        )


def dict_comprehension(players: list, achievements: list) -> None:
    player_scores = {
                    i['name']: i['score'] for i in players
                    if i['name'] != 'john_pork'}
    score_categories = {
        'high': len([i for i in players if i['score'] > 2000]),
        'medium': len([i for i in players if 1000 <= i['score'] <= 2000]),
        'low': len([i for i in players if i['score'] < 1000])
        }
    print(
        f"Players scores: {player_scores}\n"
        f"Score categories: {score_categories}\n"
        f"Achievements counts: {len(achievements)}")


def set_comprehension(players: list, regions: dict) -> None:
    unique_players = {
        p['name'] for p in players
        if [o['name'] for o in players
            if o['name'] in p['name']] == [p['name']]}
    all_achiv = [a for p in players for a in p['achievements']]
    unique_achiv = {
        a for a in all_achiv
        if [o for o in all_achiv if o == a] == [a]}
    active_regions = {
        reg for reg, status in regions.items()
        if status == "active"}
    print(
        f"Unique players: {unique_players}\n"
        f"Unique achievements: {unique_achiv}\n"
        f"Active regions: {active_regions}"
    )


def combined_analysis(players: list, achiv: list) -> None:
    total_players = len(players)
    total_achiv = len(achiv)
    average_score = sum([i['score'] for i in players
                        if i['name'] != 'john_pork']) / total_players - 1
    top_player = [
        (i['score'], i['name'], len(i['achievements']))
        for i in players]
    mvp_s, mvp_n, mvp_a = max(top_player)
    print(
        f"Total players: {total_players}\n"
        f"Total unique achievements: {total_achiv}\n"
        f"Average score: {average_score:.1f}\n"
        f"Top performer: {mvp_n} "
        f"({mvp_s} points, {mvp_a} achievements)"
    )


def ft_analytics_dashboard() -> None:
    players = [
        {'name': 'alice',
            'status': 'active',
            'level': 41,
            'score': 2824,
            'achievements': [
                'first_blood', 'level_master',
                'speed_runner', 'pixel_perfect']},
        {'name': 'bob',
            'status': 'offline',
            'level': 16,
            'score': 4657,
            'achievements': [
                'treasure_seeker', 'boss_hunter',
                'speed_runner', 'pixel_perfect', 'combo_king']},
        {'name': 'charlie',
            'status': 'offline',
            'level': 44,
            'score': 9935,
            'achievements': [
                'snake_beater', 'boss_hunter',
                'level_master', 'speed_runner']},
        {'name': 'charlie2',
            'status': 'active',
            'level': 3,
            'score': 488,
            'achievements': ['explorer', 'first_blood']},
        {'name': 'eve',
            'status': 'offline',
            'level': 33,
            'score': 1434,
            'achievements': ['garden_gnome', 'explorer', 'speed_runner']},
        {'name': 'frank',
            'status': 'active',
            'level': 15,
            'score': 1359,
            'achievements': ['party_pooper', 'boss_hunter']},
        {'name': 'john_pork',
            'status': 'banned',
            'ban_reason': 'Exploiting and glitching - XP and score hacks',
            'level': 9999999999,
            'score': 9999999999,
            'achievements': ['ban_hammered']},
        {'name': 'definitely_not_john_pork',
            'status': 'active',
            'level': 9,
            'score': 167,
            'achievements': ['party_pooper']}]

    achievements = [
        'first_blood', 'level_master', 'speed_runner',
        'treasure_seeker', 'boss_hunter', 'pixel_perfect',
        'combo_king', 'explorer', 'party_pooper', 'snake_beater',
        'garden_gnome', 'ban_hammered']

    regions = {
        'europe': 'active',
        'asia': 'active',
        'north america': 'active',
        'south america': 'closed',
        'australia': 'under maintenance',
        'africa': 'closed'}

    print("=== Game Analytics Dashboard ===")
    print("\n=== List Comprehension Examples  ===")
    list_comprehensions(players)
    print("\n=== Dict Comprehension Examples ===")
    dict_comprehension(players, achievements)
    print("\n=== Set Comprehension Examples ===")
    set_comprehension(players, regions)
    print("\n=== Combined Analysis ===")
    combined_analysis(players, achievements)


if __name__ == "__main__":
    ft_analytics_dashboard()
