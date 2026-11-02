import unittest
from laskin import Laskin


class StubIO:
    def __init__(self, inputs):
        self.inputs = inputs
        self.outputs = []

    def lue(self, teksti):
        return self.inputs.pop(0)

    def kirjoita(self, teksti):
        self.outputs.append(teksti)


class TestLaskin(unittest.TestCase):
    def test_yksi_summa_oikein(self):
        io = StubIO(["1", "3", "-9999"])
        laskin = Laskin(io)
        laskin.suorita()

        self.assertEqual(io.outputs, ["Summa: 4"])

    def test_useita_summia_oikein(self):
        io = StubIO(["1", "2", "10", "20", "-9999"])
        laskin = Laskin(io)
        laskin.suorita()

        self.assertEqual(io.outputs, ["Summa: 3", "Summa: 30"])

    def test_negatiivisten_lukujen_summa_oikein(self):
        io = StubIO(["-5", "2", "-9999"])
        laskin = Laskin(io)
        laskin.suorita()

        self.assertEqual(io.outputs, ["Summa: -3"])

    def test_nollien_summa_oikein(self):
        io = StubIO(["0", "0", "-9999"])
        laskin = Laskin(io)
        laskin.suorita()

        self.assertEqual(io.outputs, ["Summa: 0"])

    def test_lopetus_ensimmaisena_lukuna_ei_tulosta_summaa(self):
        io = StubIO(["-9999"])
        laskin = Laskin(io)
        laskin.suorita()

        self.assertEqual(io.outputs, [])

    def test_lopetus_toisena_lukuna_ei_tulosta_summaa(self):
        io = StubIO(["5", "-9999"])
        laskin = Laskin(io)
        laskin.suorita()

        self.assertEqual(io.outputs, [])
