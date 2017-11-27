import matplotlib.pyplot as plt


class Plotter:
    def __init__(self):
        self.fig = plt.figure(figsize=(30, 10), dpi=50)
        self.subplot = 1

    def add_subplot(self, points, cmap, vmin, vmax, title):
        self.fig.add_subplot(1, 4, self.subplot)
        self.subplot += 1

        plt.imshow(points, cmap=cmap, vmin=vmin, vmax=vmax, interpolation='nearest')
        plt.title(title)
        plt.colorbar()

    def add_graph(self, points):
        splot = self.fig.add_subplot(1, 4, self.subplot)
        self.subplot += 1
        if points:
            previous = points[0]
            for point in points[1:]:
                splot.arrow(previous[0],
                            previous[1],
                            point[0] - previous[0],
                            point[1] - previous[1],
                            head_width=0.0, head_length=0.0, fc='k', ec='k')
                previous = point

            splot.set_xlim(min([p[0] for p in points]), max([p[0] for p in points]))
            splot.set_ylim(min([p[1] for p in points]), max([p[1] for p in points]))

    def plot(self, title, path):
        plt.suptitle(title)
        plt.savefig(path)
        plt.close()
