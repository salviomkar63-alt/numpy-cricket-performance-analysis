import numpy as np

runs = np.array([
    [45, 62, 33, 51, 72],   # Player 1
    [12, 28, 19, 20, 15],   # Player 2
    [78, 90, 55, 66, 88],   # Player 3
    [30, 25, 40, 22, 35],   # Player 4
    [55, 47, 60, 58, 63],   # Player 5
    [10, 15, 9,  18, 12],   # Player 6
    [80, 95, 72, 89, 110]   # Player 7
])
print("------Match analysis------")
run_match = np.sum(runs,axis=0) #score in match
average_run_match = np.mean(runs,axis=0) #average run 
print(f"score in each match : {run_match}") #score in all matches
print(f"Average score in all match: {average_run_match}")
print(f"The highest score of team in among all matches :{max(run_match)} ,in match no:{np.argmax(run_match)+1}") #highest score in match
print(f"The lowest score of team in among all matches :{min(run_match)} ,in match no:{np.argmin(run_match)+1}") #lowest score in match

print("------Player analysis------")

average_run_player = np.around(np.mean(runs,axis=1))
total_mark = np.sum(runs,axis=1)
print(f"Score of all player in all matches: {total_mark}")     #player run in all match
print(f"The average run of all player :{average_run_player}")    # Average run per player
print(f"Top performer in all matches {max(average_run_player)} ,Player{np.argmax(average_run_player)+1}")  #max average player
print(f"lowest average in all matches {min(average_run_player)} ,Player{np.argmin(average_run_player)+1}")   #min average player
consistent_player =np.std(runs,axis=1)
print(f"The most consistent player is Player{np.argmin(consistent_player)+1} with Std = {min(consistent_player):.2f}")


print("------The analysis completed------")









