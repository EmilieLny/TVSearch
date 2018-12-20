import os
from bottle import (get, post, redirect, request, route, run, static_file, jinja2_view, template, error)
import utils
import json

# Static Routes

@get("/js/<filepath:re:.*\.js>")
def js(filepath):
    return static_file(filepath, root="./js")

@get("/css/<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root="./css")

@get("/images/<filepath:re:.*\.(jpg|png|gif|ico|svg)>")
def img(filepath):
    return static_file(filepath, root="./images")

@route('/')
def index():
    sectionTemplate = "./templates/home.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData={})

@error(404)
def error404(error):
    sectionTemplate = "./templates/404.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData={})

@route('/browse')
def browse():
    sectionTemplate = "./templates/browse.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData=[json.loads(utils.getJsonFromFile(x)) for x in utils.AVAILABE_SHOWS])


@route('/search', method="GET")
def browse():
    sectionTemplate = "./templates/search.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData={})


@route('/search', method="POST")
def browse():
    sectionTemplate = "./templates/search_result.tpl"
    user_search_query = request.forms.get('q')
    list_of_show_objects = [json.loads(utils.getJsonFromFile(x)) for x in utils.AVAILABE_SHOWS]
    search_results = []
    for i in range(len(list_of_show_objects)-1):
        for j in range(len(list_of_show_objects[i]['_embedded']['episodes'])-1):
            show = list_of_show_objects[i]
            if user_search_query in str(show['name']) or user_search_query in str(show['_embedded']['episodes'][j]['name']) or user_search_query in str(show['_embedded']['episodes'][j]['summary']):
                single_result = {
                    "showid": list_of_show_objects[i]['id'],
                    "episodeid": list_of_show_objects[i]['_embedded']['episodes'][j]['id'],
                    "text": (list_of_show_objects[i]['name']+": "+list_of_show_objects[i]['_embedded']['episodes'][j]['name'])
                }
                search_results.append(single_result)
    sectionData = search_results
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData=sectionData, query=user_search_query)


run(host='0.0.0.0', port=os.environ.get('PORT', 5000))
