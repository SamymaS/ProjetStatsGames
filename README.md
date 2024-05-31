# ProjetStatsGames
Ceci est un side project pour m'améliorer sur différentes technos.

Intégrer un site de suivi de statistiques de jeu avec un forum de discussion pour passionnés de jeux vidéo.

### 1. Planification et Conception

#### 1.1 Définir les Objectifs
- **Suivi de Statistiques** : Permettre aux utilisateurs de suivre leurs performances dans les jeux vidéo.
- **Forum de Discussion** : Offrir une plateforme pour que les utilisateurs discutent et partagent des informations.

#### 1.2 Structurer les Fonctionnalités

- **Statistiques de Jeu** :
    - Tableau de bord avec graphiques et statistiques.
    - Intégration avec des API de jeux pour récupérer les données.
    - Comparaison des performances avec des amis.

- **Forum** :
    - Création et gestion de sujets de discussion.
    - Système de votes et de commentaires.
    - Notifications en temps réel pour les nouvelles réponses.

#### 1.3 Choisir les Technologies

- **Front-end** : React (statistiques) et Vue.js (forum)
- **Back-end** : Node.js (statistiques) et Django avec Django REST Framework (forum)
- **Graphiques** : Chart.js
- **Base de données** : MongoDB
- **Notifications en Temps réel** : WebSockets

### 2. Mise en Place de l'Environnement de Développement

#### 2.1 Initialisation des Projets

- **Back-end Django** :
    - Créer un projet Django.
    - Configurer Django REST Framework.
    - Configurer les modèles et les vues pour le forum.

- **Front-end React** :
    - Initialiser un projet React.
    - Configurer React Router pour la navigation.
    - Installer Chart.js pour les graphiques.

- **Front-end Vue.js** :
    - Initialiser un projet Vue.js.
    - Configurer Vue Router pour la navigation.

### 3. Développement des Fonctionnalités

#### 3.1 Développement du Suivi de Statistiques

- **API Intégration** : Intégrer les API des jeux vidéos pour récupérer les données des utilisateurs.
- **Tableau de Bord** : Développer le tableau de bord avec React et affichez les statistiques avec Chart.js.
- **Comparaison de Performances** : Ajouter des fonctionnalités pour comparer les performances avec celles des amis.

#### 3.2 Développement du Forum

- **Modèles Django** : Créer les modèles pour les sujets, les messages, les votes et les utilisateurs.
- **API REST** : Développer les endpoints pour créer, récupérer, mettre à jour et supprimer des sujets et des messages.
- **Interface Vue.js** : Créer les composants Vue.js pour afficher les sujets, les messages et gérer les interactions des utilisateurs.
- **Notifications en Temps Réel** : Utiliser WebSockets pour mettre en place les notifications en temps réel.

### 4. Intégration des Deux Projets

#### 4.1 Authentification Unique

- **Authentification Utilisateur** : Utiliser un système d'authentification centralisé pour les deux parties du site. Par exemple, vous pouvez utiliser JWT (JSON Web Tokens) pour gérer les sessions utilisateur.
- **Partage de Données** : S'assurer que les données utilisateur sont cohérentes entre les deux systèmes.

#### 4.2 Navigation et Interface Utilisateur

- **Design Cohérent** : Utiliser un framework CSS comme Bootstrap ou Tailwind pour assurer une apparence cohérente sur tout le site.
- **Navigation** : Intégrer les routes de React et Vue.js dans une barre de navigation commune.

### 5. Test et Déploiement

#### 5.1 Tests

- **Unitaires et Intégration** : Écrire des tests unitaires et d'intégration pour les deux systèmes.
- **Tests de Performance** : S'assurer que le site peut gérer la charge des utilisateurs actifs.

#### 5.2 Déploiement

- **Serveurs** : Utiliser des services comme Heroku, AWS ou DigitalOcean pour déployer vos applications.
- **CI/CD** : Configurer une pipeline CI/CD pour automatiser le déploiement et les tests.

### 6. Maintenance et Évolution

#### 6.1 Collecte de Retours

- **Feedback Utilisateur** : Recueillir les retours des utilisateurs pour améliorer les fonctionnalités existantes et en ajouter de nouvelles.
- **Bug Tracking** : Utiliser des outils de suivi des bugs pour gérer les problèmes et les résoudre rapidement.

#### 6.2 Mise à Jour

- **Mise à Jour Régulière** : Garder les dépendances du code à jour pour des raisons de sécurité et de performance.
- **Nouvelles Fonctionnalités** : Planifier et développer de nouvelles fonctionnalités en fonction des retours et des besoins des utilisateurs.



============================



### Structure des Fichiers
    ProjetStatsGames/
    │
    ├── forum/
    │   └── ... __pychache__/
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   ├── wsgi.py
    │
    ├── forum_app/
    │   └── ... __pychache__/
    │   └── ... migrations/
    │   ├── init.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── serializers.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    │
    ├── frontend/
    │   └──  src/
    │        └── ... components/
    │        │        └──LoginForm.js
    │        │        └──RegistrationForm.js
    │        └── ... utils/
    │        │       └──api.js
    │        ├── App.css
    │        └── app.js
    │
    ├── ... node_modules/
    ├── ... txt/
    ├── ... venv/   
    │   
    ├── db.sqlite3 
    ├── manage.py
    ├── package.json
    ├── package-lock.json
    ├── start.bat
    │  
    │    
    └── README.md
    └── ... 
> Cette strucure risque d'évoluer au fur et à mesure que le projet avance (je ne fixe pas de deadline pour le moment)

============================

### Résumé des Étapes

- Configurer les routes d'authentification JWT dans le fichier `urls.py` du projet principal (`forum/urls.py`).
- Inclure les routes de l'application `forum_app` dans `forum/urls.py`.
- Définir les routes spécifiques à l'application dans le fichier `forum_app/urls.py`.


============================

### Rappel

 adresse http://127.0.0.1:8000/
 /admin
 /api

 Démarer le serveur django : `cmd venv\forum python manage.py runserver`

 Redémarrer le serveur Django : (Ctrl+c) pour arrêter le processus dans l'invite de commandes puis `cmd venv\forum python manage.py runserver`

 SuperUser : id `supersamyb` mdp `superadmin` (maj ?)

### Git 

- **git init** : Initialise un nouveau repository Git local.
- **git add** . : Ajoute tous les fichiers et dossiers du projet au suivi de Git.
- **git commit -m "Initial commit"** : Crée un commit avec un message décrivant ce commit.
- **git remote add origin** https://github.com/SamymaS/ProjetStatsGames.git : Ajoute le remote appelé origin pointant vers votre repository GitHub.
- **git push -u origin main**: Pousse les commits locaux vers la branche main sur le remote origin et définit main comme la branche par défaut pour les futures opérations de push et pull.
