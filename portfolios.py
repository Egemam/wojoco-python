def portfolio_submit(user, text):
    path = f'portfolio/{user}.txt'
    with open(path, 'w') as fp:
        fp.write(text)
def portfolio_read(user):
    path = f'portfolio/{user}.txt'
    with open(path, 'r') as fp:
        fp.read()