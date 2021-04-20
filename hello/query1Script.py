import matplotlib.pyplot as plt

def query1Script(x, date1, date2, y, z):
    time = [0, 1, 2, 3]
    position = [0, 100, 200, 300]

    plt.plot(time, position)
    plt.xlabel('Time (hr)')
    plt.ylabel('Position (km)')
