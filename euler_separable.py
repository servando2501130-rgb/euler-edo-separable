"""
EDO separable: dy/dt = 2*t*y,  y(0) = 1,  t in [0, 1],  h = 0.2

Solucion analitica (separacion de variables):
    dy/y = 2t dt  ->  ln|y| = t^2 + C  ->  y(t) = y0 * exp(t^2)
Con y(0) = 1:  y(t) = exp(t^2)
"""
import math


def f(t, y):
    """Lado derecho de la EDO: dy/dt = 2ty."""
    return 2 * t * y


def solucion_exacta(t, y0=1.0):
    """Solucion analitica obtenida por separacion de variables."""
    return y0 * math.exp(t ** 2)


def euler(f, t0, y0, h, n):
    """Metodo de Euler: y_{k+1} = y_k + h * f(t_k, y_k)."""
    ts, ys = [t0], [y0]
    for _ in range(n):
        ys.append(ys[-1] + h * f(ts[-1], ys[-1]))
        ts.append(ts[-1] + h)
    return ts, ys


def main():
    t0, tf, y0, h = 0.0, 1.0, 1.0, 0.2
    n = round((tf - t0) / h)

    ts, ys = euler(f, t0, y0, h, n)

    print(f"{'t':>5} {'Euler':>10} {'Exacta':>10} {'Error abs':>10} {'Error rel %':>12}")
    for t, y in zip(ts, ys):
        ye = solucion_exacta(t, y0)
        err = abs(ye - y)
        print(f"{t:5.1f} {y:10.6f} {ye:10.6f} {err:10.6f} {100 * err / ye:12.4f}")

    try:
        import matplotlib.pyplot as plt
        tt = [i * (tf - t0) / 200 for i in range(201)]
        plt.plot(tt, [solucion_exacta(t, y0) for t in tt], label="Exacta: $e^{t^2}$")
        plt.plot(ts, ys, "o--", label=f"Euler (h={h})")
        plt.xlabel("t")
        plt.ylabel("y")
        plt.legend()
        plt.grid(True)
        plt.savefig("comparacion.png", dpi=150, bbox_inches="tight")
        print("\nGrafica guardada en comparacion.png")
    except ImportError:
        print("\nmatplotlib no instalado: se omite la grafica.")


if __name__ == "__main__":
    main()
