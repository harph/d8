import random
import sys

from exceptions import (InsufficientNumberOfDocumentsError,
                        InvalidNumberOfClustersError)


class Document(object):
    """
    Represents a text document.
    """

    def __init__(self, text):
        self.text = text

    def __unicode__(self):
        return self.text

    def _recalculate_terms(self):
        # TODO: calculate terms using a steamer and removing stop words
        self._terms = set(self.text.split())

    @property
    def terms(self):
        return self._terms

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value
        self._recalculate_terms()


class DocumentCluster(object):
    """
    Represents a cluster of documents.
    """

    def __init__(self, initial_doc):
        self.documents = {initial_doc}
        self.centroid = None
        self.recalculate_centroid()

    def __len__(self):
        return len(self.documents)

    def __unicode__(self):
        return "%s, %d" %(self.name, len(self.documents))

    @property
    def name(self):
        return '_'.join(self.centroid_terms)

    def recalculate_centroid(self):
        self.centroid = reduce(lambda acum, doc: acum.union(doc.terms),
                               self.documents, set())

    def get_distance_to_centroid(self, document):
        """
        Calculates the distance between the document and the centroid. This is
        based on tghe different between the centroid and document terms.
        
        Args:
            document (Document): Document instance for which the distance is
            going to be calculated.

        Returns:
            int: Positive value representing distance of the document to the
            centroid.
        """
        diff = self.centroid - document.terms
        return len(diff)

def generate_document_clusters(documents, num_clusters):
    """
    Given a list of documents and a number of clusters, it generates a list of
    documents.

    Args:
        documents (list): An iterable list of Document instances.
        num_clusters (int): Number of cluster to be generated.

    Returns:
        list: List of length 'num_clusters' containin DocumentCluster
        instances.
    """
    if num_clusters <= 0:
        raise InvalidNumberOfClustersError(
            'Number of clusters must be greater than 0')

    if len(documents) < num_clusters:
        msg = ('Insufficient number of documents ({docs_len}) for '
               'the amount of clusters requested ({num_clusters})')
        raise InsufficientNumberOfDocumentsError(
            msg.format(docs_len=len(documents), num_clusters=num_clusters))

    # Pick randomily one document per cluster.
    document_clusters = [
        DocumentCluster(doc)
        for doc in random.sample(documents, num_clusters)
    ]

    for doc in documents:
        best_cluster = None
        min_distance = sys.maxint
        for cluster in document_clusters:
            #if doc not int cluster:
            distance = cluster.get_distance_to_centroid(doc)
            if distance < min_distance:
                best_cluster = cluster
                min_distance = distance
        best_cluster.documents.add(doc)

    return document_clusters
