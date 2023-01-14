<!-- Rayka Backend API -->
1- Add your "local_settings.py" file to /src/rayka/ containing AWS credentials.

2- Run the command below  in the Terminal based on your OS to build the docker container.

Linux and macOS:
    "docker compose up --build"

Windows:
    "docker-compose up --build"

The command will run the 4 unittests and after that run django server at "localhost:8083".
Now the Server is ready to accept requests.


->>> You can find API documentation on DocX file. <<<-