# 🎯️ Résolution d'équation non linéaire

Ce projet propose une implémentation en python de différents méthode numérique perméttant de trouver les racines (zéros) des équations non linéaire de type $f(x)=0$


## 🚀 À propos du projet

La résolution d'équation non linéaire est la pilier de l'analyse numérique. Ces dépôt regroupe les algorithmes les plus couramment utilisés, offrant la simplicité de mise en œuvre et la rapidité de convergence.

## 🛠️ Méthode implementé

Le projet inclus les algorithmes suivants:
1. **Méthode de la dichotomie (ou bissection)**
- Principe: divise l'intervalle en deux à chaque étape
- Avantage: convergence garantie si la fonction est continue et change de signe à chaque étape
- Inconvénient: convergence relativement lent

2. **Méthode de Newton**
- Principe: utilise la dérivée d'une fonction pour trouver une approximation linéaire
- Avantage: convergence très rapide
- Inconvénient: nécessite la connaissance du dérivée $f^{'}(x)$

3. **Méthode du point fixe**
- Principe: trouver une équation simple ayant même solution que $f(x)$
- Avantage: convergence rapide
- Inconvénient: recherche d'une autre équation ayant la même solution 

## 📋 Prérequis
Pour exécuter ces scripts, vous devez avoir **Python 3.x** installer ainsi que les bibliothèques suivantes (si vous utilisez des fonctions mathématiques complexes et des graphiques)

```bash
pip install numpy matplotlib
```
## 📁️ Structure de projet

```text
ResolutionSystemeLineaire/
├── README.md
├── docs
│   ├── ResolutionEquationNonLineaire.pdf
│   └── ResolutionEquationNonLineaire.tex
└── src
    ├── methode_dichotomie 
    │   ├── dichotomie.ipynb
    │   └── dichotomie.py
    ├── methode_newton
    │   ├── newton.ipynb
    │   └── newton.py
    └── methode_point_fixe
        ├── point_fixe.ipynb
        └── point_fixe.py
```

## 💻 Installation et utilisation 
1. Cloner le dépôt 

```bash
git clone https://github.com/TifaniohMF/ResolutionEquationNonLineaire.git
cd ResolutionEquationNonLineaire
```

2. Exécuter un script 

```bash
python3 newton.py
```

## 📊 Exemple de configuration 

Dans la plupart des scripts vous pouvez modifier les paramètres suivants :
- f : la fonction à résoudre
- a, b : l'intervalle initial pour la dichotomie 
- x0 : le point de départ pour Newton
- tol : pour la précision souhaité
- max_iter: nombre maximal d'itération 

## 🤝 Contribution
Les contributions sont les bienvenus ! Si vous souhaite ajouter une méthode ou les améliorer les codes existant :
1. Forkez le projet
2. Créer votre branche de fonctionnalités
```bash
git checkout -b feature/Nouvelle méthode
```
5. Commite vos changements
```bash
git commit -m "feat : ajout de la méthode X"
```
7. Pushez vers la branche
```bash
git push origin feature/NouvelleMethode
```
8. Ouvrez une pull requests

### Contact
**TifaniohMF**- [Profil Github](https://github.com/TifaniohMF)
