import unittest
import makesite


class SlugifyTest(unittest.TestCase):

    def test_slugify(self):
        self.assertEqual(makesite.slugify('NginX est brillant'), 'nginx-est-brillant')
        self.assertEqual(makesite.slugify('Bilan hébergement 2023'), 'bilan-hebergement-2023')
        self.assertEqual(makesite.slugify('Sécurisation Docker : des pistes'), 'securisation-docker-des-pistes')
        self.assertEqual(makesite.slugify('Il court, il court, le furet'), 'il-court-il-court-le-furet')
        self.assertEqual(makesite.slugify('De GNU/Linux à gnuSystemlinuxdGnomeOs'), 'de-gnulinux-a-gnusystemlinuxdgnomeos')
        self.assertEqual(makesite.slugify('Au fait... mon téléphone'), 'au-fait-mon-telephone')