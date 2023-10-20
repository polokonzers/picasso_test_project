# Picasso test project

  

A Django Rest API, that shows an ability to upload files, and asynchronous change their field "processed" through Celery+Redis.
Model "File" includes those fields:
1. `file (FileField)`
2. `uploaded_at (DateTimeField)`
3. `processed (BooleanField)`

All actions with `File` instances passes through `FileSerializer`.

**POST**-requests use endpoint `upload/`, body: `form-data`, key: `file`, value: `<your_file>`.
At the process of uploading `File` on the server, client receives a response status with serialized data of `Field` and Celery starts an asynchronous task to change `File` field `processed` to `True`. 
Example of response:
`{`
    `"id": 2,`
    `"file": "/media/Example_file.pdf",`
    `"uploaded_at": "2023-10-20T11:04:20.712604Z",`
    `"processed": false`
`}`

**GET**-requests use endpoint `files/`.
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


Docker-compose with 4 containers used:
1. Redis
2. PostgreSQL
3. Django Rest API
4. Celery worker

The API able to work with different file types and logs errors, if they appear.

**Test coverage - 75%**
Maximum RPS depends on the throughput of the VM on which the containers will be launched