"""
# Intercom Articles API

Implements the Intercom Articles API [1]. Can be used to create, list, update, and delete individual Articles.
For operations regarding collections and the Help Center itself, see the Help Center API.

---
- [1] https://developers.intercom.com/intercom-api-reference/reference/articles


## Example Usage

```python
from intercom_python_sdk import Intercom

intercom = Intercom('my_api_key')

articles_list = intercom.articles.list_all() # Returns an ArticlesList object

for article in articles_list: # We can iterate over the ArticlesList object like a list
    print(article.name) # We can access the attributes of each Article object, as is defined in `apis/articles/models.py` and the Intercom Article Model [2].
    print(article.body) # The article body is a raw HTML string.
    print(article.content) # The content property returns the article body as a parsed BeautifulSoup object.

# We can get a specific Article by ID from an ArticleList object
article = articles_list.get_by_id(1234567890) # Returns an Article object

# Or we could pull the Article directly from the API
article = intercom.articles.get_by_id(1234567890) # Returns an Article object

# We can also update an Article
article.name = "My New Article Name"
article.update() # Updates the Article on the Intercom API

# And we can delete an Article
article.delete() # Deletes the Article from the Intercom API

# Or, by ID
intercom.articles.delete_by_id(1234567890)
```

## Creating a New Article
Like in other APIs, to create a new Article, We can use a Schema to dump a dictionary of data into an Article object, and then create it on the API.

article_data = {
    'title': 'Example Article',
    'body': '<p>Example Article Body</p>',
    'description': 'Example Article Description',
    'author_id': intercom.admins.me().id,
    'state':'draft' # Can be 'draft' or 'published'
}
article_schema = ArticleSchema().dump(article_data)
new_article = intercom.articles.create(article_schema) # Returns the new Article object.

"""

from . import api
from . import models
from . import schemas

