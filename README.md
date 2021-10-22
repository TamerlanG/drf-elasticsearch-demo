# Elasticsearch + DRF Demo
Simple demo illustrating how to integrate elasticsearch with django-rest-framework.
We create three simple functionalities.
1. Search 
2. Filtration
3. Autocomplete

## Requirements
- Docker
- Docker-Compose
## Installation
```commandline
docker-compose up -d 
```

### Usage 
####Search
````/article-search?search=programming````
####Filter
```/article-search?category=2```
####Auto-Complete
```/article-search/suggest?title__completion=how ```