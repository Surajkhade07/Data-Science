# import matplotlib.pyplot as plt
# # Giving labels to x and y axis
# years = [1990, 1992, 1994, 1996, 1998, 2000, 2003, 2005, 2007, 2010]
# runs =  [500, 700, 1100, 1500, 1800, 1200, 1700, 1300, 900, 1500]

# plt.plot(years, runs)
# plt.xlabel("Years")
# plt.ylabel("Runs")
# plt.title("Sachin tendulkar yearly runs")
# plt.show()

import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5, 6, 7]  # Days of the week
studying = [3, 4, 3, 5, 4, 3, 4]
playing = [2, 2, 1, 1, 2, 3, 2]
watching_tv = [2, 1, 2, 2, 1, 1, 1]
sleeping = [5, 5, 6, 5, 6, 5, 5]

labels = ['Studying', 'Playing', 'Watching TV', 'Sleeping']
colors = ['skyblue', 'lightgreen', 'gold', 'lightcoral']

plt.figure(figsize=(10,6))
plt.stackplot(days,studying, playing, watching_tv, sleeping,
              labels=labels, colors=colors, alpha=0.9)

plt.legend(loc='best')  # Location of the legend
plt.title('Weekly Activity Tracker')
plt.xlabel('Day')
plt.ylabel('Hours')
plt.grid(True)
plt.show()