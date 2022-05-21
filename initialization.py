# initialization
import numpy as np
import matplotlib as plt


all_walks = []
for i in range(10) :
    random_walks = [0]
    for x in range(100) :
        step = random_walks[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walks.append(step)
    all_walk2.append(random_walks)

# converting to the NumPy array
np_aw = np.array(all_walk2)

# showing of np_aw
plt.plot(np_aw)
plt.show()

# Clearing
plt.clf()

# transporting to the np_aw_transported
np_aw_transported = np.transpose(np_aw)

# Plot of np_aw_transported and show
plt.plot(np_aw_transported)
plt.show()
