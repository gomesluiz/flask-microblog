
Este comando criará os diretórios e arquivos necessários para migrações de banco de dados.
```bash
$ flask db init
```

Run flask db upgrade to apply the migration and create the users table in your database.

```bash
$ flask db migrate -m 'users table'
```
Execute o comando a seguir para aplicar a migração ao seu banco de dados. Este comando executa o script de migração e atualiza o esquema do seu banco de dados de acordo.
```bash
$ flask db upgrade
```

Este comando reverte seu banco de dados para seu estado inicial, que é a migração base.
```bash
$ flask db downgrade base
```
Este comando é útil quando você deseja:

* Redefinir seu banco de dados: Se você fez alterações e quer começar do zero, reverter para a migração base removerá todas as migrações subsequentes e deixará seu banco de dados em seu estado original.
* Corrigir problemas: Se uma migração causou problemas, reverter para a migração base pode ajudar você a se recuperar e então reaplicar as migrações corretas.

