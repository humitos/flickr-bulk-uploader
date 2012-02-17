import os
import flickrapi

api_secret = 'a131ba6ac653b986'
api_key = 'dced4d69f72c55375dd72f12d2a3941b'

PHOTOS_DIRECTORY = '/home/humitos/fotos'

flickr = flickrapi.FlickrAPI(api_key, api_secret, format='etree')

(token, frob) = flickr.get_token_part_one(perms='write')
flickr.get_token_part_two((token, frob))

for root, dirs, files in os.walk(PHOTOS_DIRECTORY):
    if dirs != []:
        continue
    else:
        print 'Subiendo fotos de:'
        print '    %s' % root
        photoset_created = False
        photoset_title = os.path.basename(root)
        photoset_id = False

        for filename in files:
            duplicated_photo = False
            path = os.path.join(root, filename)
            print '      - %s' % path

            # check if the photo is already in Flickr server
            photosets_list = flickr.photosets_getList()
            for ps in photosets_list.find('photosets').findall('photoset'):
                if ps.find('title').text == photoset_title:
                    photoset_id = ps.get('id')
                    photoset_photos = flickr.photosets_getPhotos(
                        photoset_id=photoset_id)
                    for photo in photoset_photos.find('photoset')\
                                                .findall('photo'):
                        if photo.get('title') == filename[:-4]:
                            # skip this file because it's already in Flickr
                            print 'Este archivo ya esta en el servidor: %s' % filename
                            duplicated_photo = True
                            break

            if duplicated_photo:
                continue
            upload_etree = flickr.upload(filename=path,
                                         is_public=0)

            if upload_etree.get('stat') == 'ok':
                photo_id = upload_etree.find('photoid').text
                if photoset_id and photoset_created:
                    flickr.photosets_addPhoto(photoset_id=photoset_id,
                                              photo_id=photo_id)

                if not photoset_created:
                    photoset_etree = flickr.photosets_create( \
                                        title=photoset_title,
                                        primary_photo_id=photo_id)
                    if photoset_etree.get('stat') == 'ok':
                        photoset_created = True
                        photoset_id = photoset_etree.find('photoset').get('id')
                    else:
                        print 'Problema creando el Photoset'

            else:
                print 'Problema subiendo la foto'
