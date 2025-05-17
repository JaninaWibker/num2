import marimo

__generated_with = "0.13.6"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Notebook zu Potenzenmethode & Rayleigh-Quotienten-Iteration""")
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    import numpy as np
    import scipy.linalg as spla
    return np, spla


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Wir betrachten die Matrizen
    $$A = \begin{pmatrix} 5 & 4 & 4 & 5 \\ 9 & 4 & 8 & 3 \\ -9 & -4 & -8 & -5 \\ 0 & 1 & 1 & 2 \end{pmatrix} \qquad \text{und} \qquad
    B = \begin{pmatrix} 5 & 4 & 4 & 5 \\ 6 & 4 & 5 & 3 \\ -6 & -4 & -8 & -5 \\ 0 & 1 & 1 & 2 \end{pmatrix}.$$

    Anhand dieser Matrizen wollen wir die Verfahren zur Approximation von Eigenwerten testen und verstehen. 

    **(a) Um die Ergebnisse der Verfahren später beurteilen zu können, lassen Sie sich von Python zunächst die "korrekten" Eigenwerte berechnen und anzeigen. Benutzen Sie dazu den Befehl `eig` aus dem `linalg` Modul von `scipy`. Da dieses Modul oben mit dem Namen `spla` eingebunden wurde, wird der Befehl also über `spla.eig(...)` aufgerufen.**
    """
    )
    return


@app.cell
def _(np, spla):
    A = np.array([[5.0, 4, 4, 5],[9, 4, 8, 3],[-9, -4, -8, -5],[0, 1, 1, 2]])
    B = np.array([[5.0, 4, 4, 5],[6, 4, 5, 3],[-6, -4, -5, -5],[0, 1, 1, 2]])
    print(A)
    print(B)

    print(spla.eig(A))
    print(spla.eig(B))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Potenzenmethode""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""**(b) Schreiben Sie eine Prozedur, die `K` Iterationen der Potenzenmethode für eine Matrix `A` und einen Startvektor `z0` berechnet. Die Prozedur soll die aktuelle Approximation an den Eigenwert in jedem Schritt auf dem Bildschirm ausgeben, und am Ende die finale Approximationen an den Eigenwert und den Eigenvektor an das Hauptprogramm zurückgeben.**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""**Hinweis:** Das komplexe Skalarprodukt $x^H y = \overline{x}^T y$ zweier Vektoren $x$ und $y$ erhalten Sie in numpy durch `np.vdot(x,y)`.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Außerdem ein kleiner Tipp, _falls_ Sie an einer schönen Bildschrimausgabe interessiert sind: In sogenannten "F-Strings" können Sie die Darstellung von Zahlen in Strings (also z.B. für den `print`-Befehl) beeinflussen. Ein Beispiel:""")
    return


@app.cell
def _(np):
    a = np.sqrt(2) 
    print('Die Variable hat den Wert',a)
    print(f'Die Variable hat den Wert {a:.3f}')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""In der zweiten Variante wurde die Darstellung der in `a` gespeicherten Zahl spezifiziert. Das führende `f` vor dem String erlaubt solche Formatierungen. Die geschweiften Klammern stellen einen Platzhalter für eine Zahl, die formatiert ausgegeben werden soll, dar. Vor dem Doppelpunkt wird angegeben, welche Variable ausgegeben werden soll, und dahinter wird spezifiziert in welcher Darstellung. Das `f` steht für eine Fix point number (das Komma trennt also immer den ganzahligen Teil von dem Rest). Der Zusatz `.3` legt genauer fest, dass 3 Nachkommastellen nach dem Dezimalpunkt angezeigt werden sollen.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""**(c) Testen Sie die Prozedur mit den obigen Matrizen $A$ und $B$. Starten Sie dabei mit einem beliebigen Vektor, z.B. $z_0 = (1,1,1,1)^T$, und berechnen Sie 30 Iterationen. Gegen welchen Eigenwert von $A$ bzw. $B$ konvergiert die Methode, und warum? Vergleichen und erklären Sie die Konvergenzgeschwindigkeiten. Überprüfen Sie außerdem den Fehler der finalen Approximationen $\lambda,v$ an Eigenwert und Eigenvektor, indem Sie den Wert von $\left\lVert Av-\lambda v \right\rVert_2$ für die jeweilige Matrix ausgeben.**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Inverse Potenzenmethode mit Shift""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    **(d) Schreiben Sie nun eine Prozedur, welche einen zusätzlichen Eingabeparameter $\mu$ hat und die inverse Potenzenmethode mit Shift $\mu$ durchführt.**

    Zur Lösung der auftretenden LGS verwenden wir eine LR-Zerlegung. Für eine Matrix $A$ erhalten Sie diese über den Befehl, `spla.lu(A)`, welcher drei Matrizen $P,L,R$ (Permutationsmatrix, untere und obere Dreiecksmatrix) zurückgibt, für die $A = PLR$ gilt. ACHTUNG: Aus der VL kennen wir die Zerlegung in der Form $PA=LR$!

    Mit dem Befehl `solve_triangular(A,b,lower=True)` bzw. `solve_triangular(A,b,lower=False)` können Sie dann LGS mit einer unteren/oberen Dreiecksmatrix durch Vorwärts- bzw. Rückwärtssubstitution lösen lassen.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""**(e) Testen Sie Ihre Prozedur wie oben mit der Matrix $A$. Verwenden Sie als Shift zunächst $\mu = 4$. Was beobachten Sie im Vergleich zu oben? Verwenden Sie anschließend die Shifts $\mu = -3$ und $\mu = 0$. Was passiert und warum?**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Rayleigh-Quotienten-Iteration""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    **(f) Kopieren Sie Ihre Prozedur aus Teil (d) und ändern Sie diese zur Rayleigh-Quotienten-Iteration ab. Testen Sie diese wie in Teil (e). Verwenden Sie auch einmal einen besonders schlechten Shift, z.B. $\mu = 100$.**

    Ggf. sollten Sie noch ein Abbruchkriterium ergänzen, z.B. falls $\left\lVert Av-\lambda v \right\rVert_2<10^{-14}$ für die aktuelle Approximation $\lambda,v$ an Eigenwert und Eigenvektor gilt (sonst kann die Matrix $\mu I - A$ irgendwann singulär werden).
    """
    )
    return


if __name__ == "__main__":
    app.run()
