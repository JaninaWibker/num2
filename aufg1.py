import marimo

__generated_with = "0.13.6"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Programmieraufgabe 1: (gedämpftes) Newton-Verfahren

    **Abgabe in den Programmiertutorien am 14. und 15. Mai 2025.**
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Benötigte Module für dieses Notebook:""")
    return


@app.cell
def _():
    import numpy as np
    return (np,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    In diesem Notebook wollen wir das Newton-Verfahren und das gedämpfte Newton-Verfahren zur Approximation einer Nullstelle der Funktion
    $$f: \mathbb{R}^2 \to \mathbb{R}^2, \quad x = (x_1,x_2) \mapsto \begin{pmatrix} 1 - \frac{2}{\exp(x_1-x_2)+1} \\ x_2^3 + x_2 -2 \end{pmatrix}$$
    testen.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""**(a) Schreiben Sie jeweils eine Prozedur, die für einen Vektor $x\in\mathbb{R}^2$ die Funktion bzw. deren Ableitung an der Stelle $x$ berechnet und als `numpy`-array zurückgibt.**""")
    return


@app.cell
def _(np):
    def f(x):
        x_1 = x[0]
        x_2 = x[1]
        y_1 = 1 - 2 / (np.exp(x_1 - x_2) + 1)
        y_2 = x_2 ** 3 + x_2  - 2

        return np.array([y_1, y_2])

    def fprime(x):
        x_1 = x[0]
        x_2 = x[1]

        # differentiate f_1 by x_1
        y_11 = 2 * np.exp(x_1-x_2) / ((np.exp(x_1 - x_2) + 1) ** 2)
        # differentiate f_1 by x_2
        y_12 = 2 * np.exp(x_1-x_2) / ((np.exp(x_1 - x_2) + 1) ** 2)
        y_21 = 0 # differentiate f_2 by x_1
        y_22 = 3 * (x_2 ** 2) + 1 # differentiate f_2 by x_2
        return np.array([[y_11, y_12], [y_21, y_22]])

    f([1, 1])
    fprime([1, 1])
    return f, fprime


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    **(b) Schreiben Sie eine Prozedur, die das Newton-Verfahren mit den in der Vorlesung besprochenen Kovergenz- und Abbruchkriterien auf eine Funktion $f:\mathbb{R}^n \to \mathbb{R}^n$ für beliebiges $n\in\mathbb{N}$ anwendet.**

    Ihrer Prozedur soll folgende Eingabedaten haben:
    - Einen Vektor `x0`, der den Startwert $x^{(0)}\in\mathbb{R}^n$ für das Newton-Verfahren enthält.
    - Zwei Prozeduren `f` und `fprime`, mit denen Funktions- und Ableitungswerte von $f$ berechnet werden können.
    - Eine Toleranz `tol` und eine maximale Zahl an Iterationen `kMax`, mit denen die Konvergenz- und Abbruchkriterien gesteuert werden können.

    Berücksichtigen Sie außerdem folgendes:
    - Die im Newton-Verfahren auftretenden Gleichungssysteme können Sie mit dem in `numpy` enthaltenen LGS-Löser `np.linalg.solve` lösen.
    - Am Ende der Prozedur sollen alle berechneten Iterierten $x^{(k)}$, $k=0,1,2,...$ an das Hauptprogramm zurückgegeben werden. Geben Sie außerdem eine Meldung aus, ob das Verfahren erfolgreich konvergiert ist, oder ob es wegen Divergenz bzw. wegen Erreichen der maximalen Iterationszahl abgebrochen hat.

    _Hinweis:_ Sie können alle Iterierten zum Beispiel als Zeilen in einer gemeinsamen Matrix speichern. Jedes Mal, wenn eine neue Iterierte berechnet wurde, wird die Matrix dementsprechend um eine Zeile ergänzt. Dazu ist der Befehl `np.vstack` hilfreich. Beispielsweise werden drei Matrizen `A1,A2,A3` derselben Breite mit dem Aufruf `np.vstack((A1,A2,A3))` übereinander gestapelt.
    """
    )
    return


@app.cell
def _(np):
    def newton(x0: np.ndarray, f: callable, fprime: callable, tol: float, kmax: int):
        done = False
        k = 0
        x = [x0]
        while True:
            # compute f(x_k) and f'(x_k)
            ff = f(x[k])
            ffprime = fprime(x[k])

            # check convergence criteria
            if np.linalg.norm(ff) <= tol:
                break

            # solve f'(xk)Δxk = -f(xk)
            delta_xk = np.linalg.solve(ffprime, -ff)

            # prepare for next loop iteration
            x.append(x[k] + delta_xk)
            k = k + 1

            # check abort condition
            if k >= kmax:
                print(f"aborted because kmax reached (kmax={kmax})")
                break

        return np.array(x)

    return (newton,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    **(c) Testen Sie Ihre Prozedur für die obige Funktion $f$ mit den Startvektoren $x^{(0)} = (4,2)^T$ und $x^{(0)} = (4,-4)^T$. Verwenden Sie die Parameter `tol = 1e-8` und `kMax = 20`.**

    Geben Sie alle Iterierten aus. Für welchen Startvektor konvergiert das Verfahren? Vergewissern Sie sich im Falle der Konvergenz anhand der Funktionsvorschrift von $f$, dass Sie tatsächlich eine Nullstelle von $f$ erhalten haben. Geben Sie in dem Fall auch den Fehler der einzelnen Iterierten aus. Können Sie die erwartete, quadratische Konvergenz erkennen?
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Startwert $x^{(0)} = (4,2)^T$:""")
    return


