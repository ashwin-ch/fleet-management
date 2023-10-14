

# APIs supported
* Get specific vehicle information
* Check if vehicle available
* Update service required
* Check tire-pressure warning
* Update diagnostics


# Name of the image for Fleet Off Board Manager
`FleetMgr`


# Commands executed for tracking
## Build a docker
> docker build -t fleetmgr:dev .

## Run a docker image on the host network, and
> docker run --network host -d -p 5000:5000 -it fleetmgr:dev

## Curl commands for testing:
### Is vehicle available?
> curl -X GET "http://localhost:5000/vehicle/is_available/v43"

### Get vehicle info
> curl -X GET "http://localhost:5000/get_vehicle/v12"

### Get all vehicle info
> curl -X GET "http://localhost:5000/get_vehicles"

