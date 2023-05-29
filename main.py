from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.properties import BooleanProperty, ObjectProperty
from kivy.lang import Builder

class Person:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
persons = [
            Person("TEJADA JUAN ALBERTO", "0414-2322340", "tejadajalberto@gmail.com/xcuc23@gmail.com"),
            Person("UGUETO CARDIEL XIOMELYS", "0412-7322441", "xiomelyscuc@hotmail.com"),
            Person("SANDOVAL CAMACHO GUSTAVO ENRIQUE", "0414-3320289", "camachoenrique11@gmail.com"),
            Person("LUGO DIAZ CARLOS ALBERTO", "0412-2223002", "lugo.carlos08@gmail.com"),
            Person("RIOBUENO FONSECA NELSON ANTONIO", "0426-5361969", "nriobueno@gmail.com"),
            Person("CHAVEZ GONZALEZ YORFRAN GREGORY", "0414-2118475", "yorfranchavez_24@hotmail.com"),
            Person("CORITZA ESCOBAR", "0412-8206941", "coriescobar07@gmail.com"),
            Person("ALBERTO HAUAYEK", "0412-8030788", "albertohauayek5@gmail.com"),
            Person("BLEQUET DE SOSA MARIA DEL CARMEN", "0414-2398891", "mblequett@gmail.com"),
            Person("RUBÉN MOROCOIMA LÓPEZ", "0426-2136387", "morocoimaruben63@gmail.com"),
            Person("ARGENIS MONASTERIO", "0414-3895170", "argenismonasterio@hotmail.com"),
            Person("DIÓGENES RAFAEL UGUETO GARCÍA", "0412-0104408", "diogenesu@gmail.com"),
            Person("OSWALDO VERASMEDI", "0414-1066091", "oswverasmendi13@gmail.com"),
            Person("GUTIERREZ TORO YAMILET GREGORIA", "0426-9108347", "yamigt@hotmail.com"),
            Person("PEDRA FIQUEROA LUIS ALBERTO", "0414-3251400", "lpedra.64@gmail.com"),
            Person("SUAREZ GONZALEZ DILIA", "0424-2727589", "diliagsg@gmail.com"),
            Person("NORA JOSEFINA ROMERO CARDONA", "0412-8200713", "norajrc61@gmail.com"),
            Person("ROCIO DEL VALLE HERNÁNDEZ DÍAZ", "0412-7165560", "rocihernandezdiaz@gmail.com"),
            Person("RANDY JOSÉ BLANCO BLANCO", "0414-3002642", "randy.blancoblanco60@gmail.com"),
            Person("JESÚS CELESTINO BAEZ LAREZ", "0424-2761138 / 0412-9006108", "jbaez0925@gmail.com"),
            Person("RAQUEL BEHABLY RANGEL CARRILLO", "0424-3144497 / 0412-5896857", "raquelrangel@gmail.com"),
            Person("JULIO MARTINEZ", "0414-1071161", "oyunibe@gmail.com"),
            Person("ELIZABETH MARIA MENDEZ DE MACIAS", "0416-3007171", "elizabethmendezm@hotmail.com"),
            Person("CRISTELA COROMOTO VEGAS DE BOLÍVAR", "0412-5720818", "cristelavegas@gmail.com"),
            Person("HENRY DEL CARMEN RAMIREZ ZAMBRANO", "0416-6211698", "henryramirez1655@gmail.com"),
            Person("MARIELA GONZÁLEZ", "0414-1149118", "angelaaleiram@gmail.com"),
            Person("SANIN NIEVES", "0414-1215100", "saninmiguel@hotmail.com / jaimedelnogal@hotmail.com"),
            Person("JAIME DEL NOGAL", "0414-1086615", "jaimedelnogal.unega@gmail.com"),
            Person("KAREN MÉNDEZ", "0426-3171928", "karenmendezm77@gmail.com"),
            Person("JOSÉ DANIEL APONTE", "0412-3816771", "japonte0403@gmail.com"),
            Person("NINA MAYIRA", "0414-8681892", "ninamayiraromerodelira@gmail.com"),
            Person("WILLIAM LÓPEZ", "0412-9548093", "moralylucesvargas2012@gmail.com"),
            Person("FRANCISCO FORERO", "0414-2886490", "fjforero@gmail.com"),
            Person("JACKMARY HENRIQUEZ RAMOS", "0424-2183643", "jackmary5@hotmail.com"),
            Person("JESÚS CUMARE", "0426-5575654", "jesuscumare@gmail.com / nyorkaduran@gmail.com"),
            Person("NYORKA DURÁN RIVERO", "0412-3973562", "nyorkaduranrivero@gmail.com"),
            Person("CARLOS LESSMAN", "0416-4187169", "carlosluislessman@gmail.com"),
            Person("MOISÉS JIMÉNEZ", "0412-9964441", "moisejimenez16@gmail.com"),
            Person("SUSANA FREITES", "0424-2241565", "susanafm007@gmail.com"),
            Person("YAJAIRA OROPEZA", "0424-1084625", "yajairaoro54@gmail.com"),
            Person("CORIMAR GUZMÁN", "0416-9217824", "corimarguzman@gmail.com"),
            Person("LARRY LÓPEZ", "0414-2617916", "llopez7865@gmail.com"),
            Person("WOLFANG MARTÍNEZ", "0412-3865983", "frankmartinez316@gmail.com"),
            Person("MAURO MIJARES", "0412-2026506", "abgmijaresmauro@gmail.com"),
            Person("GIOVANNI DI TIZZIO", "0424-1530761", ""),
            Person("RAQUEL BENAVIDES", "0424-1978190 / 0424-1978145", "lasirenagil@hotmail.com"),
            Person("BISSETT OJEDA", "0424-2284551", "bibiojeda78@gmail.com"),
            Person("BELLERLY LATÁN", "0412-2652792", "bellerlylatan@gmail.com"),
            Person("DANNY CHACÓN", "0424-1265887", "dannychacon398@gmail.com"),
            Person("ARCADIO ÁLVAREZ", "0414-1369492", "arjosal@gmail.com"),
            Person("NOLIS CUMARE", "0412-8267880", "noliscumareeus@gmail.com"),
            Person("JESSICA ROMERO", "0412-7524486", "jessromerop19@gmail.com"),
            Person("NIURKA CEDEÑO", "0414-1069984", "niurka20039@gmail.com"),
            Person("ZULMA OLIVERO", "0414-2646177", "zulmaolivero@gmail.com"),
            Person("JOSÉ MARÍN", "0424-1828182", "joseeleggua28@gmail.com"),
            Person("JENNIFER SUÁREZ", "0426-4055100", "jenniffer_suarez28@yahoo.es"),
            Person("JESÚS TABLANTE", "0412-5660961", "tablante.j.a@gmail.com"),
            Person("FRANKLIN SÁNCHEZ", "0412-0106698", "franksan16@gmail.com"),
            Person("JHOAN GASPAR", "0416-5953451", "gasparjhoan@gmail.com"),
            Person("ROBERTH LONDOÑO", "0412-5719024", "roberthlondono92@gmail.com"),
            Person("MARIBEL GONZÁLEZ", "0412-8295126", "gdelsea@gmail.com"),
            Person("RICHARD DELGADO", "0416-8100750", "bravotango9@gmail.com"),
            Person("RAMON ALEXANDER VELASQUEZ", "0414-3047934", "alexlobo81@gmail.com / alexlobo81@hotmail.com"),
            Person("RAFAEL BRICEÑO", "0414-9397528", "rafabri_51@hotmail.com"),
            Person("JORGE JOSÉ RODRÍGUEZ REYES", "0424-216-546 / 0412-287-5804", "jjrr24@gmail.com"),
            Person("ZULY MOLINA", "0412-9528093", "zullymarmolina@gmail.com"),
            Person("OSWALDO TOVAR", "0412-5843613", "matematicatovar@gmail.com"),
            Person("VICTORIA RIVAS", "0412-2018636", "vickilagonell@gmail.com"),
            Person("FRANKLIN SÁNCHEZ", "0412-0106698", "franksan16@gmail.com"),
            Person("MARJORIE CLARO", "0412-7084138", "mecs2109@gmail.com"),
            Person("CAROLAY MARTÍNEZ", "0412-0195206", "carolaymartinez30@gmail.com"),
        ]
