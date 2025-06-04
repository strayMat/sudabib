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

Base de données [OpenAlex](https://openalex.org/), qui est une base de données ouverte d'articles scientifiques, de revues, d'auteurs et d'institutions. Elle est utilisée pour extraire des informations pertinentes sur les publications scientifiques.

### Schéma flux de données (optionnel)

### Technologies

python, [openalex api](https://docs.openalex.org/), llm, ollama, mistral 

### Maintenance

> - Projet en développement actif

## Contacts

matt.dout@gmail.com

## Détails techniques

### Installation and simple usage of LLM

- Installation: 

```
uv add llm
uv run llm install llm-mistral # install mistral plugin
uv run llm keys set mistral # go there for creating an API key for mistral
```

- Usage: `uv run llm -m mistral-small "tell me a joke about pelican"` 

- Paramètre un modèle par défaut : `uv default mistral-small`

### En utilisant un serveur Ollama (permet d'avoir un modèle local instancié ie. chargé en mémoire) 

- Installer Ollama : `curl -fsSL https://ollama.com/install.sh | sh`

- Télécharger un modèle en local, par exemple, Llama 3.1 1B : `ollama pull llama3.2:1b`

- Installer le plugin Ollama pour LLM : `llm install llm-ollama`

- Poser une question: `llm -m llama3.2:1b 'How much is 2+2?'