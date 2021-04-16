import matplotlib.pyplot as plt
import numpy as np
from siki.basics import Exceptions


class ChartDescriptionToken(object):

    def __init__(self, chart, title):
        self.chart = chart
        self.bins = np.arange(len(chart))
        self.title = title


class PltChartCache(object):

    def __init__(self):
        self.tokens = []

    def add(self, chart, title):
        token = ChartDescriptionToken(chart, title)
        self.tokens.append(token)

    def _plot_single(self):
        plt.hist(self.tokens[0].chart, self.tokens[0].bins, color='fuchsia', alpha=0.5)
        plt.title(self.tokens[0].title)
        plt.show()

    def _plot_multi(self, nrows, ncols):
        if nrows * ncols != len(self.tokens):
            raise Exceptions.ArrayIndexOutOfBoundsException("Dimensions does not match the size of images")

        # iterate each image
        for i in range(nrows * ncols):
            plt.subplot(nrows, ncols, i + 1)
            plt.hist(self.tokens[0].chart, self.tokens[0].bins, color='fuchsia', alpha=0.5)
            plt.title(self.tokens[i].title)

        plt.show()

    def plots(self, nrows=0, ncols=0):
        if len(self.tokens) == 1:
            self._plot_single()

        if len(self.tokens) > 1:
            self._plot_multi(nrows, ncols)