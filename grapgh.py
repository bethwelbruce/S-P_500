import matplotlib.pyplot as plt

event_windows = ["Inclusion day", "Day 1", "Day -1 to 1", "Day -5 to 5", "Day -10 to 10"]
caars = [2.50, 3.25, 2.88, 2.00, 2.22]

plt.plot(event_windows, caars, marker="o")
plt.xlabel("Event window")
plt.ylabel("CAAR")
plt.title("CAARs for S&P 500 index additions")
plt.grid(True)
plt.show()
