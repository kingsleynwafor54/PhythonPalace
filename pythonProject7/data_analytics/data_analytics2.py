# Note: this requires th ``pillow`` package to be installed
from sklearn.datasets import load_sample_image
from matplotlib import pyplot as plt
import numpy as np

# china = load_sample_image("Frass&Tanya.PNG")
china = load_sample_image("china.jpg")
ax = plt.axes(xticks=[], yticks=[])
ax.imshow(china)
print(china)
print(china.shape)

data = china / 255.0
data = data.reshape(427 * 640, 3)
print(data.shape)


def plot_pixels(data, title, colors=None, N=10000):
    if colors is None:
        colors = data

    # choose a random subset
    rng = np.random.RandomState(0)
    i = rng.permutation(data.shape[0])[:N]
    colors = colors[i]
    R, G, B = data[i].T

    fig, ax = plt.subplots(1, 2, figsize=(16, 6))
    ax[0].scatter(R, G, color=colors, marker='.')
    ax[0].set(xlabel='Red', ylabel='Green', xlim=(0, 1), ylim=(0, 1))

    ax[1].scatter(R, G, color=colors, marker='.')
    ax[1].set(xlabel='Red', ylabel='Green', xlim=(0, 1), ylim=(0, 1))

    fig.suptitle(title, size=20)


plot_pixels(data, title='Input color space: 16 million possible colors')
plt.show()

import warnings;

warnings.simplefilter('ignore')
from sklearn.cluster import MiniBatchKMeans

kmeans = MiniBatchKMeans(16)
kmeans.fit(data)
new_colors = kmeans.cluster_centers_[kmeans.predict(data)]

plot_pixels(data, colors=new_colors, title="Reduced color space: 16 colors")

# plt.show()
china_recolored = new_colors.reshape(china.shape)

fig, ax = plt.subplots(1, 2, figsize=(16, 6), subplot_kw=dict(xticks=[], yticks=[]))
fig.subplots_adjust(wspace=0.05)
ax[0].imshow(china)
ax[0].set_title('Original Image', size=16)
ax[1].imshow(china_recolored)
ax[1].set_title('16-color Image', size=16)
plt.show()

# Unsupervised learning system(Reinforcement Learning Algorithm)
import numpy as np

# R matrix

R = np.matrix([[-1, -1, -1, -1, 0, -1],
               [-1, -1, -1, 0, -1, 100],
               [-1, -1, -1, 0, -1, -1],
               [-1, 0, 0, -1, 0, -1],
               [-1, 0, 0, -1, -1, 100],
               [-1, 0, -1, -1, 0, 100]])
# print (R)
# Q matrix for traversing among 6 states (0-5)
Q = np.matrix(np.zeros([6, 6]))
# print(Q)

print(R)
# Gamma (learning parameter)
gamma = 0.8

# Initial state (Usually to be chosen at random)
initial_state = 1


# This function returns all available actions in the state given as an argument
def available_actions(state):
    current_state_row = R[state,]
    av_act = np.where(current_state_row >= 0)[1]
    return av_act


# Get available actions in the current state

available_act = available_actions(initial_state)
#This function chooses at r andom which action to be performed within the range of all the available actions
def sample_next_action(available_action_range):
    next_action=int(np.random.choice(available_action_range,1))
    return next_action

# Samplel next action to be performed
action=sample_next_action(available_act)
def update(current_state, action, gamma):
    max_index = np.where(Q[action,] == np.max(Q[action,]))[1]

    if max_index.shape[0] > 1:
        max_index = int(np.random.choice(max_index, size=1))
    else:
        max_index = int(max_index)
    max_value = Q[action, max_index]

    # Q learning formular
    Q[current_state, action] = R[current_state, action] + gamma * max_value
    
    
# Update Q matrix
update(initial_state, action, gamma)
 
 

#Training phase
#Train over 10 000 iterations(Re-iterate the #process above)

for i in range(10000):
    current_state=np.random.randint(0,int(Q.shape[0]))
    available_act=available_actions(current_state)
    action=sample_next_action(available_act)
    update(current_state,action,gamma)

#Normalize the "trained"
#Q Matrix
print("Trained Q matrix:")
print(Q/np.max(Q)*100)

#Testing
#Goal_State=5
#Calculatee_the_best_policy
current_state=2
steps=[current_state]
while  current_state!=5:
    next_step_index=np.where(Q[current_state,]==np.max(Q[current_state]))[1]
    if next_step_index.shape[0]>1:
        next_step_index=int(np.random.choice(next_step_index,size=1))
    else:
        next_step_index=int(next_step_index)

    steps.append(next_step_index)
    current_state=next_step_index

# Print selected sequence of steps
print("Selected path:")
print(steps)




