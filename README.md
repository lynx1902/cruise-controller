# Cruise Controller

Control Objective:   
To control the velocity of car and make it reach desired velocity. 

Here the cars expriences drag due to air proportional to its velocity which is $bv$
and it is given an input $u$    

<!-- ![](https://i.imgur.com/FIlLlOb.png =400x200 )  -->
<img src="https://i.imgur.com/FIlLlOb.png" width="400" height="200"/> 

Model Dynamics:
$m \dot v + bv = u$   

PID controller is used to reach the given desired value of velocity   
P : Proportional gain (helps to reach desired value but does not reachs desired value)   
I : Integral gain (helps to reach desired value but overshoots)   
D : Derivate gain (helps to reduce overshoot due to integral gain)   

​Desired value of velocity: $60 km/hr$

## Result

