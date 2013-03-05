# -*- coding: utf-8 -*-
"""
Created on Mon Mar 04 15:15:56 2013

@author: aitor
"""
import urllib2
import json
import csv

def get_articles():      
    MORELAB_URL_SEARCH = "http://www.morelab.deusto.es/joseki/articles?query="
    QUERY_GET_ARTICLES= ( u"""PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> """ 
                          u"""PREFIX foaf: <http://xmlns.com/foaf/0.1/> """ 
                          u"""SELECT DISTINCT ?page WHERE { ?s rdf:type foaf:Document . ?s foaf:homepage ?page }""" )
    END_JSON = "&output=json"
    
    url = MORELAB_URL_SEARCH + urllib2.quote(QUERY_GET_ARTICLES.encode('utf-8')) + END_JSON
    
    response = urllib2.urlopen(url)
    content = response.read()
    bindings = json.loads(content)["results"]["bindings"]
    pages = []
    for binding in bindings:
        pages.append(binding["page"]["value"])
    return pages

def get_authors(page):
    MORELAB_URL_SEARCH = "http://www.morelab.deusto.es/joseki/articles?query="
    QUERY_GET_AUTHORS_START =  (    u"""PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> """
                                    u"""PREFIX dc: <http://purl.org/dc/elements/1.1/>"""
                                    u"""PREFIX foaf: <http://xmlns.com/foaf/0.1/> """ 
                                    u"""SELECT DISTINCT ?author WHERE { ?s foaf:homepage <""")
    QUERY_GET_AUTHORS_END =   u"""> . ?s dc:creator ?author }"""
    END_JSON = "&output=json"
    
    query = QUERY_GET_AUTHORS_START + page + QUERY_GET_AUTHORS_END
    url = MORELAB_URL_SEARCH + urllib2.quote(query) + END_JSON
    response = urllib2.urlopen(url)
    content = response.read()
    bindings = json.loads(content)["results"]["bindings"]
    authors = []
    for binding in bindings:
        name = binding["author"]["value"]
        if 'http://' in name:
            name = get_name_from_uri(name) 
        name = normalize_name(name)
        if not is_malformed(name):
            authors.append(name.encode('utf-8'))
    return authors
    
# There are several malformed names in MORElab's publication repository
def is_malformed(name):
    malformedNames = ['fern', 'others', 'deusto',  'd.t.t.f.', 'spain', 'd.b.']
    return name in malformedNames

def get_name_from_uri(uri):
     name = uri.split('/')[-1]
     name = name.replace(', ', '-')
     name = name.replace(',', '')
     name = name.replace(' ', '-')
     name = name.replace('_', '-')
     return name
   
 # Names in MORElab's Joseki server are a complete chaos, this is an attempt
 # to normalize the names
