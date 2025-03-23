import network
import usocket as socket
import machine
import gc
gc.collect()

led_r = machine.Pin(2, machine.Pin.OUT)
led_g = machine.Pin(5, machine.Pin.OUT)
led_b = machine.Pin(10, machine.Pin.OUT)



def obter_arquivo(arquivo):
    conteudo = ''
    a = open(arquivo, 'rb')
    conteudo = a.read()
    a.close()
    return conteudo

estacao = network.WLAN(network.STA_IF)
estacao.active(True)
estacao.connect('Quaresma', 'HD2BIOS@#')
while estacao.isconnected() == False:
    pass
print('Conexao realizada.')
print(estacao.ifconfig())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

try:
    while True:
        conexao, endereco = s.accept()
        print('Conexao de %s' % str(endereco))
        requisicao = conexao.recv(1024)
        requisicao = str(requisicao)
        print('Conteudo = %s' % requisicao)
        
        if requisicao.find('/led_r/1') != -1:
            print('Acender Led Vermelho')
            led_r.value(1)
        elif requisicao.find('/led_r/0') != -1:
            print('Apagar Led Vermelho')
            led_r.value(0)
        elif requisicao.find('/led_g/1') != -1:
            print('Acender Led Verde')
            led_g.value(1)
        elif requisicao.find('/led_g/0') != -1:
            print('Apagar Led Verde')
            led_g.value(0)
        elif requisicao.find('/led_b/1') != -1:
            print('Acender Led Azul')
            led_b.value(1)
        elif requisicao.find('/led_b/0') != -1:
            print('Apagar Led Azul')
            led_b.value(0)
        
            
            
        else:
            led_r.value(0)
            led_g.value(0)
            led_b.value(0)
            
        html = obter_arquivo('http-led-bootstrap.html')
        conexao.send('HTTP/1.1 200 OK\n')
        conexao.send('Content-Type: text/html\n')
        conexao.send('Connection: close\n\n')
        conexao.sendall(html)
        conexao.close()
        
except KeyboardInterrupt:
    s.close()
    estacao.active(False)
        
