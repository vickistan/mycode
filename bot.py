 #!/usr/bin/python

import socket

network = 'irc.intra.rackspace.com'

port = 6667

irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
irc.connect ( ( network, port ) )
print irc.recv ( 4096 )
irc.send ( 'NICK vbot\r\n' )
irc.send ( 'USER botty botty botty :Python IRC\r\n' )
irc.send ( 'JOIN #vickistan\r\n' )
irc.send ( 'PRIVMSG #vickistan :Hello World.\r\n' )

while True:

   data = irc.recv ( 4096 )
   if data.find ( 'PING' ) != -1:
      irc.send ( 'PONG ' + data.split() [ 1 ] + '\r\n' )

   if data.find ( '!vbot quit' ) != -1:
      irc.send ( 'PRIVMSG #vickistan :Fine, if you dont want me\r\n' )
      irc.send ( 'QUIT\r\n' )

   if data.find ( 'hi vbot' ) != -1:
      irc.send ( 'PRIVMSG #vickistan :I already said hi...\r\n' )

   if data.find ( 'hello vbot' ) != -1:
      irc.send ( 'PRIVMSG #vickistan :I already said hi...\r\n' )

   if data.find ( 'KICK' ) != -1:
      irc.send ( 'JOIN #vickistan\r\n' )

   if data.find ( 'cheese' ) != -1:
      irc.send ( 'PRIVMSG #vickistan :WHERE!!!!!!\r\n' )

   if data.find ( 'slaps vbot' ) != -1:
      irc.send ( 'PRIVMSG #vickistan :This is the Trout Protection Agency. Please put the Trout Down and walk away with your hands in the air.\r\n' )

   print data

