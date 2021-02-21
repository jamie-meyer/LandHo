from app import create_app


if __name__ == '__main__':
    port = 5000
    app = create_app()  # Or pass 'live' to NOT be in debug mode
    app.run(host='0.0.0.0', port=port, debug=True)
else:
    application = create_app()
