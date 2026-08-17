"""Méthode de dichotomie (bissection) pour la résolution de f(x) = 0."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable

from src.exceptions import IntervalleInvalideError, NonConvergenceError


@dataclass
class ResultatDichotomie:
    """Résultat renvoyé par :func:`dichotomie`.

    Attributes:
        racine: Approximation de la racine trouvée.
        iterations: Nombre d'itérations effectuées.
        historique: Liste des milieux successifs (utile pour tracer
            la convergence).
    """

    racine: float
    iterations: int
    historique: list[float] = field(default_factory=list)


def dichotomie(
    f: Callable[[float], float],
    a: float,
    b: float,
    tol: float = 1e-7,
    max_iter: int = 1000,
) -> ResultatDichotomie:
    """Résout f(x) = 0 par la méthode de dichotomie (bissection) sur [a, b].

    La méthode suppose que f est continue sur [a, b] et que f(a) et f(b)
    sont de signes opposés (théorème des valeurs intermédiaires), ce qui
    garantit l'existence d'au moins une racine dans l'intervalle.

    Args:
        f: Fonction dont on cherche un zéro.
        a: Borne inférieure de l'intervalle de recherche.
        b: Borne supérieure de l'intervalle de recherche.
        tol: Tolérance sur la largeur de l'intervalle final.
        max_iter: Nombre maximal d'itérations autorisées.

    Returns:
        Un objet ResultatDichotomie contenant la racine approchée,
        le nombre d'itérations effectuées et l'historique des milieux.

    Raises:
        IntervalleInvalideError: Si f(a) et f(b) sont de même signe.
        NonConvergenceError: Si la tolérance n'est pas atteinte après
            max_iter itérations.

    Example:
        >>> resultat = dichotomie(lambda x: x**2 - 2, 0, 2)
        >>> round(resultat.racine, 4)
        1.4142
    """
    fa, fb = f(a), f(b)
    if fa * fb > 0:
        raise IntervalleInvalideError(
            f"f(a) et f(b) doivent être de signes opposés "
            f"(f({a})={fa}, f({b})={fb})."
        )

    historique: list[float] = []
    milieu = (a + b) / 2

    for i in range(1, max_iter + 1):
        milieu = (a + b) / 2
        historique.append(milieu)
        f_milieu = f(milieu)

        if f_milieu == 0 or abs(b - a) / 2 <= tol:
            return ResultatDichotomie(racine=milieu, iterations=i, historique=historique)

        if fa * f_milieu < 0:
            b = milieu
        else:
            a, fa = milieu, f_milieu

    raise NonConvergenceError(
        f"La dichotomie n'a pas convergé après {max_iter} itérations."
    )
    