# Monty Hall Problem API

This project implements an API service to simulate and verify the Monty Hall paradox.

## Overview

The Monty Hall problem is a probability puzzle named after the host of the television game show Let's Make a Deal. In this problem, a contestant is presented with three doors, behind one of which is a prize. The contestant picks a door, and then the host, who knows what's behind the doors, opens another door which has no prize. The contestant is then given the option to switch their choice to the other unopened door or stick with their original choice. The paradox is that switching doors actually increases the probability of winning from 1/3 to 2/3.

This API allows users to simulate this problem multiple times and see the results.

## API Endpoint

- `POST /game/play/`
  - Request body: `{"choose_option": str, "attempts": int}`
    - `choose_option`: Either "keep" (keep initial choice) or "change" (switch to the other door)
    - `attempts`: Number of times to run the simulation
  - Response: `{"wins": int, "losses": int}`

## Setup

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On Unix or MacOS: `source venv/bin/activate`
4. Install the requirements: `pip install -r requirements.txt`
5. Run migrations: `python manage.py migrate`
6. Start the server: `python manage.py runserver`

## Running Tests

To run the tests, use the following command:
`pytest`
