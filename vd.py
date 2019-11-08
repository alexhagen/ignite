import visdom
import matplotlib.pyplot as plt
'''

This will log from a database/file that we are saving using our "Metrics" class
to visdom.  It will look through for each type of data and log to the
appropriate type of plot.
'''

class vd(object):
    def __init__(self, env):
        self.visdom = visdom.Visdom(server="http://deepard.pnl.gov", env=env)
        self.steps = dict()

    def plot_cm(self, cm, title='Confusion Matrix', categories=None):
        """Plot the current confusion matrix."""
        size = cm.shape[0]
        plt.imshow(cm, cmap='cividis', extent=[0, size, 0, size])
        self.visdom.matplot(plt.gcf(), win='confusion_matrix')

    def plot_metric(self, metric_name, metric, step=None):
        """."""
        if step is None:
            if metric_name in self.steps.keys():
                step = self.steps[metric_name] + 1.0
            else:
                step = 0.0
        self.steps[metric_name] = step
        self.visdom.line(X=[step], Y=metric, name=metric_name, win=metric_name,
                         update='append')

    def plot_image(self, image_name, image):
        """."""
        pass

    def plot_image_to_video(self, image_name, image, step=None):
        """."""
        pass
