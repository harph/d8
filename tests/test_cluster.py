import unittest

from d8.clusters import Document, generate_document_clusters
from d8.exceptions import (InvalidNumberOfClustersError,
                           InsufficientNumberOfDocumentsError)


class TestGenerateCluster(unittest.TestCase):
    def setUp(self):
        self.documents = [
            Document('Lorem ipsum dolor sit amet.'),
            Document('Consectetur adipiscing elit.'),
            Document('Duis scelerisque iaculis libero.'),
            Document('Duis eleifend pretium tristique.'),
            Document('Ut porttitor sem justo, id pharetra ipsum maximus eu.'),
        ]

    def test_clusters_length(self):
        """
        Tests that the total number of documents in the clusters is equals to
        the to the number of documents given.
        """
        documents = self.documents
        test_cases = (
            # N documents and 1 cluster
            (documents, 1),
            # Same number of documents and clusters.
            (documents, len(documents)),
            # Number of clusters is half the number of documents
            (documents, len(documents) / 2),
        )
        for docs, n_clusters in test_cases:
            doc_clusters = generate_document_clusters(docs, n_clusters)
            total_docs = sum([len(c) for c in doc_clusters])
            error_msg = ('Number of documents returned in the clusters '
                         '({returned}) does not add to the number of given '
                         ' documents given ({given}).').format(
                            given=len(docs),
                            returned=total_docs
                         )
            self.assertEquals(len(docs), total_docs, error_msg)

    def test_insuficient_number_of_documents(self):
        """
        Tests that generate_document_clusters raises an exception if the
        number of clusters requested is greater than the number of given
        documents.
        """
        test_cases = (
            # N document and N + 1 clusters
            (self.documents, len(self.documents) + 1),
            # No documents and 1 cluster.
            ([], 1),
        )
        for docs, n in test_cases:
            with self.assertRaises(InsufficientNumberOfDocumentsError):
                generate_document_clusters(docs, n)

    def test_number_of_clusters(self):
        """
        Tests that the number of clusters returned matches the requested
        number.
        """
        documents = self.documents
        test_cases = (
            # Same number of clusters as documents (one doc per cluster)
            (documents, len(documents)),
            # Number of clusters is half the number of documents
            (documents, len(documents) / 2),
            # Multiple documents, one clusters
            (documents, 1),
        )

        for docs, n_clusters in test_cases:
            doc_clusters = generate_document_clusters(docs, n_clusters)
            error_msg = ('Number of clusters returned ({returned}) does not '
                         'match the number of clusters '
                         'requested ({requested}).').format(
                            returned=len(doc_clusters),
                            requested=n_clusters
                         )
            self.assertEquals(len(doc_clusters), n_clusters, error_msg)

    def test_number_of_clusters_expection(self):
        """
        Tests that requesting zero or less clusters and
        InvalidNumberOfClustersError exception is rased.
        """
        test_cases = (
            # N documents with zero clusters
            (self.documents, 0),
            # N documents with -1 clusters
            (self.documents, -1)
        )
        for docs, n in test_cases:
            with self.assertRaises(InvalidNumberOfClustersError):
                generate_document_clusters(docs, n)


if __name__ == '__main__':
    unittest.main()
