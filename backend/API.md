## API documentation
---
### Requests based on drinks
1. Get all drinks - no details

`GET '/drinks'`

- Get list of all drinks with minimal information
- Request Arguments: None
- Role based access: None - It's a public endpoint
- Returns: status code 200 and a json `{"success": True, "drinks": drinks}` where drinks is the list of drinks with the `short data representation` -  `drink.short()` or an appropriate status code indicating the reason for failure

```json
{
  "success": "True",
  "drinks": [drink.short() for all_drinks],
}
```

2. Get all drinks - with details

`GET '/drinks-detail'`

- Get list of all drinks with all information
- Request Arguments: None
- Role based access: `get:drinks-detail`
- Returns: status code 200 and a json `{"success": True, "drinks": drinks}` where drinks is the list of drinks with the `long data representation` -  `drink.long()` or an appropriate status code indicating the reason for failure

```json
{
  "success": "True",
  "drinks": [drink.long() for all_drinks],
}
```


3. Create a new drink

`POST '/drinks'`

- Create a new drink
- Request Arguments: JSON request body as following
```json
{
  "id": "The drink reference id in the database",
  "title": "the new drink name",
  "recipe": [{
          name: string,
          color: string,
          parts: number
        },
          ] 
}
```
- Role based access: `post:drinks`
- Returns: status code 200 and a json `{"success": True, "drinks": drinks}` where drinks is the list of drinks with the `long data representation` -  `drink.long()` or an appropriate status code indicating the reason for failure

```json
{
  "success": "True",
  "created": new_drink.id,
  "drinks": [drink.long() for all_drinks],
}
```
4. Update drinks information

`PATCH '/drinks/${id}'`

- Update the drink information for a drink specified by `id` request argument
- Request Arguments: 
  - Parameters: `id` with type `integer`
  - Request Body: JSON request as follows
```json
{
  "title": "the new drink name",
  "recipe": [{
          name: string,
          color: string,
          parts: number
        },
          ] 
}
```
- Role based access: `patch:drinks`
- Returns: status code 200 and a json `{"success": True, "drinks": drinks}` where drinks is the list of drinks with the `long data representation` -  `drink.long()` or an appropriate status code indicating the reason for failure

```json
{
  "success": "True",
  "created": new_drink.id,
  "drinks": [drink.long() for all_drinks],
}
```

5. Delete a drink

`DELETE '/drinks/${id}'`

- delete a drink specified by `id` request argument
- Request Arguments: 
  - Parameters: `id` with type `integer`
  - Request Body: None
- Role based access: `delete:drinks`
- Returns: status code 200 and a json `{"success": True, "deleted": id}` or an appropriate status code indicating the reason for failure

```json
{
  "success": "True",
  "deleted": "id of the drink to be deleted",
}
```
---