def normalize_name(name):
    name = name.lower()
      
    if u"ipiña" in name:
        name = "dipina"
    elif u"de-ipina" in name:
        name = "dipina"
    elif u"lópez, d." in name:
        name = "dipina"
    elif u"de ipina, d." in name:
        name = "dipina"
    elif u"lopez-ipina" in name:
        name = "dipina"
    elif u"deipina, d" in name:
        name = "dipina"
    elif u"ipina" in name:
        name = "dipina"
    elif u"vázquez, j." in name:
        name = "juan-ignacio-vazquez"
    elif u"vazquez, j" in name:
        name = "juan-ignacio-vazquez"
    elif u"juan-ignacio-vázquez" in name:
        name = "juan-ignacio-vazquez"
    elif u"vazquez, i" in name:
        name = "juan-ignacio-vazquez"
    elif u"vázquez, i" in name:
        name = "juan-ignacio-vazquez"
    elif u"sacristán, m" in name:
        name = "marcos-sacristan"
    elif u"marcos-sacristán" in name:
        name = "marcos-sacristan"
    elif u"abaitua, j" in name:
        name = "joseba-abaitua"
    elif u"abaitua odriozol" in name:
        name = "joseba-abaitua"
    elif u"díaz labrador" in name:
        name = "josuka"
    elif u"díaz, j.k." in name:
        name = "josuka"
    elif u"labrador" in name:
        name = "josuka"
    elif u"josuka-diaz" in name:
        name = "josuka"
    elif u"alineida" in name:
        name = "aitor-almeida"
    elif u"escondrillas, a." in name:
        name = "aitor-almeida"   
    elif u"sainz, d" in name:
        name = "david-sainz"
    elif u"sáinz, d" in name:
        name = "david-sainz"
    elif u"gonzalez, d" in name:
        name = "david-sainz"
    elif u"de garibay" in name:
        name = "jonathan-garibay"
    elif u"sotomayor, b" in name:
        name = "borja-sotomayor"
    elif u"muguira, l" in name:
        name = "leire-muguira"
    elif u"de las heras" in name:
        name = "rafael-heras"
    elif u"pretel, i" in name:
        name = "ivan-pretel"
    elif u"blanco, s" in name:
        name = "sergio-blanco"
    elif u"díaz-de-sarralde" in name:
        name = "ignacio-sarralde"
    elif u"diaz-de-sarralde" in name:
        name = "ignacio-sarralde"
    elif u"buján, d" in name:
        name = "david-bujan"
    elif u"bujan" in name:
        name = "david-bujan"
    elif u"emaldi, m" in name:
        name = "mikel-emaldi"
    elif u"garcía-zubia, j" in name:
        name = "zubia"
    elif u"garcia-zubia" in name:
        name = "zubia"
    elif u"javier-garcía-zubía" in name:
        name = "zubia"
    elif u"zubía" in name:
        name = "zubia"
    elif u"irurzun, j" in name:
        name = "jaime-irurzun"
    elif u"angulo, i" in name:
        name = "ignacio-angulo"
    elif u"arruti, a" in name:
        name = "asier-arruti"
    elif u"barbier, a" in name:
        name = "ander-barbier"
    elif u"guenaga, m.l" in name:
        name = "mariluz-guenaga"
    elif u"garcia, i" in name:
        name = "ivan-garcia"
    elif u"garcía, i" in name:
        name = "ivan-garcia"
    elif u"garcia, d" in name:
        name = "d-garcia"
    elif u"garcía, d" in name:
        name = "d-garcia"
    elif u"ez, j" in name:
        name = "j-fernandez"
    elif u"hernández, u" in name:
        name = "unai-hernandez"
    elif u"jayo" in name:
        name = "unai-hernandez"
    elif u"ez, u." in name:
        name = "unai-hernandez"
    elif u"hern" in name:
        name = "unai-hernandez"
    elif u"trueba, i" in name:
        name = "ivan-trueba"
    elif u"klein, b" in name:
        name = "bernhard-klein"
    elif u"guggenmos, c" in name:
        name = "christian-guggenmos"
    elif u"larizgoitia, i" in name:
        name = "iker-larizgoitia"
    elif u"lamsfus, c" in name:
        name = "carlos-lamfus"
    elif u"sedano, i" in name:
        name = "inigo-sedano"
    elif u"iñigo-sedano" in name:
        name = "inigo-sedano"   
    elif u"castro" in name:
        name = "manuel-castro" 
    elif u"dziabenko" in name:
        name = "olga-dziabenko" 
    elif u"martín, s" in name:
        name = "s-martin" 
    elif u"martín, d" in name:
        name = "d-martin" 
    elif u"díaz, g" in name:
        name = "g-diaz" 
    elif u"gil, g" in name:
        name = "g-gil" 
    elif u"gil, c" in name:
        name = "c-gil" 
    elif "," in name:
        name = name.split(',')[0]
 
    return name
                      
def get_relations():
    pages = get_articles()
    relations =[]
    for page in pages:
        authors = get_authors(page)
        relations.append(authors)
    return relations

# exports the relations in Gelphi's CSV format (as a undirected graph)    
def export_gephi_csv(relations):
    with open('./data/coauthors.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        for authors in relations:
            for author in authors:
                ind = authors.index(author)
                for i in range(ind+1, len(authors)):
                    row = [author, authors[i]]
                    writer.writerow(row)     

def export_igraph_edgelist(relations):
     with open('./data/coauthors.txt', 'w') as file:
        for authors in relations:
            for author in authors:
                ind = authors.index(author)
                for i in range(ind+1, len(authors)):
                    file.write(author + " " + authors[i] + "\n")    
            
            
rel = get_relations()
export_gephi_csv(rel)
export_igraph_edgelist(rel)
        

                            
    

