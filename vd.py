import visdom

'''

This will log from a database/file that we are saving using our "Metrics" class
to visdom.  It will look through for each type of data and log to the
appropriate type of plot.
'''

class vd(object):
    def __init__(self, env):
        self.visdom = visdom.Visdom()

    def plot_cm(self, cm, title='Confusion Matrix'):
        """Plot the current confusion matrix."""
        pass

    def plot_metric(self, metric_name, metric, step=None):
        """."""
        pass

    def plot_image(self, image_name, image):
        """."""
        pass

    def plot_image_to_video(self, image_name, image, step=None):
        """."""
        pass
