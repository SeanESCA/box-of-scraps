# tfl

This project aims to collate the travel times on public transport in London by scraping Google Maps. 

## Design and Implementation

The design and implementation were informed by the following resources.

- [Stations, stops and piers](https://tfl.gov.uk/travel-information/stations-stops-and-piers/)
- [Standard Tube map (as of 06/2025)](https://content.tfl.gov.uk/standard-tube-map.pdf)

The main program is entirely contained in `maps.py` and requires `maps.json`. All JSON files should be in the `./data` folder. The minimum data required in `maps.json` is as follows.

```
{
  "underground": {
    "bakerloo": {
      "paths": {
        "path1": {
          "url": "URL"
        } 
      }
    }
  }
}
```
All the keys, except `"paths"` and `"url"`, can be replaced by any string. The codes of the start and end of a path on the line are used in place of `"path1"` in `maps.json` for easy identification. `"URL"` must be a Google Maps URL for a specific path. For example, all the stations on a path should lie on the same underground line; additionally, there should not be any walking in the middle of the journey.
Besides `maps.py`, there are two other standalone scripts:

- `underground_wiki.py` saves the data on [this Wikipedia page](https://en.wikipedia.org/wiki/List_of_London_Underground_stations) to `underground.json`. This data comprises the names of the stations, the tube lines that pass through them, and their locations.
- `codes.py` saves the stations and their codes in [station-abbreviations.pdf](https://github.com/SeanESCA/box-of-scraps/blob/main/tfl/station-abbreviations.pdf) to `networks.json` and `stations.json`. The original file is provided by Transport for London at [Station Codes (as of 2014)](https://content.tfl.gov.uk/station-abbreviations.pdf).

## Contributing

This project will probably not be continued because I personally no longer need it. Still, if you want to help expand this project, let's get in touch!
