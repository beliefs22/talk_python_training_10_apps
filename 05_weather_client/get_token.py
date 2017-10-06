def get_token():
    """
    Gets weather underground api token from api_token.txt file
    :return: api token
    """

    with open('api_token.txt', 'r') as token_file:
        my_token = token_file.readline().rstrip()
    return my_token

