from config import config

def main():
    from app import app
    app.run()  # Already configured in __init__.py


if __name__ == '__main__':
    main()

