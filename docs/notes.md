Source: https://www.youtube.com/watch?v=JEpWlTl95Tw


## Proportional only

```
Error = Setpoint - ProcessValue
Output = K * Error
```

$u(t) = K_{p} \times e(t)$


## Proportional + integral

$u(t) = K_{p} \times e(t) + K_{i} \int e(t) \, dt$

$u(t) = K_{p} \times e(t) + K_{i} \sum_{}^{} e(t)$


Most of time we use only one $K$ constant:

$u(t) = K \times e(t) + \sum_{}^{} \frac{K}{\tau_{i}} e(t)$

```
Error = SetPoint - ProcessValue
Reset = Reset + K/tau_i * Error
Output = K * Error + Reset
```


## Proportional + Derivative

$u(t) = K \times e(t) + \frac{K}{\tau_{d}} \frac{d}{dt}(e(t))$
But we cannot measure the actual derivative -> we'll use the slope (taux d'accroissement) instead:

Note: in the video, he doesn't use any  Time value in his derivative / slope (considers the interval $\Delta t = 1$). This is why in the pseudo-code, we simply do `K/tau_d * (Error - LastError)` for the derivative part, we measured the slope on the interval between current and last measure.

$u(t) = K \times e(t) + \frac{K}{\tau_{d}} \frac{\Delta e(t)} {\Delta t}$


```
Error = SetPoint - ProcessValue
ErrorSlope = K/tau_d * (Error - LastError)
Output = K * Error + ErrorSlope
LastError = Error  # need to save it for next pass
```
## Proportional + Integral + Derivative
Going to the general math formula (starting from the simple summations and slope):

Using summation and slope:
$u(t) = K \times e(t) + \frac{K}{\tau_{i}} \sum_{}^{} e(t) + \frac{K}{\tau_{d}} \frac{\Delta e(t)}{\Delta t}$

Using different K's constants (independents):
$u(t) = K \times e(t) + K_{i} \sum_{}^{} e(t) + K_{d} \frac{\Delta e(t)}{\Delta t}$

With Integrals and Derivative instead of Summation and Slope:
$u(t) = K \times e(t) +  K_{i} \int e(t) \, dt + {K_{d}} \frac{d}{dt}(e(t)$)

```
Error = SetPoint - ProcessValue

Reset = Reset + K/tau_i  * Error
ErrorSlope = K/tau_d * (Error - LastError) 

Output = K * Error + Reset + ErrorSlope
LastError = Error
```

