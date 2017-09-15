#!/bin/env python
import ldap
import sys
#import pdb
_ldap_host = '10.0.0.0'
_ldap_port = '389'
_bind_dn = 'uid=user,ou=corp,dc=foo,dc=gov,dc=br'
_pw = 'pass'
_base_dn = 'dc=foo,dc=gov,dc=br'
_filter = '(&(objectclass=foousr)(|(uid=' + sys.argv[1]+ ')))'
_attrs = ['cn']


def _connect(h = _ldap_host + ':' + _ldap_port):
  l = ldap.initialize('ldap://' + h)
  try:
    l.protocol_version = ldap.VERSION3
    l.simple_bind_s(_bind_dn, _pw) 
  except ldap.INVALID_CREDENTIALS:
    print "Falha no login com LDAP!"
    sys.exit(0)
  except ldap.LDAPError, e:
    if type(e.message) == dict and e.message.has_key('desc'):
      print e.message['desc']
    else: 
      print e
    sys.exit(0)
  try:
    id_l = l.search( _base_dn, ldap.SCOPE_SUBTREE, _filter, _attrs )
    result_set = []
    while 1:
        result_type, result_data = l.result(id_l, 0)
        if (result_data == []):
            break
        else:
            if result_type == ldap.RES_SEARCH_ENTRY:
                result_set.append(result_data)
    print result_set
  except ldap.LDAPError, e:
    print('Falha para realizar a busca no ldap. Erro: '+ e)
    #pdb.set_trace()
    l.unbind_s()
  l.unbind_s()

def _check_pars():
  if len(sys.argv) != 2:
    print('***Erro***\nUse: myLdap.py <user>')
  else:
    _connect()

_check_pars()
