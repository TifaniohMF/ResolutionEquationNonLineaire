"""Exceptions personnalisées pour les méthodes de résolution d'équations non linéaires."""


class NonConvergenceError(RuntimeError):
    """Levée quand une méthode itérative n'a pas convergé dans le nombre
    maximal d'itérations autorisé."""


class IntervalleInvalideError(ValueError):
    """Levée quand l'intervalle [a, b] fourni ne vérifie pas les conditions
    requises (ex : f(a) et f(b) de même signe pour la dichotomie)."""


class DeriveeNulleError(ZeroDivisionError):
    """Levée quand la dérivée s'annule au cours de la méthode de Newton,
    rendant l'itération suivante impossible."""
    