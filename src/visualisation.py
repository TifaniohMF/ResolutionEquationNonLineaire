"""Outils de visualisation pour comparer la convergence des méthodes."""

from __future__ import annotations

from typing import Callable, Sequence

import matplotlib.pyplot as plt
import numpy as np


def tracer_fonction(
    f: Callable[[float], float],
    a: float,
    b: float,
    racine: float | None = None,
    titre: str = "Représentation graphique de f",
    ax: plt.Axes | None = None,
) -> plt.Axes:
    """Trace le graphe de f sur [a, b] et met en évidence une racine.

    Args:
        f: Fonction à tracer.
        a: Borne inférieure de l'intervalle affiché.
        b: Borne supérieure de l'intervalle affiché.
        racine: Si fourni, marque ce point sur l'axe des abscisses.
        titre: Titre du graphique.
        ax: Axes matplotlib existants (créés si non fournis).

    Returns:
        Les axes matplotlib utilisés, pour permettre une composition
        avec d'autres tracés.
    """
    if ax is None:
        _, ax = plt.subplots(figsize=(7, 5))

    x = np.linspace(a, b, 500)
    y = [f(xi) for xi in x]

    ax.axhline(0, color="black", linewidth=0.8)
    ax.plot(x, y, label="f(x)")
    if racine is not None:
        ax.scatter([racine], [0], color="red", zorder=5, label=f"racine ≈ {racine:.6f}")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.set_title(titre)
    ax.legend()
    ax.grid(True, alpha=0.3)
    return ax


def tracer_convergence(
    historiques: dict[str, Sequence[float]],
    valeur_exacte: float | None = None,
    titre: str = "Convergence des méthodes",
) -> plt.Axes:
    """Compare la vitesse de convergence de plusieurs méthodes.

    Trace, pour chaque méthode, l'erreur |x_n - valeur_exacte| (ou
    |x_n - x_final| si valeur_exacte n'est pas connue) en fonction du
    numéro d'itération, sur une échelle logarithmique.

    Args:
        historiques: Dictionnaire {nom_de_la_méthode: liste des x_n}.
        valeur_exacte: Valeur de référence pour calculer l'erreur. Si
            None, la dernière valeur de chaque historique est utilisée.
        titre: Titre du graphique.

    Returns:
        Les axes matplotlib utilisés.
    """
    _, ax = plt.subplots(figsize=(7, 5))

    for nom, historique in historiques.items():
        ref = valeur_exacte if valeur_exacte is not None else historique[-1]
        erreurs = [abs(x - ref) for x in historique]
        # Évite log(0) pour le dernier point qui peut être exact
        erreurs = [e if e > 0 else 1e-16 for e in erreurs]
        ax.semilogy(range(len(erreurs)), erreurs, marker="o", label=nom)

    ax.set_xlabel("Itération")
    ax.set_ylabel("Erreur |x_n - racine| (échelle log)")
    ax.set_title(titre)
    ax.legend()
    ax.grid(True, which="both", alpha=0.3)
    return ax
    