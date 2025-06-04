# sudabib


[![Build status](https://img.shields.io/github/actions/workflow/status/strayMat/sudabib/main.yml?branch=main)](https://github.com/strayMat/sudabib/actions/workflows/main.yml?query=branch%3Amain)
[![codecov](https://codecov.io/gh/strayMat/sudabib/branch/main/graph/badge.svg)](https://codecov.io/gh/strayMat/sudabib)
[![Documentation](https://img.shields.io/badge/docs-latest-blue.svg)](https://strayMat.github.com/sudabib/)
[![License](https://img.shields.io/github/license/strayMat/sudabib)](https://img.shields.io/github/license/strayMat/sudabib)


> 📝 **Note**
> Utilisez le français pour tout le contenu de ce projet

---

## Description

> - Projet d'exploration des outils llm pour la revue de littérature en interfaçant des llm avec la librarie openalex en utilisant comme pont entre les deux la [librairie llm de Simon Willison](https://github.com/simonw/llm)
> - Livrables : Outil python entrant une requête en langage naturel concernant une question scientifique et renvoyant une réponse sourcée grâce à des abstracts d'articles scientifiques.
> - Destinataires: Chercheurs et rapporteurs pour débroussailler la revue initial de littérature. 
> - Motivation: Envie de comprendre comment marche [llm]() et envie de mieux comprendre openalex.
>
> - Acteurs impliqués : NA.
> - Temporalité du projet : 2025-05-29 lazy mode 
>
> Optionnel : une image qui permet de visualiser le résultat du projet
> Ex :
>
> - capture d'écran d'un tableau de bord ou d'une application
> - figure marquante d'un rapport, etc.

## Liens utiles

- Documentation :
- Code source : 

> 📝 **Explication du contenu à rédiger**
>
> Vous pouvez aussi rajouter d'autres liens utiles : protocole, rapport d'étude, lien site internet, tutoriels, guide utilisateur

## Contexte technique

### Données utilisées

> 📝 **Explication du contenu à rédiger**
>
> Décrire les données utilisées et leur éventuelles restrictions d'accès.

### Schéma flux de données (optionnel)

### Technologies

> 📝 **Explication du contenu à rédiger**
>
> Donner quelques repères sur les technologies utilisées : langage, logiciels, éventuellement dossiers où trouver le code, etc.

### Maintenance

> 📝 **Explication du contenu à rédiger**
>
> Expliquer si le projet est maintenu et comment, par exemple parmi les alternatives suivantes :
>
> - Projet en développement actif
> - Projet finalisé ✅, sans maintenance ni modification
> - Maintenance minimale 📞, pour mettre à jour les dépendances ou en cas de problème
> - Maintenance planifiée ⏰, avec des tâches récurrentes à réaliser (auquel cas décrire les tâches et leur fréquence)

## Contacts

> 📝 **Explication du contenu à rédiger**
>
> Description des contacts importants du projet, en précisant pour chacun :
>
> - l'organisation (service, pôle, etc),
> - le rôle sur le projet,
> - le contact mail (générique et non personnel).

## Détails techniques

### Installation and simple usage of LLM

- Installation: 

```
uv add llm
uv run llm install llm-mistral # install mistral plugin
uv run llm keys set mistral # go there for creating an API key for mistral
```

- Usage:

```
ul -m mistral-small "tell me a joke about pelican"
``` 

- Paramètre un modèle par défaut, par exemple, un llama local (nécessite le téléchargement du plugin [llm-gpt4all](https://github.com/simonw/llm-gpt4all)):

```
uv run llm 

### En utilisant un serveur Ollama (permet d'avoir un modèle local instancié ie. chargé en mémoire) 

- Installer Ollama : `curl -fsSL https://ollama.com/install.sh | sh`

- Télécharger un modèle en local, par exemple, Llama 3.1 1B : `ollama pull llama3.2:1b`

- 