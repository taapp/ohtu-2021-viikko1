import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_lisays_negatiivisen_lisays(self):
        self.assertAlmostEqual(self.varasto.lisaa_varastoon(-8), None)

    def test_ottaminen_negatiivisen_ottaminen(self):
        self.assertAlmostEqual(self.varasto.ota_varastosta(-8), 0.0)
    

    def test_ottaminen_otetaan_enemman_kuin_saldo(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.ota_varastosta(10), 8)

    def test_alkusaldo_negatiivinen(self):
        varasto_temp = Varasto(10,-10)
        self.assertAlmostEqual(varasto_temp.saldo, 0.0)

    def test_tilavuus_negatiivinen(self):
        varasto_temp = Varasto(-1)
        self.assertAlmostEqual(varasto_temp.tilavuus, 0.0)

    def test_lisays_enemman_kuin_tilaa(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_str(self):
        self.varasto.lisaa_varastoon(8)
        # varastossa pitäisi olla tilaa 10 - 8 eli 2
        self.assertAlmostEqual(str(self.varasto), f"saldo = 8, vielä tilaa 2")

