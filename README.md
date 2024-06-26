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
> Cette structure risque d'évoluer au fur et à mesure que le projet avance (je ne fixe pas de deadline pour le moment)

============================

### Résumé des Étapes

- Configurer les routes d'authentification JWT dans le fichier `urls.py` du projet principal (`forum/urls.py`).
- Inclure les routes de l'application `forum_app` dans `forum/urls.py`.
- Définir les routes spécifiques à l'application dans le fichier `forum_app/urls.py`.


============================

### Rappel

- **Lancer les tests** : `python manage.py test`
- **Activer les variables d'environnement** : `.\venv\Scripts\activate`
- **Démarer le serveur django** : `cmd venv\forum python manage.py runserver`

- **Redémarrer le serveur Django** : (Ctrl+c) pour arrêter le processus dans l'invite de commandes puis `cmd venv\forum python manage.py runserver`

- **SuperUser** : id `supersamyb` mdp `superadmin` (maj ?)



`https://dev.twitch.tv/console/apps/16c99xmtcoavl4xqx6r6n0jdf6e4zc`
API :
`https://www.igdb.com/`


tests routes 
>- `http://localhost:8000/`
>
>- `http://localhost:8000//admin/`
>
>- `http://localhost:8000/api/`
>- `http://localhost:8000/api/topics/`
>- `http://localhost:8000/api/posts/`
>- `http://localhost:8000/api/comments/`
>
>- `http://localhost:8000/oauth/authorize/`
>- `http://localhost:8000/oauth/callback/`
>
>- `http://localhost:8000/games/`

### Étape 1 : Vérifiez et Appliquez les Migrations

Créez les Migrations
Django créer les migrations nécessaires pour vos modèles en exécutant la commande suivante :

code: `python manage.py makemigrations`

Appliquez les migrations pour créer les tables dans votre base de données :
code: `python manage.py migrate`

### Étape 2 : Redémarrez le Serveur Django
Après avoir appliqué les migrations, redémarrez votre serveur Django pour vous assurer que les modifications sont prises en compte :

code: `python manage.py runserver`

Vérifiez les Tables et Testez les Routes
Une fois que les migrations sont appliquées et que le serveur est redémarré, essayez d'accéder à l'URL http://127.0.0.1:8000/api/topics/ pour vérifier que la table forum_app_topic a été correctement créée et que les données peuvent être récupérées.

Exemple de Commandes Complètes
Voici un résumé des commandes que vous devez exécuter :


`python manage.py makemigrations`
`python manage.py migrate`
`python manage.py runserver`

###Explication :
`makemigrations` : Cette commande scanne vos modèles pour toute modification et crée des fichiers de migration correspondants.
`migrate` : Cette commande applique les fichiers de migration à votre base de données, créant ainsi les tables définies dans vos modèles.
`runserver` : Cette commande démarre le serveur de développement Django.


### Git 

- `git init` : Initialise un nouveau repository Git local.
- `git add` . : Ajoute tous les fichiers et dossiers du projet au suivi de Git.
- `git commit -m "Initial commit"` : Crée un commit avec un message décrivant ce commit.
- `git remote add origin https://github.com/SamymaS/ProjetStatsGames.git` : Ajoute le remote appelé origin pointant vers votre repository GitHub.
- `git push -u origin main` : Pousse les commits locaux vers la branche main sur le remote origin et définit main comme la branche par défaut pour les futures opérations de push et pull.

### Etape par étape

- Tirer les changements de la branche main distante avec rebase :

`git pull origin main --rebase`

> - Résoudre les conflits (si nécessaire) :

Résoudre les conflits manuellement, ajouter les fichiers résolus et continuer le rebase :

`git add .`
`git rebase --continue`

Pousser la branche main mise à jour :

`git push -u origin main`

### Explications

> - `git pull origin main --rebase`: Cette commande tire les changements de la branche main distante et repositionne vos commits locaux au sommet des commits récupérés.
> - `Résoudre les conflits` : Si des conflits se produisent pendant le rebase, vous devrez les résoudre manuellement, ajouter les fichiers modifiés (git add .) et continuer le rebase (git rebase --continue).
> - `git push -u origin main` : Une fois que votre branche locale est à jour et sans conflits, cette commande pousse vos modifications vers le dépôt distant.
