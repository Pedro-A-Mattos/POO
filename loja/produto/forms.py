from wtforms import Form, SubmitField,IntegerField,FloatField,StringField,TextAreaField,validators
from flask_wtf.file import FileField,FileRequired,FileAllowed

class Addproducts(Form):
    name = StringField('Nome', [validators.DataRequired()])
    price = FloatField('Preço', [validators.DataRequired()])
    discount = IntegerField('Desconto', default=0)
    stock = IntegerField('Estoque', [validators.DataRequired()])
    colors = StringField('Cor', [validators.DataRequired()])
    desc = TextAreaField('Descrição', [validators.DataRequired()])

    image_1 = FileField('Image 1', validators=[FileRequired(), FileAllowed(['jpg','png','gif','jpeg']), 'Images only please'])
    image_2 = FileField('Image 2', validators=[FileRequired(), FileAllowed(['jpg','png','gif','jpeg']), 'Images only please'])
    image_3 = FileField('Image 3', validators=[FileRequired(), FileAllowed(['jpg','png','gif','jpeg']), 'Images only please'])
