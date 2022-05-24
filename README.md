# yoshiken.dev

The source of [yoshiken.dev](https://yoshiken.dev/).

## build


fish

```sh
docker pull yoshiken/yoshiken.dev.python
docker run -v (pwd)/content:/app/content:ro -v (pwd)/docs:/app/docs -v (pwd)/template:/app/template yoshiken/yoshiken.dev.python
```

bash

```sh
docker pull yoshiken/yoshiken.dev.python
docker run -v $(pwd)/content:/app/content:ro -v $(pwd)/docs:/app/docs -v $(pwd)/template:/app/template yoshiken/yoshiken.dev.python
```
