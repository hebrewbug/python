import matplotlib.pyplot as plt



#inizialization
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


plt.plot(random_walks)


plt.show()
