# postman-collection-conv

## Eonvironment

```sh
python --version
  # Python 3.8.12
```

## Install

```
pip install git+https://github.com/ot-nemoto/postman-collection-conv.git
```

## Convert to markdown

### markdown-docs-gen

**Arguments**

|Argument|Description|require|
|--|--|--|
|-c / --collection|Postman Collection file Path.|True|
|-e / --environment|Postman Environment file Paht.|-|

```sh
markdown-docs-gen -c <postman-collection-file-path>
```

### markdown-requests-gen

**Arguments**

|Argument|Description|require|
|--|--|--|
|-c / --collection|Postman Collection file Path.|True|
|-e / --environment|Postman Environment file Paht.|-|

```sh
markdown-requests-gen -c <postman-collection-file-path>
```
