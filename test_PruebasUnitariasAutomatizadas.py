import pytest
from ConvertirNumeroRomano import convertirNumeroRomano

def test_conversion_correcta():
    assert convertirNumeroRomano(10) == 'X'

def test_limites_inferiores():
    assert convertirNumeroRomano(1) == 'I'

def test_limites_superiores():
    assert convertirNumeroRomano(3999) == 'MMMCMXCIX'


def test_validacion_entrada_incorrecta():
    with pytest.raises(ValueError):
        convertirNumeroRomano('ABC')

def test_rango_entrada_invalido():
    with pytest.raises(ValueError):
        convertirNumeroRomano(4000)
