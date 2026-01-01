# London Train Travel

## Aims

-   To acquire a complete data set of the travel times via public transport,
    as well as the means to update this data set with minimal effort.

-   To determine all stations and areas within a given travel time from a given station.

-   To predict the shortest route via public transport using the A* algorithm.

## Important Links

-   [Stations, stops and piers](https://tfl.gov.uk/travel-information/stations-stops-and-piers/)

-   [Standard Tube map (as of 06/2025)](https://content.tfl.gov.uk/standard-tube-map.pdf)

-   [Station codes (as of 2014)](https://content.tfl.gov.uk/station-abbreviations.pdf)

## Methodology

-   Acquire travel times by scraping Google Maps.

-   Store coordinates of every station with respect to every line.

## Checklist

### Travel Times

#### Underground

- [x] Bakerloo
- [x] Central
- [x] Circle
- [x] District
- [x] Jubilee
- [x] Metropolitan
- [x] Northern
- [x] Piccadilly
- [x] Victoria
- [x] Waterloo and City

#### Overground

- [x] Liberty
- [x] Lioness
- [ ] Mildmay
- [x] Suffragette
- [ ] Weaver
- [ ] Windrush

#### Misc

- [ ] Elizabeth
- [ ] London Trams
- [ ] Thameslink

### Node Positions

#### Underground

- Bakerloo
    - [ ] Elephant & Castle to Harrow & Wealdstone
- Central
    - [ ] West Ruislip to Leytonstone
    - [ ] Leytonstone to Snaresbrook
    - [ ] Woodford to Epping
- Circle
    - [x] Paddington to Hammersmith
    - [x] Paddington to Bayswater
- District
    - [ ] Ealing Broadway to Upminster
    - [ ] Turnham Green to Richmond
    - [ ] Wimbledon to Edgware Road
    - [ ] Earl's Court to Kensington (Olympia)
- Jubilee
    - [ ] Stanmore to Stratford
- Metropolitan
    - [ ] Amersham to Aldgate
    - [ ] Harrow-on-the-Hill to Uxbridge
    - [ ] Moor Park to Watford
    - [ ] Chalfont & Latimer to Chesham
- Northern
    - [ ] Kennington to Elephant & Castle
    - [ ] Kennington to Battersea
    - [ ] Kennington to Morden
    - [ ] Euston to Edgware
    - [ ] Camden Town to High Barnet
    - [ ] Finchley Central to Mill Hill East
- Piccadilly
    - [x] Uxbridge to Cockfosters
    - [x] Acton Town to Hatton Cross
    - [x] Hatton Cross to Heathrow Terminals 2 & 3
    - [x] Heathrow Terminal's 2 & 3 to Heathrow Terminal 5.
- Victoria
    - [ ] Brixton to Walthamstow Central
- W&C
    - [ ] Waterloo to Bank

#### Misc

- Elizabeth
- London Trams
- Thameslink
- Liberty
- Lioness
- Mildmay
- Suffragette
- Weaver
- Windrush