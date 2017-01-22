# All The Swift Files

This repos contains scripts that fetches all `.swift` files from popular Github
repos. One reason to having them is to study use pattern of Swift's language
features.

## Usage

Run `make`, wait for the command to finish. Then `sources` directory will
contain (only) Swift files from Swift projecs hosted on Github with 5000+ stars.

## Advanced Usage

### Include private repo

Add `clone_url` and `name` for your repo in `5k_repos.json`. Or create your own
JSON list to use in place of `5k_repos.json`. Path to this file is the
commandline argument to `fetch_sources.py`.

### Up-to-date repos list

The script `get_repos.py` can fetch list of repositories with a minimal number
of stars. You need to have a personal Github access token to use it. For
example, an up-to-date content of `5k_repos.py` can be obtained by running

```
python YOUR_GITHUB_TOKEN 5000 > 5k_repos.json
```
