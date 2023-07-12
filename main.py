import spacy
import pytextrank
from rdflib import Graph
from SPARQLWrapper import SPARQLWrapper, JSON
from rdflib.namespace import FOAF

nlp = spacy.load("en_core_web_lg")
nlp.add_pipe("textrank")

def extract(sentence):
    result=[]
    doc = nlp(sentence)
    for phrase in doc._.phrases[:3]:
        result.append(phrase.text)
    
    return result

def query(keywords):

    for item in keywords:
        if 'book' in item:
            i= keywords.index(item)
            keywords[i]=item.replace('book','')
            
        
    user_input1 = keywords[0].strip()
    user_input2 = keywords[1].strip()
    g = Graph()
    g.parse("kde_googlebooks.ttl", format='turtle')
    query = """
    PREFIX rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
    PREFIX dbo:<http://dbpedia.org/ontology/>
    PREFIX ex: <http://example.org/>
    SELECT ?title ?author ?genre ?year ?rating ?lan 
    WHERE {{
    ?book ex:author ?author;
            ex:title ?title;
            ex:genre ?genre;
            ex:publishedYear ?year;
            ex:rating ?rating;
            ex:language ?lan.
    FILTER ( 
        (regex(str(?author), "{0}", "i") || regex(str(?title), "{0}", "i") || regex(str(?genre), "{0}", "i") || regex(str(?rating), "{0}", "i") || regex(str(?year), "{0}", "i")|| regex(str(?lan), "{0}", "i"))
        &&
        (regex(str(?author), "{1}", "i") || regex(str(?title), "{1}", "i") || regex(str(?genre), "{1}", "i") || regex(str(?rating),"{1}", "i") || regex(str(?year), "{1}", "i")|| regex(str(?lan), "{1}", "i")))
    }}
    ORDER BY DESC(?rating)
    """.format(user_input1, user_input2)
    result = g.query(query)
    result_dic={}
    result_list=[]
    for row in result:
        result_dic["Title"]=row[0][:100]
        result_dic["Author"]=row[1][:50]
        result_dic["Genre"]=row[2][:50]
        result_dic["Year"]=row[3][:4]
        result_dic["Rate"]=row[4][:4]
        result_list.append(result_dic)
        print("Title: ", row[0])
        print("Author: ", row[1])
        print("Genre: ", row[2])
        print("Year:", row[3][:4])
        print("\n")
    return result_list
       
    
 

# text=input()
# res=extract(text)
# x=query(res)
# print(x)



