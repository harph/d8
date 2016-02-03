from exceptions import InsufficientNumberOfDocumentError


class DocumentCluster(object):
    def __init__(self, centroid_terms):
        self.centroid_terms = centroid_terms
        self.documents = []

    @property
    def name(self):
        return '_'.join(self.centroid_terms)

    def recalculate_centroid(self):
        pass


def generate_document_clusters(documents, num_clusters):
    if len(documents) < num_clusters:
        msg = ('Insufficient number of documents ({docs_len}) for '
               'the amount of clusters requested ({num_clusters})')
        raise InsufficientNumberOfDocumentError(
            msg.format(docs_len=len(documents), num_clusters=num_clusters))

    clusters = []
    return clusters
