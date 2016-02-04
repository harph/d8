import unittest

from d8.clusters import generate_document_clusters
from d8.exceptions import InsufficientNumberOfDocumentsError


class TestGenerateCluster(unittest.TestCase):
    def setUp(self):
        # TODO create pseudo-documents
        self.documents = []

    def test_clusters_len(self):
        """
        Tests that the number of clusters returned matches the requested
        number.
        """
        # Number of clusters to be generated
        num_clusters = 5
        doc_clusters = generate_document_clusters(self.documents, num_clusters)
        self.assertEquals(len(doc_clusters), num_clusters,
                         'Number of clusters returned does not match the '
                         'number of clusters requested.')

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
