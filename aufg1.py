import marimo

__generated_with = "0.12.10"
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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Startwert $x^{(0)} = (4,-4)^T$:""")
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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""**(e) Wiederholen Sie Teil (c) mit dem gedämpften Newton-Verfahren. Verwenden Sie dabei $\lambda_{\min}=10^{-10}$ und geben Sie die Werte des Dämpungsparameters aus.**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Startwert $x^{(0)} = (4,2)^T$:""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Startwert $x^{(0)} = (4,-4)^T$:""")
    return


if __name__ == "__main__":
    app.run()
