#!/usr/bin/env python

from optparse import OptionParser
import sys
def main():

    usage = "Use: %prog [options] arg"
    parser = OptionParser(usage)
    parser.add_option("-s", "--server", dest="servidor",
                      help="Nome do Servidor")
    parser.add_option("-u", "--ug", dest="ug",
                      help="Nome da UG")
    parser.add_option("-c", "--codigo", dest="codigo",
                      help="Codigo de servico", type="int")
    parser.add_option("-a", "--ambiente", dest="ambiente",
                      help="Tipo do ambiente <Ex: TRE, HOM, PRO>")
    parser.add_option("-n", "--name", dest="nome_aplicacao",
                      help="Nome da aplicacao, nome igual do SIGECOM")
    (options, args) = parser.parse_args()

    
    if options.servidor is None or options.ug is None or options.codigo is None \
        or options.ambiente is None or options.nome_aplicacao is None:
            print 'Erro. Numeros de argumentos invalidos!'
	    sys.exit(1)
    else:
	    print options.servidor
	    print args

if __name__ == '__main__':
    main()
