import unittest

from d8.clusters import Document, generate_document_clusters
from d8.exceptions import InsufficientNumberOfDocumentsError


class TestGenerateCluster(unittest.TestCase):
    def setUp(self):
        # TODO create pseudo-documents
        self.documents = [
            Document('Lorem ipsum dolor sit amet.'),
            Document('Consectetur adipiscing elit.'),
            Document('Duis scelerisque iaculis libero.'),
            Document('Duis eleifend pretium tristique.'),
            Document('Ut porttitor sem justo, id pharetra ipsum maximus eu.'),
        ]

    def test_clusters_len(self):
        """
        Tests that the number of clusters returned matches the requested
        number.
        """
        documents = self.documents
        # Number of clusters to be generated
        # Case 1: same number of clusters as documents (one doc per cluster)
        # Case 2: number of clusters is half the number of documents
        # Case 3: multiple documents, zero clusters
        # Case 4: no documents, zero clusters
        test_cases = (
            (documents, len(documents)),  # Case 1
            (documents, len(documents) / 2),  # Case 2
            (documents, 0),  # Case 3
            ([], 0),  # Case 4
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

    def test_insuficient_number_of_documents(self):
        """
        Tests that generate_document_clusters raises an exception if the
        number of clusters requested is greater than the number of given
        documents.
        """
        with self.assertRaises(InsufficientNumberOfDocumentsError):
            generate_document_clusters(self.documents, len(self.documents) + 1)


if __name__ == '__main__':
    unittest.main()
