# About

Scrapes the passed in Smash.gg tournament URL every X seconds for all played sets in every bracket.

[Smash.gg API](https://help.smash.gg/hc/en-us/articles/217471947-API-Access)  

# Installation

`pip install requests`

# Usage

`python driver.py tournament-url [interval]`

tournament-url: The Smash.gg tournament you wish to scrape sets from.  
interval: How often you would like to scrape (in seconds). Defaults to 5 seconds.  

## Examples

#### Single-Stage Tournament

Short URL: `python driver.py https://smash.gg/nxs-3v3-sat-36/events`  
Long URL: `python driver.py https://smash.gg/tournament/nexus-gaming-saturday-150-na-3v3-weekly-tournament-36/details`  

```js tournament.json

{
  "Bracket": {      /* Pool Name */
    "426004": {     /* Group ID */
      "1": {        /* Group Name */
        "1": [...], /* Round X Matches */
        "2": [...], 
        "3": [...], 
        "4": [
          "Clueless 3-0 Orange Team", 
          "Lights Out! 2-3 HECCIN fast", 
          "Garbage 1-3 Superposition", 
          "UMD 2-3 asaah uh dude"
        ], 
        "5": [
          "Clueless 3-0 HECCIN fast", 
          "Superposition 2-3 asaah uh dude"
        ], 
        "6": [
          "Clueless 4-0 asaah uh dude"
        ]
      }
    }
  }
}

``` 

#### Multi-Stage Tournament

Short URL: `python driver.py https://smash.gg/toc`  
Long URL: `python driver.py https://smash.gg/tournament/tournament-of-champions-2/details`  

```js tournament.json
{
  "Playoffs": { /* Pool Name */
    "362947": { /* Group ID */
      "1": {    /* Group Name */
        "1": [  /* Round X Matches */
          "Take 3 2-1 Eggplant", 
          "Iris 2-0 SetToDestroyX"
        ], 
        "2": [
          "G2 Esports 3-1 Take 3", 
          "Freestylers in Disguise 0-3 Iris"
        ], 
        "3": [
          "G2 Esports 3-0 Iris"
        ]
      }
    }
  }, 
  "Qualifiers": { /* Pool Name */
    "362944": {   /* Group ID */
      "1": {...}  /* Group Name */
    }, 
    "362945": {
      "2": {...}
    }, 
    "362946": {
      "3": {...}
    }
  }
}

```