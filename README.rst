Flickr Bulk Uploader
--------------------


This application is useful for those users that want to upload a lot
of Photos to Flickr, for example, when you pay for an account and you
need to do the first import.

That was the reason to me to create this application.


How it works
------------

You need to create a config file in called "settings.py" in the same
directory of the project with this inside::

    UPLOAD_FOLDER = '/path/to/your/photos/directory'

Once you have created this file and run the applicacion, it will
search all the subdirectories that doesn't have more subdirectories
and it will upload all the files inside them in a PhotoSet with the
name of this directory.

Example::

    /home/humitos/fotos/
    ├── Sunny day
    │   ├── IMG_0016.JPG
    │   ├── IMG_0017.JPG
    │   ├── IMG_0018.JPG
    
    ......
    
    ├── Kayak
    │   ├── DSC01732.jpg
    │   ├── DSC01733.jpg
    │   ├── DSC01734.jpg
    
    ......
    
    ├── My birthday
    │   ├── My camera
    │   │   ├── IMG_0239.JPG
    │   │   ├── IMG_0240.JPG
    │   └── My brother's camera
    │       ├── IMG_0151.JPG
    
    ......
    
Whit this directory structure, "flickr-bulk-uploader.py" will create 4
PhotoSets with the names: "Sunny day", "Kayak", "My camera" and "My
brother's camera".

Yes, the two las PhotoSets' names could be consider as a BUG. If you
have another idea about how to solve it, please open a new Issue.


Don't duplicate photos, please!
-------------------------------

If something wrong happens in the middle of the upload proccess and it
stops; you can "resume" the last state running it again without
uploading the same photos again. "flickr-bulk-upload.py" will check if
the Photo was already uploaded in the PhotoSet before to upload it.


Running the application
-----------------------

Just run it as a Python script::

    $ python flickr-bulk-uploader.py
