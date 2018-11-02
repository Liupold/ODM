﻿import unittest
from harvester.Core import HarvesterEngine
from harvester import HarvesterHelper
from requests.structures import CaseInsensitiveDict
from time import sleep
import shutil


class TestHarvesterEngine(unittest.TestCase):

    def setUp(self):
        self.test_download_instance = HarvesterEngine(
            "https://speed.hetzner.de/100MB.bin", location="Harvester_tmp/",
            part_location="Harvester_tmp/")

    def test_init_vars(self):
        self.assertEqual(self.test_download_instance.url,
                         'https://speed.hetzner.de/100MB.bin')
        self.assertEqual(self.test_download_instance.verify, True)
        self.assertIsInstance(
            self.test_download_instance._HarvesterCoreLOGer,
            HarvesterHelper.LOG)
        self.assertIs(
            type(self.test_download_instance.recived_headers),
            CaseInsensitiveDict)
        self.assertEqual(self.test_download_instance.downloadable, True)
        self.assertEqual(self.test_download_instance.pauseable, True)

    def test_Download_and_Pause(self):
        self.assertEqual(self.test_download_instance.block, True)
        self.test_download_instance.Download(False)
        sleep(2)
        self.assertGreater(self.test_download_instance.done, 0)
        self.assertEqual(self.test_download_instance.block, False)
        self.assertEqual(self.test_download_instance.downloading, True)
        self.test_download_instance.Download(False)
        self.test_download_instance.Pause()
        self.assertEqual(self.test_download_instance.downloading, False)
        self.assertEqual(self.test_download_instance.stoped, True)
        self.assertLess(self.test_download_instance.Get_done(), 1)

    def tearDown(self):
        shutil.rmtree('Harvester_tmp/', ignore_errors=True)


if __name__ == '__main__':
    unittest.main()