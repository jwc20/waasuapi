# workatastartup-api

This api uses [NixOs](https://nixos.org/) to install the dependencies, first [follow their instructions to install](https://nixos.org/download.html#download-nix).

### Install

To install, run the following commands.

```
git@github.com:jwc20/workatastartup-api.git
cd workatastartup-api
nix-build
```

### Usage

To use the api, run the nix shell (or venv).

```
nix-shell
```

Inside the shell, you can run the example.py.

### Create a selenium client

### Scrape for startup companies

### Dependencies

```
beautifulsoup4
lxml
requests
selenium
pprintpp
```

### See Also

- [hnjobs](https://hnjobs.emilburzo.com/)
- [Who Is Hiring?](https://kennytilton.github.io/whoishiring/)
- [hn_search](https://news.ycombinator.com/item?id=10313519)

### TODO

- [x] **_(high)_** Add filtering.
- [x] **_(high)_** Get company details and available jobs from the companies search result.
- [ ] **_(medium)_** Add scroll down feature.
- [ ] **_(low)_** Convert job details into dictionary. (?)
- [ ] **_(medium)_** Add "(New Grads Ok)" option.
- [ ] **_(high)_** Add export to csv feature.
- [ ] **_(medium)_** Add more to README instructions.
- [ ] **_(low)_** AND and OR support for queries. [(Example)](https://news.ycombinator.com/item?id=10313519)

### FIXME

~~**_(low)_** Fix log in url~~ \
 ~~**_(low)_** Fix scroll down timer, display the total time (?).~~\
~~**_(high)_** Fix search query url.~~

- [ ] **_(high)_** Use typing.
