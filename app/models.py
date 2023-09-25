from django.db import models


class cidades(models.Model):
    
    nome = models.CharField(max_length=35)
    uf = models.CharField(max_length=2)
    

class ocupacao(models.Model):
    
    nome = models.CharField(max_length=20)
    
    def __str__(self):
        return f'Ocupação: {self.nome}'


class pessoas(models.Model):
    
    nome = models.CharField(max_length=50)
    pai = models.CharField(max_length=50)
    mae = models.CharField(max_length=50)
    cpf = models.CharField(max_length=14)
    data_nasc = models.DateField()
    email = models.EmailField(max_length=100)
    cidades = models.ForeignKey(cidades,
                                on_delete=models.CASCADE)
    ocupacao = models.ForeignKey(ocupacao, 
                                 on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Aluno: {self.nome} - CPF: {self.cpf}'
    
    


    


class instituicao(models.Model):
    
    nome = models.CharField(max_length=100)
    site = models.CharField(max_length=150)
    telefone = models.IntegerField()
    
    def __str__(self):
        return f'Instituição: {self.nome} - Site: {self.site} - Telefone: {self.telefone}'
    

class areas_saber(models.Model):
    
    nome = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome
    
    

class cursos(models.Model):
    
    nome = models.CharField(max_length=20)
    carga_horaria_total = models.PositiveIntegerField()
    duracao_meses = models.PositiveIntegerField()
    areas_saber = models.ForeignKey(areas_saber,
                                    on_delete=models.CASCADE)
    instituicao = models.ForeignKey(instituicao,
                                    on_delete=models.CASCADE)
    

class periodo(models.Model):
    
    nome = models.CharField(max_length=20) 
    
    def __str__(self):
        return self.nome
    

class disciplinas(models.Model):
    
    nome = models.CharField(max_length=20)
    areas_saber=models.ForeignKey(areas_saber,
                                  on_delete=models.CASCADE)
    
    def __str__(self):
        return  f'Nome: {self.nome} - Disciplina: {self.areas_saber}'
    
    
class matriculas(models.Model):
    
    instituicao=models.ForeignKey(instituicao,on_delete=models.CASCADE)
    cursos=models.ForeignKey(cursos,on_delete=models.CASCADE)
    pessoas=models.ForeignKey(pessoas,on_delete=models.CASCADE)
    data_inicio=models.DateField()
    data_previsao_termino=models.DateField()
    
    def __str__(self):
        return f'Instituição: {self.instituicao} - Cursos: {self.cursos} - Pessoa: {self.pessoas} - Data Inicio: {self.data_inicio} - Data Termino: {self.data_previsao_termino}'


class avaliacoes(models.Model):
    
    descricao=models.CharField(max_length=200)
    cursos=models.ForeignKey(cursos,
                             on_delete=models.CASCADE)
    disciplinas=models.ForeignKey(disciplinas,
                                  on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Descrição: {self.descricao} - Cursos: {self.cursos} - Disciplinas: {self.disciplinas}'
    
    
class frequencia(models.Model):
    
    cursos=models.ForeignKey(cursos,
                             on_delete=models.CASCADE)
    disciplinas=models.ForeignKey(disciplinas,
                                  on_delete=models.CASCADE)
    numero_faltas=models.IntegerField()
    
    def __str__(self):
        return f'Cursos: {self.cursos} - Disciplinas: {self.disciplinas} - Numero Faltas: {self.numero_faltas}'
        
    
    
class turmas(models.Model):
    
    nome = models.CharField(max_length=10)
    periodo=models.ForeignKey(periodo,
                              on_delete=models.CASCADE)
    def __str__(self):
        return f'Nome: {self.nome} - Periodo: {self.periodo}'



    
    
class ocorrencias(models.Model):
    
    descricao = models.CharField(max_length=200)
    data = models.DateField()
    cursos = models.ForeignKey(cursos,
                               on_delete=models.CASCADE)
    disciplinas = models.ForeignKey(disciplinas,
                                    on_delete=models.CASCADE)
    pessoas = models.ForeignKey(pessoas,
                                on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Descrição: {self.descricao} - Data: {self.data} - Cursos: {self.cursos} - Disciplinas: {self.disciplinas} - Pessoa: {self.pessoas}'
    
    
class disciplinas_por_cursos(models.Model):
    
    nome = models.CharField(max_length=40)
    carga_horaria = models.PositiveIntegerField()
    cursos = models.ForeignKey(cursos,
                               on_delete=models.CASCADE)
    periodo = models.ForeignKey(periodo,
                                on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Nome: {self.nome} - Carga Horaria: {self.carga_horaria} - Curso: {self.cursos} - Periodo: {self.periodo}'
class avaliacao (models.Model):
    
    prova = models.CharField(max_length=50)
    trabalho = models.CharField(max_length=50)
    projeto = models.CharField(max_length=50)
    lista_exercicio = models.CharField(max_length=50)
    
    def __str__(self):
        return f'Prova: {self.prova} - Trabalho {self.trabalho} - Projeto {self.projeto} - Lista Exercicio: {self.lista_exercicio}'
        