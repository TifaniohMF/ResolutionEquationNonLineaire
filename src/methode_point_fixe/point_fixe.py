"""Méthode du point fixe pour la résolution de x = g(x)."""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import Callable

from src.exceptions import NonConvergenceError

logger = logging.getLogger(__name__)


@dataclass
class ResultatPointFixe:
    """Résultat renvoyé par :func:`point_fixe`.

    Attributes:
        racine: Approximation du point fixe trouvé.
        iterations: Nombre d'itérations effectuées.
        historique: Liste des approximations successives x_0, x_1, ...
    """

    racine: float
    iterations: int
    historique: list[float] = field(default_factory=list)


def point_fixe(
    g: Callable[[float], float],
    x0: float,
    tol: float = 1e-8,
    max_iter: int = 50,
) -> ResultatPointFixe:
    """Résout x = g(x) par la méthode itérative du point fixe.

    Une équation f(x) = 0 doit d'abord être réécrite sous la forme
    x = g(x). La méthode converge si g est contractante au voisinage
    du point fixe (condition suffisante : |g'(x)| < 1).

    Args:
        g: Fonction de point fixe (x = g(x)).
        x0: Estimation initiale.
        tol: Tolérance sur l'écart entre deux itérations successives.
        max_iter: Nombre maximal d'itérations autorisées.

    Returns:
        Un objet ResultatPointFixe contenant le point fixe approché, le
        nombre d'itérations effectuées et l'historique des approximations.

    Raises:
        NonConvergenceError: Si la tolérance n'est pas atteinte après
            max_iter itérations (souvent le signe que g n'est pas
            contractante autour de la racine cherchée).

    Example:
        >>> import math
        >>> resultat = point_fixe(math.cos, 0.5)
        >>> round(resultat.racine, 4)
        0.7391
    """
    historique = [x0]

    for i in range(1, max_iter + 1):
        x = historique[-1]
        x_new = g(x)
        historique.append(x_new)
        logger.debug("Itération %d : x = %.10f, g(x) = %.10f", i, x_new, g(x_new))

        if abs(x_new - x) < tol:
            return ResultatPointFixe(racine=x_new, iterations=i, historique=historique)

    raise NonConvergenceError(
        f"La méthode du point fixe n'a pas convergé après {max_iter} itérations. "
        "Vérifiez que g est contractante au voisinage de la racine cherchée."
    )
    