def get_token():

    with open('api_token.txt', 'r') as token_file:
        my_token = token_file.readline().rstrip()
    return my_token