kv = """
<Cell>:
    size_hint: (None, None)
    width: 400
    height: 60
    canvas.before:
        Color:
            rgba: [0.23, 0.23, 0.23, 1] if self.is_even else [0.2, 0.2, 0.2, 1]
        Rectangle:
            pos: self.pos
            size: self.size

<Table>:
    grid: grid
    bar_width: 25
    scroll_type: ['bars', 'content']
    bar_color: [0.4, 0.7, 0.9, 1]
    bar_inactive_color: [0.2, 0.7, 0.9, .5]
    do_scroll_x: True
    do_scroll_y: True
    GridLayout:
        id: grid
        cols: 3
        rows: 500
        size_hint: (None, None)
        width: self.minimum_width
        height: self.minimum_height
"""

Builder.load_string(kv)


class Cell(Label):
    is_even = BooleanProperty(None)


class Table(ScrollView):

    grid = ObjectProperty(None)

    def __init__(self, *args, **kwargs):
        super(Table, self).__init__(*args, **kwargs)
        for i, person in enumerate(persons):
            text = "Nombre: {}".format(person.name)
            self.grid.add_widget(Cell(text=text))#, is_even=i % 2 is 0))
            text = "Tel: {}".format(person.phone)
            self.grid.add_widget(Cell(text=text))#, is_even=i % 2 is 0))
            text = "Email: {}".format(person.email)
            self.grid.add_widget(Cell(text=text))#, is_even=i % 2 is 0))


class TestApp(App):
    def build(self):
        return Table()


if __name__ == '__main__':
    TestApp().run()