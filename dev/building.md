# Building

## Publish Documentation

```zsh
cd docs
quarto publish netlify
```

## My Mac

```zsh
flet build macos --build-version "0.3.1" --product DesignCTER --copyright "Copyright (c) 2024 Lightbridge-KS."
```

## Build Number

`--build-number`: an integer number (default is 1), an identifier used as an internal version number. Each build must have a unique identifier to differentiate it from previous builds. 


## Build Version

`--build-version`: "x.y.z" string (default is 1.0.0) used as the version number shown to users.