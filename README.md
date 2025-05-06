# Flask Active Windows Logger

Ce projet est une application web Flask qui enregistre périodiquement les fenêtres actives sur le bureau. Il est conçu pour surveiller l'utilisation des applications à des fins de cybersécurité et de productivité.

## Structure du Projet

```
projet_Journal
├── app
│   ├── __init__.py
|   ├── config.py
|   ├── monitor.py
│   ├── routes.py
│   ├── logger.py
│   ├── templates
│   │   └── index.html
│   ├── static
│   │   ├── css
│   │   │   └── styles.css
│   │   └── js
│   │       └── scripts.js
├── logs
│   └── active_windows.log
├── requirements.txt
├── run.py
└── README.md
```

## Fonctionnalités

- **Journalisation des fenêtres actives** : Enregistre périodiquement les fenêtres actives sur le bureau dans un fichier log.
- **Affichage des statistiques** : Génère un graphique des fenêtres les plus utilisées.
- **Configuration dynamique** : Permet de modifier les paramètres de journalisation via une interface utilisateur.
- **API REST** :
  - `/api/windows` : Récupère les fenêtres actives actuelles.
  - `/api/logs` : Récupère les journaux des fenêtres actives.
  - `/api/config` : Permet de consulter et de modifier la configuration.
  - `/api/window_statistics` : Génère un graphique des statistiques des fenêtres.

## Installation

1. Clonez le dépôt :
   ```bash
   git clone <url-du-depot>
   cd projet_Journal

2. Installez les dépendances requises :
   ```
   pip install -r requirements.txt
   ```

## Utilisation

1. Lancez l'application :
   ```
   python __init__.py
   ```
2. Ouvrez votre navigateur web et accédez à http://127.0.0.1:5000 pour utiliser l'application.

3. L'application affiche :

Les fenêtres actives actuelles.
Les journaux des fenêtres actives.
Un graphique des statistiques des fenêtres les plus utilisées.
Une interface pour configurer les paramètres de journalisation.

## Journalisation

Les informations sur les fenêtres actives sont enregistrées dans le fichier `logs/active_windows.log`. Chaque entrée inclut un horodatage et le nom de la fenêtre active.

## Configuration

Les informations sur les fenêtres actives sont enregistrées dans le fichier logs/active_windows.log. Chaque entrée inclut un horodatage et le nom des fenêtres actives.

Configuration
Vous pouvez configurer les paramètres suivants via l'interface utilisateur ou en modifiant le fichier config.py :

LOG_INTERVAL : Intervalle de temps (en secondes) entre chaque enregistrement.
REMOTE_SERVER_URL : URL du serveur distant pour la journalisation (si activée).
REMOTE_LOGGING : Activer ou désactiver la journalisation distante.

## Api

Endpoints disponibles :

GET /api/windows : Récupère les fenêtres actives actuelles.

GET /api/logs : Récupère les journaux des fenêtres actives.

GET /api/config : Récupère la configuration actuelle.

POST /api/config : Met à jour la configuration.

GET /api/window_statistics : Génère un graphique des statistiques des fenêtres.

## Contribution
N'hésitez pas à soumettre des issues ou des pull requests pour des améliorations ou des corrections de bugs.
## Licence

Ce projet est sous licence MIT.