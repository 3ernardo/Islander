# Writing

file = open('testfile.txt', 'w')

file.write('Teste de escrita e leitura.')

file.close()

# Reading

file = open('testfile.txt', 'r')

print (file.read())