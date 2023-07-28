from tests import fake_factory

from intercom_python_sdk.schemas import (
    ArticleSchema, 
    ArticleStatisticsSchema,
    ArticleListSchema
)

from intercom_python_sdk.models import Article, ArticleList

import unittest


class TestArticleSchema(unittest.TestCase):
    def test_article_schema(self):
        article, _ = fake_factory.fake_schema(ArticleSchema)
        assert isinstance(article, ArticleSchema)

    def test_article_schema_validation(self):
        _, data = fake_factory.fake_schema(ArticleSchema)
        assert not ArticleSchema().validate(data)

    def test_article_schema_load(self):
        article, data = fake_factory.fake_schema(ArticleSchema)
        article = ArticleSchema().load(data)
        assert isinstance(article, Article)

    def test_article_schema_dump_and_load(self):
        article, data = fake_factory.fake_schema(ArticleSchema)
        article = ArticleSchema().load(data)
        article = ArticleSchema().dump(article)
        assert not ArticleSchema().validate(article), ArticleSchema().validate(article)

    # Tests that the statistics field is correctly loaded as an instance of ArticleStatisticsSchema
    def test_article_statistics_loaded(self):
        article, data = fake_factory.fake_schema(ArticleSchema)
        assert 'statistics' in data
        assert isinstance(data['statistics'], dict)
        assert not ArticleStatisticsSchema().validate(data['statistics'])

    # Tests that an error is raised if the 'id' field is missing
    def test_article_missing_id_field(self):
        _, data = fake_factory.fake_schema(ArticleSchema)
        del data['id']
        assert ArticleSchema().validate(data)

    # Tests that an error is raised if the 'title' field is missing
    def test_article_missing_title_field(self):
        article, data = fake_factory.fake_schema(ArticleSchema)
        del data['title']
        assert ArticleSchema().validate(data)


class TestArticleListSchema(unittest.TestCase):
    def test_article_list_schema(self):
        article_list, _ = fake_factory.fake_schema(ArticleListSchema)
        assert isinstance(article_list, ArticleListSchema)

    def test_article_list_schema_validation(self):
        _, data = fake_factory.fake_schema(ArticleListSchema)
        assert not ArticleListSchema().validate(data), ArticleListSchema().validate(data)

    def test_article_list_schema_load(self):
        article_list, data = fake_factory.fake_schema(ArticleListSchema)
        article_list = ArticleListSchema().load(data)
        assert isinstance(article_list, ArticleList)

    def test_article_list_schema_dump_and_load(self):
        article_list, data = fake_factory.fake_schema(ArticleListSchema)
        article_list = ArticleListSchema().load(data)
        article_list = ArticleListSchema().dump(article_list)
        assert not ArticleListSchema().validate(article_list), ArticleListSchema().validate(article_list)

    def test_article_list_iteration(self):
        _, data = fake_factory.fake_schema(ArticleListSchema)
        article_list = ArticleListSchema().load(data)
        for article in article_list:
            assert isinstance(article, Article)
    
    def test_article_list_index(self):
        _, data = fake_factory.fake_schema(ArticleListSchema)
        article_list = ArticleListSchema().load(data)
        assert isinstance(article_list[0], Article)

    def test_article_list_len(self):
        _, data = fake_factory.fake_schema(ArticleListSchema)
        article_list = ArticleListSchema().load(data)
        assert len(article_list) == len(data['data'])