#!/usr/bin/python
# -*- coding: utf-8 -*-

import web
import db_manager
import json

urls = (
    '/songs', 'list_active_songs',
    '/songs/(.*)', 'delete_song'
)

app = web.application(urls, globals())


class list_active_songs:
    def GET(self):
        web.header('Content-Type', 'application/json')
        params = web.input()
        if 'greater_than' in params:
            return db_manager.get_active_songs_greater_than(params.greater_than)

        return db_manager.get_active_songs()


class delete_song:
    def DELETE(self, song_id):
        web.header('Content-Type', 'application/json')
        try:
            if db_manager.delete_song(song_id):
                return json.dumps({"message": "Song {} deleted".format(song_id)})
        except Exception, e:
            print e
            raise web.internalerror(
                json.dumps({"message": "Something went wrong :( Please, contact the administrator"}))

        raise web.notfound(json.dumps({"message": "Song {} not found".format(song_id)}))


if __name__ == "__main__":
    app.run()
