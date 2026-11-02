# Método de Euler para una EDO separable
 
## Problema
 
Resolver la ecuación diferencial
 
    dy/dt = 2ty,   y(0) = 1,   t ∈ [0, 1]
 
de dos formas: analíticamente y numéricamente con el método de Euler (h = 0.2). Luego comparar ambas.
 
## Solución analítica (separación de variables)
 
1. Separar variables: `dy / y = 2t dt`
2. Integrar: `ln|y| = t² + C`
3. Despejar: `y = K·e^(t²)`, con `K = e^C`
4. Aplicar `y(0) = 1`: `K = 1`
**Solución exacta:** `y(t) = e^(t²)`
 
## Método de Euler
 
Fórmula: `y_{k+1} = y_k + h·f(t_k, y_k)`, con `f(t, y) = 2ty`, `h = 0.2`, 5 pasos.
 
## Resultados
 
| t   | Euler    | Exacta   | Error abs | Error rel % |
|-----|----------|----------|-----------|-------------|
| 0.0 | 1.000000 | 1.000000 | 0.000000  | 0.00        |
| 0.2 | 1.000000 | 1.040811 | 0.040811  | 3.92        |
| 0.4 | 1.080000 | 1.173511 | 0.093511  | 7.97        |
| 0.6 | 1.252800 | 1.433329 | 0.180529  | 12.60       |
| 0.8 | 1.553472 | 1.896481 | 0.343009  | 18.09       |
| 1.0 | 2.050583 | 2.718282 | 0.667699  | 24.56       |
 
## Análisis
 
- El error crece con t. Euler es de primer orden: el error global es O(h).
- La solución es convexa y creciente. Euler usa la pendiente al inicio de cada paso, por lo que subestima y el error se acumula.
- En t = 0 la pendiente es 0, así que el primer paso no cambia y.
- Reducir h disminuye el error de forma proporcional.
## Ejecución
 
    python euler_separable.py
 
Requiere Python 3. `matplotlib` es opcional (genera `comparacion.png`).
 
    pip install matplotlib
 
