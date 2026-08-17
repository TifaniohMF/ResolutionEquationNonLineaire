"""Méthode de Newton-Raphson pour la résolution de f(x) = 0."""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import Callable

from src.exceptions import DeriveeNulleError, NonConvergenceError

logger = logging.getLogger(__name__)


@dataclass
class ResultatNewton:
    """Résultat renvoyé par :func:`newton`.

    Attributes:
        racine: Approximation de la racine trouvée.
        iterations: Nombre d'itérations effectuées.
        historique: Liste des approximations successives x_0, x_1, ...
    """

    racine: float
    iterations: int
    historique: list[float] = field(default_factory=list)


def newton(
    f: Callable[[float], float],
    df: Callable[[float], float],
    x0: float,
    tol: float = 1e-10,
    max_iter: int = 100,
) -> ResultatNewton:
    """Résout f(x) = 0 par la méthode de Newton-Raphson.

    La méthode part d'une estimation initiale x0 et applique la relation
    de récurrence x_{n+1} = x_n - f(x_n) / f'(x_n). Elle converge
    quadratiquement au voisinage d'une racine simple, à condition que
    x0 soit suffisamment proche de la solution et que f soit dérivable.

    Args:
        f: Fonction dont on cherche un zéro.
        df: Dérivée de f.
        x0: Estimation initiale de la racine.
        tol: Tolérance sur l'écart entre deux itérations successives.
        max_iter: Nombre maximal d'itérations autorisées.

    Returns:
        Un objet ResultatNewton contenant la racine approchée, le nombre
        d'itérations effectuées et l'historique des approximations.

    Raises:
        DeriveeNulleError: Si f'(x_n) s'annule au cours des itérations.
        NonConvergenceError: Si la tolérance n'est pas atteinte après
            max_iter itérations.

    Example:
        >>> resultat = newton(lambda x: x**2 - 2, lambda x: 2 * x, 1.5)
        >>> round(resultat.racine, 4)
        1.4142
    """
    historique = [x0]

    for i in range(1, max_iter + 1):
        x = historique[-1]
        dfx = df(x)

        if dfx == 0:
            raise DeriveeNulleError(
                f"Dérivée nulle à l'itération {i} (x = {x}). "
                "La méthode de Newton ne peut pas continuer."
            )

        x_new = x - f(x) / dfx
        historique.append(x_new)
        logger.debug("Itération %d : x = %.10f, f(x) = %.2e", i, x_new, f(x_new))

        if abs(x_new - x) < tol:
            return ResultatNewton(racine=x_new, iterations=i, historique=historique)

    raise NonConvergenceError(
        f"La méthode de Newton n'a pas convergé après {max_iter} itérations."
    )
    