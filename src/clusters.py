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
    clusters = []
    return clusters
