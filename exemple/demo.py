"""Démonstration : résolution de f(x) = x^3 - x - 2 par les trois méthodes,
avec comparaison graphique de leur convergence.

Exécution :
    python examples/demo.py
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt

from src.methode_dichotomie.dichotomie import dichotomie
from src.methode_newton.newton import newton
from src.methode_point_fixe.point_fixe import point_fixe
from src.visualisation import tracer_convergence, tracer_fonction


def f(x: float) -> float:
    return x**3 - x - 2


def df(x: float) -> float:
    return 3 * x**2 - 1


def g(x: float) -> float:
    # Réécriture de x^3 - x - 2 = 0 sous la forme x = g(x)
    return (x + 2) ** (1 / 3)


def main() -> None:
    resultat_dichotomie = dichotomie(f, 1, 2)
    resultat_newton = newton(f, df, x0=1.5)
    resultat_point_fixe = point_fixe(g, x0=1.5)

    print(f"Dichotomie : racine = {resultat_dichotomie.racine:.8f} "
          f"({resultat_dichotomie.iterations} itérations)")
    print(f"Newton     : racine = {resultat_newton.racine:.8f} "
          f"({resultat_newton.iterations} itérations)")
    print(f"Point fixe : racine = {resultat_point_fixe.racine:.8f} "
          f"({resultat_point_fixe.iterations} itérations)")

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))

    tracer_fonction(
        f, 0.5, 2.5,
        racine=resultat_newton.racine,
        titre="f(x) = x³ - x - 2",
        ax=ax1,
    )

    tracer_convergence(
        {
            "Dichotomie": resultat_dichotomie.historique,
            "Newton": resultat_newton.historique,
            "Point fixe": resultat_point_fixe.historique,
        },
        valeur_exacte=resultat_newton.racine,
        titre="Comparaison de la vitesse de convergence",
    )
    plt.sca(ax2) if False else None  # (le 2e subplot est géré par tracer_convergence)

    fig.tight_layout()
    sortie = Path(__file__).resolve().parent.parent / "docs" / "images" / "convergence.png"
    sortie.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(sortie, dpi=150)
    print(f"\nGraphique enregistré dans {sortie}")


if __name__ == "__main__":
    main()
    