# Let's JA#m

The web-application for a jam session and learning of music

## Description

The application outputs chords for joint play of several musicians, or for self-practice solo or rhythm parts. You just go to the site, choose the settings, start the generation and play. The screen will show the chord that is being played in the songs and you will need to either play it (rhythm part) or play along with it (solo part). 

We also have at our disposal:
* Metronome (sound and / or visual)
* Phonogram
* Choice of complexity of the composition 

## Architecture

The application consists of two microservices:
* [backend](https://github.com/Piknik1990/jam/blob/arch/backend/README.md) - generates a composition based on the entered data
* [frontend](https://github.com/Piknik1990/jam/blob/arch/frontend/README.md) - displays and, optionally, plays the generated composition  

`Users` -(HTTP(S))-> `Frontend` -(REST API)-> `Backend`

### Backend

Communication between backend and frontend takes place via REST API. The communication format is described below in a separate section of the article.


### Frontend

### Users

### HTTP(S)

### REST API

### Docker

These parts of the application are packed into separate Docker images and play the role of microservices. Frontend and Backend have a `Dockerfile` for creating a Docker Image.


## Installion

## License
