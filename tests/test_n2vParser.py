import unittest
from unittest import TestCase
import os

from n2v import n2vParser

# files used by many tests
gene2ensembl = os.path.join(os.path.dirname(
    __file__), 'data', 'small_gene2ensem.txt.gz')
string_ppi = os.path.join(os.path.dirname(
    __file__), 'data', 'small_protein_actions_v11.txt.gz')

hpo_path = os.path.join(os.path.dirname(__file__),
                        'data', 'small_disease_disease.txt')
gtex_path = os.path.join(os.path.dirname(
    __file__), 'data', 'small_gtex.txt.gz')
gene_disease_train_path = os.path.join(
    os.path.dirname(__file__), 'data', 'small_gene_disease.txt')
gene_disease_test_path = os.path.join(
    os.path.dirname(__file__), 'data', 'small_g2d_test.txt')

params = {'gtex_path': gtex_path, 'gene2ensembl_path': gene2ensembl, 'string_path': string_ppi,
          'g2d_train_path': gene_disease_train_path, 'g2d_test_path': gene_disease_test_path, 'd2d_path': hpo_path}


class TestN2vParser(TestCase):
    def test_n2vParser_init(self):
        n2vParser(data_dir="tests/data", params=params)

    def test_get_num_proteins_not_mapped_count(self):
        p = n2vParser(data_dir="tests/data", params=params)
        # TODO: currently testing only execution, in
        # the future it will be necessary to also test
        # if the return value is correct
        p.get_num_proteins_not_mapped_count()

    def test_get_number_proteins_found_TCRD(self):
        p = n2vParser(data_dir="tests/data", params=params)
        # TODO: currently testing only execution, in
        # the future it will be necessary to also test
        # if the return value is correct
        p.get_number_proteins_found_TCRD()

    def test_parse(self):
        p = n2vParser(data_dir="tests/data", params=params)
        # TODO: currently testing only execution, in
        # the future it will be necessary to also test
        # if the return value is correct
        p.parse()

    def test_summary(self):
        p = n2vParser(data_dir="tests/data", params=params)
        # TODO: currently testing only execution,
        # but the following method currently
        # consists only of a "pass"
        p.print_summary()

    def test_n2vParser_wrong_path(self):
        with self.assertRaises(Exception):
            n2vParser(data_dir="tests/dataty", params=params)
        with self.assertRaises(Exception):
            n2vParser(data_dir="tests/test_n2vParser.py", params=params)
        with self.assertRaises(Exception):
            n2vParser(data_dir="tests/data")
