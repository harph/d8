import random

from exceptions import InsufficientNumberOfDocumentsError


class Document(object):
    def __init__(self, text):
        self.text = text

    def __unicode__(self):
        return self.text


class DocumentCluster(object):
    def __init__(self, initial_doc):
        self.documents = {initial_doc}
        self.centroid_terms = {}

    def __unicode__(self):
        return self.name

    @property
    def name(self):
        return '_'.join(self.centroid_terms)

    def recalculate_centroid(self):
        pass


def generate_document_clusters(documents, num_clusters):
    if len(documents) < num_clusters:
        msg = ('Insufficient number of documents ({docs_len}) for '
               'the amount of clusters requested ({num_clusters})')
        raise InsufficientNumberOfDocumentsError(
            msg.format(docs_len=len(documents), num_clusters=num_clusters))

    clusters = [
        DocumentCluster(doc)
        for doc in random.sample(documents, num_clusters)
    ]

    return clusters
