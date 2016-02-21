import socket
import struct


def up(x): return struct.unpack("<I", x)


def p(x): return struct.pack("<I", x & 0xffffffff)


s = socket.socket()
s.connect(("vortex.labs.overthewire.org", 5842))
sum = 0
for i in range(4): sum += up(s.recv(4))[0]
s.send(str(p(sum)))
print s.recv(1024)
s.close()