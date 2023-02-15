from .run import hello_word

def test_hello_word():
    """Teste de Rota"""
    
    result = hello_word()
    assert result == 'Ola, estou na aplicação setada'