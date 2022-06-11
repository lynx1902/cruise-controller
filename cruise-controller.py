import matplotlib.pyplot as plt
import numpy as np

# params for the model
m = 1000
b = 1
v_ref=60
v = 0

# defining gain values for the PID controller
kI=0.1
kP=200
kD=0.2

# variables to calculate the error
e = v_ref-v
e_old = e
e_new = 0

# time and velocity arrays
t = np.arange(0,50,1)
velocities = []


for i in range(0,50):
    e = v_ref - v
    e_dot = (e - e_old)
    e_new += e
    u = (kP*e)+(kD*e_dot) + (kI*e_new)   # control equation
    v = (m*v + u - b*v)/(m)              # calculating velocity using Newton's laws
    velocities.append(v)
    print(v)
    e_old = e
    


# Plot to visualise the results
fig, ax = plt.subplots()
ax.plot(t,velocities,label='velocity')
plt.xlabel('Time')
plt.ylabel('Velocity')
ax.hlines(y=60, xmin=0, xmax=50, linewidth=2, color='r', label='reference velocity')
ax.hlines(y=54,xmin=0,xmax=50,color='b',linewidth=2,linestyles='dashed',label='90% of velocity (steady state value)')
plt.legend()
plt.show()
