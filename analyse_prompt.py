
from dataclasses import dataclass

@dataclass
class TeamStats:
    name: str
    goals_scored: int
    goals_conceded: int
    goals_1st_half: int
    conceded_1st_half: int
    btts_matches: int
    over15_matches: int
    adversaire_forces: list

def calculate_iep(goals_scored: int, goals_conceded: int, forces: list):
    poids = {"haut": 1.2, "milieu": 1.0, "bas": 0.8}
    pond_scored = sum(goals_scored * poids[f] / len(forces) for f in forces)
    pond_conceded = sum(goals_conceded * poids[f] / len(forces) for f in forces)
    if pond_conceded == 0:
        return float('inf')
    return round(pond_scored / pond_conceded, 2)

def analyse_match(team1: TeamStats, team2: TeamStats):
    avg_goals_scored_1 = team1.goals_scored / 5
    avg_goals_scored_2 = team2.goals_scored / 5
    avg_goals_conceded_1 = team1.goals_conceded / 5
    avg_goals_conceded_2 = team2.goals_conceded / 5

    btts_pct = (team1.btts_matches + team2.btts_matches) / 10 * 100
    first_half_goal_pct = ((team1.goals_1st_half > 0) + (team2.goals_1st_half > 0)) / 2 * 100

    iep_1 = calculate_iep(team1.goals_scored, team1.goals_conceded, team1.adversaire_forces)
    iep_2 = calculate_iep(team2.goals_scored, team2.goals_conceded, team2.adversaire_forces)

    result = []
    result.append(f"Match : {team1.name} vs {team2.name}")
    result.append(f"+1.5 buts : {'✅' if team1.over15_matches >= 3 and team2.over15_matches >= 3 else '❌'}")
    result.append(f"BTTS : {'✅' if btts_pct >= 60 else '❌'}")
    result.append(f"+0.5 but en 1re mi-temps : {'✅' if first_half_goal_pct >= 60 else '❌'}")

    if iep_1 > iep_2:
        result.append(f"Équipe la plus susceptible de marquer : {team1.name} ✅")
    elif iep_2 > iep_1:
        result.append(f"Équipe la plus susceptible de marquer : {team2.name} ✅")
    else:
        result.append("Équipe la plus susceptible de marquer : ❌ (Aucune dominance nette)")

    if first_half_goal_pct >= 60:
        if avg_goals_scored_1 > avg_goals_scored_2:
            result.append(f"Victoire 1MT probable : {team1.name}")
        else:
            result.append(f"Victoire 1MT probable : {team2.name}")
    else:
        result.append("Victoire 1MT : ❌ (Pas de forte tendance)")

    return "\n".join(result)

team1 = TeamStats(
    name="Casa Pia",
    goals_scored=5,
    goals_conceded=7,
    goals_1st_half=2,
    conceded_1st_half=3,
    btts_matches=3,
    over15_matches=3,
    adversaire_forces=["milieu", "haut", "bas", "milieu", "haut"]
)

team2 = TeamStats(
    name="Estoril",
    goals_scored=8,
    goals_conceded=5,
    goals_1st_half=3,
    conceded_1st_half=2,
    btts_matches=2,
    over15_matches=4,
    adversaire_forces=["milieu", "milieu", "milieu", "bas", "milieu"]
)
