from nba_api.stats.endpoints import playerdashboardbyyearoveryear
import matplotlib.pyplot as plt
from nba_api.stats.static import players




def findPlayerData(name):
    player_dict = players.get_players()
    search_name = name

    player = [player for player in player_dict if player['full_name'].lower() == search_name.lower()][0]


    player_id = player['id']
    player_yBy_Stats = playerdashboardbyyearoveryear.PlayerDashboardByYearOverYear(player_id).get_dict()
    years = [player_yBy_Stats['resultSets'][1]['rowSet']]
    x=[]
    y=[]
    for i in range(len(years[0]) - 1, -1, -1):
        x.append(years[0][i][1])
        y.append(years[0][i][29]/years[0][i][5])
    return x, y


def plotData(x, y, name):
    plt.figure(figsize=(11, 8))
    plt.plot(x, y)
    plt.xticks(rotation='vertical')
    plt.xlabel("Years")
    plt.ylabel("Points per Game", rotation='vertical')
    plt.suptitle(name + " points per game", fontsize = 26)
    plt.show()

if __name__ == '__main__':
    player_name  = input("Please enter your name: ")
    x,y = findPlayerData(player_name)
    plotData(x,y, player_name)

