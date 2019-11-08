from ignite import vd
import numpy as np
import time

x = vd.vd(env="test_vd")
cm = np.diag(np.ones((5,)))
x.plot_cm(cm)
time.sleep(2)
cm = np.random.uniform(size=(5, 5))
x.plot_cm(cm)

for i in range(10):
    x.plot_metric('loss', [np.power(i, 2.0)])
    time.sleep(1)
