"""Tests pour la méthode de Newton-Raphson."""

import math

import pytest

from src.exceptions import DeriveeNulleError, NonConvergenceError
from src.methode_newton.newton import newton


def test_racine_carree_de_2():
    """f(x) = x^2 - 2, f'(x) = 2x, converge très précisément vers sqrt(2)."""
    resultat = newton(lambda x: x**2 - 2, lambda x: 2 * x, x0=1.5)
    assert resultat.racine == pytest.approx(math.sqrt(2), abs=1e-9)


def test_convergence_quadratique_est_rapide():
    """Newton doit converger en très peu d'itérations sur un cas simple."""
    resultat = newton(lambda x: x**2 - 2, lambda x: 2 * x, x0=1.5)
    assert resultat.iterations <= 10


def test_derivee_nulle_leve_une_erreur():
    """Partir en x0 = 0 pour f(x) = x^2 - 2 (f'(0) = 0) doit échouer proprement."""
    with pytest.raises(DeriveeNulleError):
        newton(lambda x: x**2 - 2, lambda x: 2 * x, x0=0)


def test_non_convergence_avec_peu_diterations():
    """Un budget d'itérations trop faible doit lever NonConvergenceError."""
    with pytest.raises(NonConvergenceError):
        newton(lambda x: x**2 - 2, lambda x: 2 * x, x0=1.5, tol=1e-15, max_iter=1)


def test_racine_fonction_trigonometrique():
    """f(x) = sin(x), racine attendue proche de pi."""
    resultat = newton(math.sin, math.cos, x0=3.0)
    assert resultat.racine == pytest.approx(math.pi, abs=1e-6)


def test_historique_commence_par_x0():
    """Le premier élément de l'historique doit être la valeur initiale."""
    resultat = newton(lambda x: x**2 - 2, lambda x: 2 * x, x0=1.5)
    assert resultat.historique[0] == 1.5
    