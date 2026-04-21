import numpy as np

def dichotomie(f, a, b, tol=1e-7, max_iter=1000):
    """
    Résout f(x) = 0 par la méthode de dichotomie dans l'intervalle [a, b].

    Paramètres :
    - f : fonction à résoudre
    - a, b : bornes de l'intervalle (doivent être telles que f(a) * f(b) < 0)
    - tol : tolérance sur la largeur de l'intervalle
    - max_iter : nombre maximum d'itérations

    Retourne :
    - Approximation de la racine, ou None si échec
    """
    if f(a) * f(b) >= 0:
        raise ValueError("La fonction doit changer de signe entre a et b.")

    for _ in range(max_iter):
        milieu = (a + b) / 2
        if abs(b - a) <= tol:
            return milieu
        if f(milieu) * f(a) > 0:
            a = milieu
        else:
            b = milieu

    raise RuntimeError("La méthode n'a pas convergé après {} itérations.".format(max_iter))
"""
def dichotomie_visualisation(f,a,b,tol=1e-7):
    if f(a)*f(b) > 0:
        print("Erreur : la fonction ne change pas de signe")
        return None
    
    historique_milieu = []
    # On itere jusqu'a l'approximation
    milieu = (a+b)/2
    while milieu > tol :
            historique_milieu.append(milieu)

            if f(milieu) == 0:
                 break
            elif f(a)*f(milieu) < 0:
                 b = milieu
            else:
                 a = milieu
    return historique_milieu
"""