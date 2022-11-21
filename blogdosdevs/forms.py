from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from blogdosdevs.models import Usuario
from flask_login import current_user


class FormCriarConta(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired(message="Este campo é obrigatório"), Length(3, 20, message="Digite um nome de usuário válido")])
    email = StringField('E-mail', validators=[DataRequired(message="Este campo é obrigatório"), Email(message="Digite um e-mail válido")])
    senha = PasswordField('Senha', validators=[DataRequired(message="Este campo é obrigatório"), Length(6, 20, message="Digite uma senha entre 6 a 20 caracteres")])
    confirmacao_senha = PasswordField('Confirmação da Senha', validators=[DataRequired(message="Este campo é obrigatório"), EqualTo('senha', message="As senhas não correspondem")])
    botaosubmit_criarconta = SubmitField('Criar Conta')

    def validate_username(self, username):
        usuario = Usuario.query.filter_by(username=username.data).first()
        if usuario:
            raise ValidationError('Este nome de usuário já existe. Escolha outro nome.')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('E-mail já cadastrado. Cadastre-se com outro e-mail ou faça login para continuar.')


class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(message="Este campo é obrigatório"), Email(message="Digite um e-mail válido")])
    senha = PasswordField('Senha', validators=[DataRequired(message="Este campo é obrigatório"), Length(6, 20, message="Digite uma senha entre 6 a 20 caracteres")])
    lembrar_dados = BooleanField('Mantenha-me conectado')
    botaosubmit_login = SubmitField('Login')


class FormEditarPerfil(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired(message="Este campo é obrigatório"), Length(3, 20, message="Digite um nome de usuário válido")])
    email = StringField('E-mail', validators=[DataRequired(message="Este campo é obrigatório"), Email(message="Digite um e-mail válido")])
    senha = PasswordField('Senha', validators=[DataRequired(message="Este campo é obrigatório"), Length(6, 20, message="Digite uma senha entre 6 a 20 caracteres")])
    foto_perfil = FileField('Atualizar Foto de Perfil', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])

    linguagem_html_css = BooleanField('HTML / CSS')
    linguagem_js = BooleanField('JavaScript')
    linguagem_dotnet = BooleanField('C / C+ / C++ / C#')
    linguagem_php = BooleanField('PHP')
    linguagem_python = BooleanField('Python')
    linguagem_java = BooleanField('Java')
    linguagem_r = BooleanField('R')
    linguagem_ruby = BooleanField('Ruby')
    linguagem_sql = BooleanField('SQL / PostgreSQL / Oracle / SQL Server')

    botaosubmit_editarperfil = SubmitField('Confirmar Edições')

    def validate_email(self, email):
        if current_user.email != email.data:
            usuario = Usuario.query.filter_by(email=email.data).first()
            if usuario():
                raise ValidationError('Já existe um usuário com esse email. Insira outro e-mail.')

    def validate_username(self, username):
        if current_user.username != username.data:
            usuario = Usuario.query.filter_by(username=username.data).first()
            if usuario():
                raise ValidationError('Já existe um usuário com esse username. Insira outro username.')


class FormCriarPost(FlaskForm):
    titulo = StringField('Título do Post', validators=[DataRequired(), Length(2, 150)])
    corpo = TextAreaField('Escreva seu post aqui', validators=[DataRequired()])
    botaosubmit = SubmitField('Criar Post')


class FormEditarPost(FlaskForm):
    titulo = StringField('Título do Post', validators=[DataRequired(), Length(2, 150)])
    corpo = TextAreaField('Escreva seu post aqui', validators=[DataRequired()])
    botaosubmit = SubmitField('Editar Post')

