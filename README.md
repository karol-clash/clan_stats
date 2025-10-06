# Clan Stats

### Clan Stats is a tool that can show you Clan's clan wars score over the weeks

## Setup

You need to have python installed on your computer and added to the $PATH 

First clone the repo

`git clone https://github.com/karol-clash/clan_stats`

Enter the repo
`cd clan_stats`

Setup venv
`python -m venv .`

Activate venv
`source bin/activate` on unix-like systems

`Scripts/activate` on windows

Install dependencies
`pip install -r requirements.txt`

Create .env config file base on .env.example. Enter your Clash RoyaleAPI token
Chekout the [RoyaleAPI Proxy tutorial](https://docs.royaleapi.com/proxy.html)

## Example usage

`python clan_stats.py "#L9VRJ" 2 -csv`

