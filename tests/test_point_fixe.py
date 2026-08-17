"""Tests pour la méthode du point fixe."""

import math

import pytest

from src.exceptions import NonConvergenceError
from src.methode_point_fixe.point_fixe import point_fixe


def test_point_fixe_cosinus():
    """x = cos(x) a pour point fixe le nombre de Dottie (≈ 0.739085)."""
    resultat = point_fixe(math.cos, x0=0.5)
    assert resultat.racine == pytest.approx(0.7390851, abs=1e-5)


def test_racine_carree_via_point_fixe():
    """g(x) = (x + 2/x) / 2 (moyenne de Héron) converge vers sqrt(2)."""
    g = lambda x: (x + 2 / x) / 2
    resultat = point_fixe(g, x0=1.0)
    assert resultat.racine == pytest.approx(math.sqrt(2), abs=1e-6)


def test_fonction_non_contractante_ne_converge_pas():
    """g(x) = x^2 n'est pas contractante autour de son point fixe non nul
    (g'(1) = 2), la méthode doit donc échouer à converger."""
    with pytest.raises(NonConvergenceError):
        point_fixe(lambda x: x**2, x0=1.5, max_iter=20)


def test_iterations_positives():
    """Le nombre d'itérations renvoyé doit être strictement positif."""
    resultat = point_fixe(math.cos, x0=0.5)
    assert resultat.iterations > 0

    def test_historique_coherent_avec_iterations(self=None):
        pass
        