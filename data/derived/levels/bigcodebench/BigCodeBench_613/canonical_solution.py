import pandas as pd
from matplotlib import pyplot as plt

# Constants
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
GOALS_RANGE = (-10, 10)


def task_func(goals, penalties):
    """
    Calculates net scores for teams ('Team A' to 'Team E') by subtracting penalties from goals and clips scores to stay
    within -10 to 10. Visualizes results with a bar chart showing each team's adjusted scores 'Team' on the x-axis and
    score values 'Score' on the y-axis.


    Parameters:
    - goals (dict): A dictionary where keys are team names and values are the number of goals scored.
    - penalties (dict): A dictionary where keys are team names and values are the number of penalties incurred.

    Returns:
    - DataFrame: A pandas DataFrame with columns 'Team' and 'Score', representing each team's net score.

    Requirements:
    - pandas
    - matplotlib

    Example:
    >>> goals = {'Team A': 5, 'Team B': 3, 'Team C': 1, 'Team D': 0, 'Team E': 4}
    >>> penalties = {'Team A': 1, 'Team B': 1, 'Team C': 1, 'Team D': 0, 'Team E': 2}
    >>> df = task_func(goals, penalties)
    >>> print(df)
         Team  Score
    0  Team A      4
    1  Team B      2
    2  Team C      0
    3  Team D      0
    4  Team E      2
    """

    scores_data = []

    for team in TEAMS:
        team_goals = goals.get(team, 0)
        team_penalties = penalties.get(team, 0)
        score = team_goals - team_penalties
        scores_data.append([team, score])

    scores_df = pd.DataFrame(scores_data, columns=['Team', 'Score'])
    scores_df['Score'] = scores_df['Score'].clip(*GOALS_RANGE)

    #Plotting (commented out for testing)
    plt.figure(figsize=(10, 6))
    plt.bar(scores_df['Team'], scores_df['Score'], color='skyblue')
    plt.xlabel('Team')
    plt.ylabel('Score')
    plt.title('Team Scores Distribution')
    plt.ylim(GOALS_RANGE[0] - 1, GOALS_RANGE[1] + 1)
    plt.grid(axis='y', linestyle='--')
    plt.show()

    return scores_df
