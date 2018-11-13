i = 1
for it in range(20):
    i_str = str(i)
    filename = i_str + '.js'
    f = open(filename, 'w')

    f.write("console.log('>>>>>>>>" + i_str + "')")
    f.close()
    i = i + 1