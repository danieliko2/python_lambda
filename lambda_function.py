import wikipediaapi
import json

def lambda_handler(event, context):

    wiki_wiki = wikipediaapi.Wikipedia('en')
    
    print("test")
    page_input = event['key1']
    
    page_py = wiki_wiki.page(page_input)
    
    if page_py.exists():
        print("Page - Title: %s" % page_py.title)
        print("Page - Summary: %s" % page_py.summary)
        
        return {
            'statusCode': 200,
            'body': json.dumps(page_py.summary),
            'title': json.dumps(page_py.title)
        }
    else:
        return {'statusCode': 400}
