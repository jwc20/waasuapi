# workatastartup-api

This api uses [NixOs](https://nixos.org/) to install the dependencies, first [follow their instructions to install](https://nixos.org/download.html#download-nix).

## Install

To install, run the following commands.

```
git@github.com:jwc20/workatastartup-api.git # Clone the repo
cd workatastartup-api
nix-build                                   # Install requirements.
(Or start a python venv and run pip3 install -r requirements.txt)
```

# Usage

To use the api, run the nix shell (or venv).

```
nix-shell
```

Inside the shell, you can run the example.py.

### TODO

- #### Create a selenium client

- #### Scrape for startup companies

## TODO

- [x] **_(high)_** Add filtering.
- [x] **_(high)_** Get company details and available jobs from the companies search result.
- [ ] **_(medium)_** Add scroll down feature.
- [ ] **_(low)_** Convert job details into dictionary. (?)
- [ ] **_(medium)_** Add "(New Grads Ok)" option.
- [ ] **_(high)_** Add export to csv feature.
- [ ] **_(medium)_** Add more to README instructions.

## FIXME

~~**_(low)_** Fix log in url~~ \
 ~~**_(low)_** Fix scroll down timer, display the total time (?).~~\
~~**_(high)_** Fix search query url.~~
