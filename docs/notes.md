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
Reset = Reset + K/tau_i  * Error
Output = K * Error + Reset
```


## Proportional + Derivative

$u(t) = K \times e(t) + \frac{K}{\tau_{i}} \times \frac{d}{dt}e(t)$

```
Error = SetPoint - ProcessValue
Output = K * Error + K/tau_i * (Error -LastError)
LastError = Error
```
## Proportional + Integral + Derivative

$u(t) = K \times e(t) + \sum_{}^{} \frac{K}{\tau_{i}} e(t) + \frac{K}{\tau_{i}} \times \frac{d}{dt}e(t)$