@app.cell
def _(f, fprime, newton, np):
    newton(
        np.array([4, 2]),
        f,
        fprime,
        tol=1e-8,
        kmax=20
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Startwert $x^{(0)} = (4,-4)^T$:""")
    return


@app.cell
def _(f, fprime, newton, np):
    newton(
        np.array([4, -4]),
        f,
        fprime,
        tol=1e-8,
        kmax=20
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    **(d) Kopieren Sie das Newton-Verfahren von oben und ändern Sie es zum gedämpften Newton-Verfahren ab. Der Parameter $\lambda_{\min}$ soll dabei als zusätzlicher Eingabeparameter übergeben werden, während im ersten Schritt immer mit dem Wert $\lambda = 1$ gestartet wird. Geben Sie zusätzlich zu den Iterierten auch die verwendeten Dämpungsparameter an das Hauptprogramm zurück.**

    _Hinweis:_ Das Schlüsselwort `lambda` hat in Python eine ganz besondere Bedeutung und sollte daher nicht als Variablenname genutzt werden.
    """
    )
    return


@app.cell
def _(np):
    def damped_newton(x0: np.ndarray, f: callable, fprime: callable, tol: float, kmax: int, lambda_min: float):
        done = False
        k = 0
        x = [x0]
        l = 1
        while True:
            # compute f(x_k) and f'(x_k)
            ff = f(x[k])
            ffprime = fprime(x[k])

            # check convergence criteria
            if np.linalg.norm(ff) <= tol:
                break

            # solve f'(xk)Δxk = -f(xk)
            delta_xk = np.linalg.solve(ffprime, -ff)

            ff_hat = f(x[k] + l * delta_xk)

            # solve f'(xk)Δxk = -f(xk + λ*Δxk)
            delta_xk_hat = np.linalg.solve(ffprime, -ff_hat)
            while np.linalg.norm(delta_xk_hat) > (1 - l / 2) * np.linalg.norm(delta_xk):
                l = l / 2
                if l < lambda_min:
                    break
                ff_hat = f(x[k] + l * delta_xk)
                # solve f'(xk)Δxk = -f(xk + λ*Δxk)
                delta_xk_hat = np.linalg.solve(ffprime, -ff_hat)

            # prepare for next loop iteration
            x.append(x[k] + l * delta_xk)
            l = min(1, 2 * l)
            k = k + 1

            # check abort condition
            if k >= kmax:
                break

        return np.array(x)
    return (damped_newton,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""**(e) Wiederholen Sie Teil (c) mit dem gedämpften Newton-Verfahren. Verwenden Sie dabei $\lambda_{\min}=10^{-10}$ und geben Sie die Werte des Dämpungsparameters aus.**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Startwert $x^{(0)} = (4,2)^T$:""")
    return


@app.cell
def _(damped_newton, f, fprime, np):
    damped_newton(
        np.array([4, 2]),
        f,
        fprime,
        tol=1e-8,
        kmax=20,
        lambda_min=10e-10
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Startwert $x^{(0)} = (4,-4)^T$:""")
    return


@app.cell
def _(damped_newton, f, fprime, np):
    damped_newton(
        np.array([4, -4]),
        f,
        fprime,
        tol=1e-8,
        kmax=20,
        lambda_min=10e-10
    )
    return


if __name__ == "__main__":
    app.run()
