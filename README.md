# Django web app
This project shows how Django and graphene can be used to construct a simple GraphQL API.

## Setup
From the project directory, run the following bash script. This will install the neccessary Python packages:

```bash
pip3 install -r requirements.txt
 ```

Run these commands to migrate the database and apply the model objects:

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

## Running the app
To run the app, use this command:
```bash
python3 manage.py runserver
```

## Adding mock data
With the app running, navigate to `http://127.0.0.1:8000/graphql`

From here, you can add mock data modifying the query found in the mock_data file and running it in GraphiQL. For example:

```
mutation addJohnSmith {
  createPerson(
    email: "johnsmith@gmail.com"
    name: "John Smith"
    addressNumber: 101
    addressStreet: "Bourke St"
    addressCity: "Melbourne"
    addressState: "VIC"
  ) {
    person {
      email
      name
      address {
        number
        street
        city
        state
      }
    }
  }
}

```

## Querying the database

To query the database and see the people you have added, execute the following query:

```
query {
  people {
    email
    name
    address {
      number
      street
      city
      state
    }
  }
}
```
