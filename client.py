from telnetlib import Telnet

client = Telnet()
client.open('alt.org')

print client.read_until('=>')

client.write('l') # Login
client.write('barbershopper' + '\n') # Username
client.write('thisisabadpassword' + '\n') # Password
client.write('p') # Play
client.write('y' + '\n') # Don't randomize for me

## Setup character
#client.write('b') # Barberian
#client.write('o') # Orc
#client.write('f') # Female


print repr(client.read_until('=>'))
print repr(client.read_until('=>'))
print repr(client.read_until('=>'))
print repr(client.read_until('=>'))

