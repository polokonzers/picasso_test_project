# Picasso test project

  

## Description

  

A Django Rest API, that shows an ability to upload files, and asynchronous change their field "processed" through Celery+Redis.

Model "File" includes those fields:

1.  `file (FileField)`

2.  `uploaded_at (DateTimeField)`

3.  `processed (BooleanField)`

  

All actions with `File` instances passes through `FileSerializer`.

Docker-compose with 4 containers used:

1. Redis

2. PostgreSQL

3. Django Rest API

4. Celery worker

  ### Additional info:

- The API able to work with different file types and logs errors, if they appear.
- **Test coverage - 75%**
- Maximum RPS depends on the throughput of the VM on which the containers will be launched

  
## Requests
**POST**-requests use endpoint `http://localhost:8000/upload/`, body: `form-data`, key: `file`, value: `<your_file>`.

At the process of uploading `File` on the server, client receives a response status with serialized data of `Field` and Celery starts an asynchronous task to change `File` field `processed` to `True`.

Example of response:

`{`

`"id": 2,`

`"file": "/media/Example_file.pdf",`

`"uploaded_at": "2023-10-20T11:04:20.712604Z",`

`"processed": false`

`}`

  

**GET**-requests use endpoint `http://localhost:8000/upload/`.

Example of response:

`[`

`{`

`"id": 1,`

`"file": "/media/Example_png_file.png",`

`"uploaded_at": "2023-10-20T11:03:00.221734Z",`

`"processed": true`

` },`

` {`

`"id": 2,`

`"file": "/media/Example_file.pdf",`

`"uploaded_at": "2023-10-20T11:04:20.712604Z",`

`"processed": true`

` }`

`]`


## Instructions:

1. Open a directory with `docker-compose.yml`
2. Run `docker-compose up -d`
3. Run `docker container ls`
4. Find and copy name or id of a container, with name `web...`
5. Run `docker exec -it <container_name> bash`
6. In opened container terminal run `cd picasso_test_project` 
7. Run `python manage.py makemigrations`
8. Run `python manage.py migrate`