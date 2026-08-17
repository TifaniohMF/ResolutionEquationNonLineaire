"""Tests d'intégration : cohérence entre les différentes méthodes."""

import math

import pytest

from src.methode_dichotomie.dichotomie import dichotomie
from src.methode_newton.newton import newton
from src.methode_point_fixe.point_fixe import point_fixe


def test_les_trois_methodes_convergent_vers_la_meme_racine():
    """Sur f(x) = x^2 - 2, les trois méthodes doivent toutes converger
    vers sqrt(2) à leur tolérance respective près."""
    racine_dichotomie = dichotomie(lambda x: x**2 - 2, 1, 2).racine
    racine_newton = newton(lambda x: x**2 - 2, lambda x: 2 * x, x0=1.5).racine
    racine_point_fixe = point_fixe(lambda x: (x + 2 / x) / 2, x0=1.0).racine

    reference = math.sqrt(2)
    assert racine_dichotomie == pytest.approx(reference, abs=1e-6)
    assert racine_newton == pytest.approx(reference, abs=1e-6)
    assert racine_point_fixe == pytest.approx(reference, abs=1e-6)


def test_newton_converge_plus_vite_que_dichotomie():
    """Newton (convergence quadratique) doit nécessiter significativement
    moins d'itérations que la dichotomie (convergence linéaire) pour une
    précision comparable."""
    resultat_newton = newton(lambda x: x**2 - 2, lambda x: 2 * x, x0=1.5, tol=1e-10)
    resultat_dichotomie = dichotomie(lambda x: x**2 - 2, 1, 2, tol=1e-10)

    assert resultat_newton.iterations < resultat_dichotomie.iterations
    