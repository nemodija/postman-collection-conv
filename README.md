# postman-collection-conv

## Eonvironment

```sh
python --version
  # Python 3.8.11
```

## Convert to markdown

### docs

**Arguments**

|Argument|Description|require|
|--|--|--|
|-c / --collection|Postman Collection file Path.|True|
|-e / --environment|Postman Environment file Paht.|-|

```sh
python markdown-docs.py -c <postman-collection-file-path>
```

### requests

**Arguments**

|Argument|Description|require|
|--|--|--|
|-c / --collection|Postman Collection file Path.|True|
|-e / --environment|Postman Environment file Paht.|-|

```sh
python markdown-requests.py -c <postman-collection-file-path>
```
